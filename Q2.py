def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

# Main program
text = input("Enter string: ")
ans = count_vowels(text)
print("Vowels:", ans)