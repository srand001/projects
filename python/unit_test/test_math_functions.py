from math_functions import add, multiply, divide, square_root

# Unit tests for math_functions.py using PyTest
# Surjit Randhawa 2026

def test_add():
	assert add(0,0) == 0
	assert add(0,1) == 1
	assert add(1,0) == 1
	assert add(1,2) == 3
	assert add(-1,2) == 1
	assert add(1,-2) == -1
	assert add(-1,-2) == -3
	assert add(1,0.5) == 1.5

def test_multiply():
	assert multiply(0,0) == 0
	assert multiply(0,1) == 0
	assert multiply(1,0) == 0
	assert multiply(1,2) == 2
	assert multiply(-1,2) == -2
	assert multiply(1,-2) == -2
	assert multiply(-1,-2) == 2
	assert multiply(2, 2.5) == 5
	assert multiply(2.5, 2.5) == 6.25

def test_divide():
	assert divide(10,2) == 5
	assert round(divide(10,3),5) == 3.33333
	assert divide(0,1) == 0
	assert divide(0,0) == None # Check for divide by zero error
	assert divide(1,0) == None # Check for divide by zero error

def test_square_root():
	assert square_root(0) == 0
	assert square_root(25) == 5
	assert round(square_root(2),5) == 1.41421
	assert square_root(-1) == None # Cannot have square root of a negative number
	
