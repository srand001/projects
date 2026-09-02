#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>

// Function to reverse individual words while keeping spaces/structure intact
std::string reverseWordsInLine(const std::string& line) {
    std::string result = "";
    std::string word = "";

    for (char ch : line) {
        // If we encounter a space or punctuation that splits words,
        // reverse the accumulated word and add it to the result
        if (std::isspace(ch)) {
            std::reverse(word.begin(), word.end());
            result += word;
            result += ch; // Keep the original whitespace
            word = "";    // Reset for the next word
        } else {
            word += ch;
        }
    }

    // Don't forget the last word if the line didn't end with a space
    if (!word.empty()) {
        std::reverse(word.begin(), word.end());
        result += word;
    }

    return result;
}

int main() {
    std::string inputFilename = "harry_potter.txt";
    std::string outputFilename = "output.txt";

    std::ifstream inputFile(inputFilename);
    std::ofstream outputFile(outputFilename);

    // Check if the input file exists and can be opened
    if (!inputFile.is_open()) {
        std::cerr << "Error: Could not open the input file '" << inputFilename << "'." << std::endl;
        return 1;
    }

    // Check if the output file can be created/opened
    if (!outputFile.is_open()) {
        std::cerr << "Error: Could not create or open the output file '" << outputFilename << "'." << std::endl;
        inputFile.close();
        return 1;
    }

    std::string line;
    // Read the input file line by line
    while (std::getline(inputFile, line)) {
        std::string processedLine = reverseWordsInLine(line);
        outputFile << processedLine << "\n";
    }

    std::cout << "File processing completed successfully!" << std::endl;
    std::cout << "Transformed text saved to '" << outputFilename << "'." << std::endl;

    // Close the file streams
    inputFile.close();
    outputFile.close();

    return 0;
}
