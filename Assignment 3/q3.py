def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)
def count_consonants(s):
    return sum(1 for ch in s if ch.isalpha() and ch not in "aeiouAEIOU")
s = input("Enter string: ")
v = count_vowels(s)
c = count_consonants(s)
print("Vowels:", v)
print("Consonants:", c)
if c != 0:
    print("Ratio:", v/c)