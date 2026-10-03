#--------------------------------------------------------------------
# Password Checker
# ----------------
#
# Check if a password matches ALL of the following:
# Longer than 8 chars
# One or more integers
# One or more lower case letter
# One or more Upper case letter
# One or more special chars
#
# Designed by Surjit Randhawa 2026
#--------------------------------------------------------------------

import re  # Regular Expression (RegEx) library

def check_password(password):
  if len(password) < 8:
    return False
  elif re.search('[0-9]',password) is None:
    return False
  elif re.search('[a-z]',password) is None:
    return False
  elif re.search('[A-Z]',password) is None:
    return False
  elif re.search('[@#$^&]',password) is None:
    return False
  return True
    
for password in ["12345678", "Abcd@1234"]:
  if(check_password(password)):
    print(password, " is a strong password.")
  else:
    print(password, " is a weak password.")


if __name__ == "__main__":

	# Examples
	check_password("01234567")  # A weak password
	check_password("Xyz@1234")  # A strong password



