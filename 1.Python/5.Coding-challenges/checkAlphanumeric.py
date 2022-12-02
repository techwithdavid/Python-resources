"abdc1321".isalnum()  # Output: True
"xyz@123$".isalnum()  # Output: False
# Another way is to use match() method from the re(regex) module as shown:

import re
print(bool(re.match('[A-Za-z0-9]+$', 'abdc1321')))  # Output: True
print(bool(re.match('[A-Za-z0-9]+$', 'xyz@123$')))
