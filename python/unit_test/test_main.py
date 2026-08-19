from main import getWeather, checkPalindrome

# Unit tests for main.py using PyTest
# Surjit Randhawa 2026

def test_getWeather():
	assert getWeather(21) == "hot"
	assert getWeather(20) == "cold"
	assert getWeather(19) == "cold"
	assert getWeather(0) == "cold"
	assert getWeather(-1) == "cold"
	
def test_checkPalindrome():
	assert checkPalindrome("madam") == True
	assert checkPalindrome("apple") == False
	assert checkPalindrome(None) == False