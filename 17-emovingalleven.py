numbers = input('enter list of natural numbers (space-separated): ').split()
nums = [int(x) for x in numbers if x.strip() != '']
evens = [n for n in nums if n % 2 == 0]
odds = [n for n in nums if n % 2 != 0]
print("Original list:", nums)
print("Even numbers:", evens)
print("Odd numbers:", odds)
