my_string = "Hello, World!"
count = 0
for char in my_string:
    if char.lower() in 'aeiou':
        count += 1
print("Number of vowels:", count)
