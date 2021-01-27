import re
line = "Luke, I am your father!"
result = re.findall(r'\w{4}', line)
print(result)
