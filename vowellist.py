#form a list of vowel from a given word
def c():
    word=input("Enter a word\t").lower()
    List=[x for x in word if x=="a" or x=="e" or x=="i" or x=="o" or x=="u"]
    print(List)
c()