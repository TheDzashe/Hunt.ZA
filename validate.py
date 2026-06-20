import re

def is_valid(email):
    regex = (r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$")
    if not re.search(regex, email):
        return False
    return True

result = is_valid("@example.capetown")
print (result)