from operations.arithmetic import add, multiply
from operations.string_ops import reverse_string, count_vowels

print("Addition:", add(5, 3))
print("Multiplication:", multiply(5, 3))

text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))
print("Vowel count:", count_vowels(text))
