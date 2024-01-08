def check_palindrome(s):
    new_str = ""
    for char in s:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
            if 'A' <= char <= 'Z':
                char = chr((ord(char) - ord('A')) + ord('a'))
            new_str += char

    n = len(new_str)
    for i in range(n // 2):
        if new_str[i] != new_str[n - i - 1]:
            return False
    return True


input_str = "A man, a plan, a canal, Panama!"
result = check_palindrome(input_str)
print(result)
