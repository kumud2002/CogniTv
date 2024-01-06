def reverse_words(input_string):
    words = input_string.split()
    reverse_string = " ".join(reversed(words))
    return reverse_string

input_string = input("Input string to be reversed :")
result = reverse_words(input_string)
print("Reversed String :",result)