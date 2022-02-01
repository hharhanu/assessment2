import re

string = "TODAYS DATE: 01/29. This is my assessment-2! I have to submit by Tuesday!"
upper= re.findall(r"[A-Z]", string)
lower = re.findall(r"[a-z]", string)
special = re.findall(r"[:/.!-]", string)
number = re.findall(r"[0-9]", string)
white_space_character = re.findall(r"[ ]", string)
print("Uppercase_count:", len(upper))
print("lowercase_count:", len(lower))
print("special_character_count:", len(special))
print("number_count:", len(number))
print("white_space_character:", len(white_space_character))
