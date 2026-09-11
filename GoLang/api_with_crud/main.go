
// RESTful CRUD API written in Go. 
// Supports Create, Update and Delete of JSON data
// Designed by Surjit Randhawa 2026

package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"sync"
	"time"

	"://github.com"
	"golang.org/x/time/rate"
)

// Const Configuration
const (
	DBFile    = "database.json"
	APIKey    = "API_KEY_SECRET_VALUE" // Sample Security Key
	RateLimit = 5                      // 5 requests per second
	RateBurst = 10                     // Maximum burst size
)

// Product represents the structure of data stored in our JSON database
type Product map[string]interface{}

// Global Application Core
var (
	dbMutex      sync.RWMutex
	limiterMap   = make(map[string]*rate.Limiter)
	limiterMutex sync.Mutex
)

// Product Schema Definition for input validation
const ProductSchema = `{
	"$schema": "http://json-schema.org",
	"title": "Product",
	"type": "object",
	"properties": {
		"id": { "type": "string" },
		"name": { "type": "string", "minLength": 3 },
		"price": { "type": "number", "minimum": 0 },
		"tags": {
			"type": "array",
			"items": { "type": "string" }
		},
		"in_stock": { "type": "boolean" }
	},
	"required": ["id", "name", "price"]
}`

// --- DATABASE CORE HELPER FUNCTIONS ---

func readDB() ([]Product, error) {
	dbMutex.RLock()
	defer dbMutex.RUnlock()

	file, err := os.ReadFile(DBFile)
	if err != nil {
		if os.IsNotExist(err) {
			return []Product{}, nil
		}
		return nil, err
	}

	var products []Product
	if err := json.Unmarshal(file, &products); err != nil {
		return nil, err
	}
	return products, nil
}

func writeDB(products []Product) error {
	dbMutex.Lock()
	defer dbMutex.Unlock()

	data, err := json.MarshalIndent(products, "", "  ")
	if err != nil {
		return err
	}
	return os.WriteFile(DBFile, data, 0644)
}

// --- SECURITY & RATE LIMIT MIDDLEWARES ---

func getLimiter(ip string) *rate.Limiter {
	limiterMutex.Lock()
	defer limiterMutex.Unlock()

	limiter, exists := limiterMap[ip]
	if !exists {
		// Allows 'RateLimit' tokens/sec with a max capacity capacity of 'RateBurst'
		limiter = rate.NewLimiter(rate.Limit(RateLimit), RateBurst)
		limiterMap[ip] = limiter
	}
	return limiter
}

// SecurityCheck validates API token authentication and applies IP Rate Limiting
func SecurityCheck(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")

		// 1. Rate Limiting Check (per Remote IP Addr)
		limiter := getLimiter(r.RemoteAddr)
		if !limiter.Allow() {
			w.WriteHeader(http.StatusTooManyRequests)
			json.NewEncoder(w).Encode(map[string]string{"error": "Rate limit exceeded. Too many requests."})
			return
		}

		// 2. Authentication Check via Authorization header
		key := r.Header.Get("X-API-KEY")
		if key != APIKey {
			w.WriteHeader(http.StatusUnauthorized)
			json.NewEncoder(w).Encode(map[string]string{"error": "Unauthorized. Invalid or missing X-API-KEY header."})
			return
		}

		next.ServeHTTP(w, r)
	}
}

// --- JSON SCHEMA VALIDATOR ---

func validateJSONSchema(jsonData []byte) error {
	schemaLoader := gojsonschema.NewStringLoader(ProductSchema)
	documentLoader := gojsonschema.NewBytesLoader(jsonData)

	result, err := gojsonschema.Validate(schemaLoader, documentLoader)
	if err != nil {
		return err
	}

	if !result.Valid() {
		var schemaErrors string
		for _, desc := range result.Errors() {
			schemaErrors += fmt.Sprintf("- %s; ", desc.String())
		}
		return fmt.Errorf("schema validation failed: %s", schemaErrors)
	}
	return nil
}

// --- CRUD ENDPOINT HANDLERS ---

func handleProducts(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet: // READ (List All)
		products, err := readDB()
		if err != nil {
			http.Error(w, `{"error":"Internal server error"}`, http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(products)

	case http.MethodPost: // CREATE
		body, err := io.ReadAll(r.Body)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(map[string]string{"error": "Invalid payload"})
			return
		}

		// JSON Schema validation before inserting
		if err := validateJSONSchema(body); err != nil {
			w.WriteHeader(http.StatusUnprocessableEntity)
			json.NewEncoder(w).Encode(map[string]string{"error": err.Error()})
			return
		}

		var newProduct Product
		_ = json.Unmarshal(body, &newProduct)

		products, _ := readDB()
		// Prevent ID Duplication
		for _, p := range products {
			if p["id"] == newProduct["id"] {
				w.WriteHeader(http.StatusConflict)
				json.NewEncoder(w).Encode(map[string]string{"error": "Conflict: Product ID already exists"})
				return
			}
		}

		products = append(products, newProduct)
		if err := writeDB(products); err != nil {
			http.Error(w, `{"error":"Could not save resource"}`, http.StatusInternalServerError)
			return
		}

		w.WriteHeader(http.StatusCreated)
		json.NewEncoder(w).Encode(newProduct)

	default:
		w.WriteHeader(http.StatusMethodNotAllowed)
	}
}

func handleProductByID(w http.ResponseWriter, r *http.Request) {
	// Extract Path ID suffix natively via basic routing mechanics
	id := r.URL.Path[len("/api/products/"):]
	if id == "" {
		w.WriteHeader(http.StatusBadRequest)
		json.NewEncoder(w).Encode(map[string]string{"error": "Missing item ID"})
		return
	}

	products, err := readDB()
	if err != nil {
		http.Error(w, `{"error":"Internal server error"}`, http.StatusInternalServerError)
		return
	}

	switch r.Method {
	case http.MethodGet: // READ (Single item)
		for _, p := range products {
			if p["id"] == id {
				json.NewEncoder(w).Encode(p)
				return
			}
		}
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Product not found"})

	case http.MethodPut: // UPDATE
		body, err := io.ReadAll(r.Body)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}

		if err := validateJSONSchema(body); err != nil {
			w.WriteHeader(http.StatusUnprocessableEntity)
			json.NewEncoder(w).Encode(map[string]string{"error": err.Error()})
			return
		}

		var updatedProduct Product
		_ = json.Unmarshal(body, &updatedProduct)

		// Overwrite target entity properties inside index slice mapping
		found := false
		for i, p := range products {
			if p["id"] == id {
				// Prevent path ID mismatch payload manipulation
				updatedProduct["id"] = id 
				products[i] = updatedProduct
				found = true
				break
			}
		}

		if !found {
			w.WriteHeader(http.StatusNotFound)
			json.NewEncoder(w).Encode(map[string]string{"error": "Product not found"})
			return
		}

		_ = writeDB(products)
		json.NewEncoder(w).Encode(updatedProduct)

	case http.MethodDelete: // DELETE
		found := false
		for i, p := range products {
			if p["id"] == id {
				products = append(products[:i], products[i+1:]...)
				found = true
				break
			}
		}

		if !found {
			w.WriteHeader(http.StatusNotFound)
			json.NewEncoder(w).Encode(map[string]string{"error": "Product not found"})
			return
		}

		_ = writeDB(products)
		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(map[string]string{"message": "Product successfully deleted"})

	default:
		w.WriteHeader(http.StatusMethodNotAllowed)
	}
}

// --- Main Function ---

func main() {
	mux := http.NewServeMux()

	// Register CRUD routing patterns mapped into the security wrapping layer
	mux.HandleFunc("/api/products", SecurityCheck(handleProducts))
	mux.HandleFunc("/api/products/", SecurityCheck(handleProductByID))

	server := &http.Server{
		Addr:         ":8080",
		Handler:      mux,
		ReadTimeout:  10 * time.Second,
		WriteTimeout: 10 * time.Second,
	}

	log.Println("Server executing natively on port :8080...")
	if err := server.ListenAndServe(); err != nil && err != http.ErrServerClosed {
		log.Fatalf("Server allocation failure error: %v", err)
	}
}
