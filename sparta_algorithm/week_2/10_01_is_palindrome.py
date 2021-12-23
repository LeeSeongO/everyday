input = "tomato"


def is_palindrome(string):
    n = len(input)
    for i in range(len(input) // 2):
        if input[i] != input[n - i - 1]:
            return False

    return True


print(is_palindrome(input))
print(len(input) // 2)