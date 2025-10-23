word = input("Enter a string: ")
if len(word) >= 3 and word[-3:] == "ing":
    word = word + "ly"
else:
    word = word + "ing"

print("Modified string:", word)
