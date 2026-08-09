from math_functions import add, multiply, divide, square_root

def test_add():
	assert add(0,0) == 0
	assert add(1,2) == 3


def test_multiply():
	assert multiply(0,0) == 0
	assert multiply(1,2) == 2
	
	
def test_divide():
	assert divide(10,2) == 5
	assert divide(0,0) == None
	

def test_square_root():
	assert square_root(0) == 0
	assert square_root(25) == 5
	assert square_root(-1) == None
	
	
