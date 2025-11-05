def charfreq():
    li = input("Enter a line of text: ")
    dic = {}
    for ch in li:
        dic[ch] = dic.get(ch, 0) + 1
    print("The number of frequency of each character:")
    for ch, count in dic.items():
        print(f"Character: '{ch}', appeared {count} time(s)")
charfreq()
