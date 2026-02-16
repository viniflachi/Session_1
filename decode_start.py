alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
message = ""
with open("secret.txt") as f:
    for line in f:
       # print(line) # instead of print, you should start decoding
        nr_vowels = 0
        for v in vowel:
           nr_vowels += line.count(v) # count the amount of time that particular vowel shows up
        letter = alphabet[nr_vowels] # optional line
        message += letter
        # message += alphabet[nr_vowels] # same as the 2 previous lines combined
print(message)