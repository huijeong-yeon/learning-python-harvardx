text = input("Input: ")
vowels = "aeiouAEIOU"

result = ""
for c in text:
    if c not in vowels:
        result += c

print("Output:", result)
