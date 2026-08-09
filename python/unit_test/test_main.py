from main import getWeather, checkPalindrome


def test_getWeather():
	assert getWeather(21) == "hot"
	assert getWeather(20) == "cold"
	assert getWeather(19) == "cold"

	
def test_checkPalindrome():
	assert checkPalindrome("madam") == True
	assert checkPalindrome("apple") == False
