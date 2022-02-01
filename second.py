import re
s = 'https://mail.google.com:1010/mail/'

obj = re.findall('://([\w\-\.]+)(:(\d+))?', s)
print("URL",obj)
obj1 = re.findall('://([\w\-\.]+)', s)
print("Hostname",obj1)
obj2 = re.findall('(\w+)://', s)
print("protocol",obj2)
obj3 = re.findall('\d+', s)
print("port number",obj3)
