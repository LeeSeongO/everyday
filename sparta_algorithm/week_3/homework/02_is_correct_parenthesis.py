s = "(())()"


def is_correct_parenthesis(string):
    """
    parenthesis_left = 0
    parenthesis_right = 0

    for parenthesis in string:
        if parenthesis == '(':
            parenthesis_left += 1
        elif parenthesis == ')':
            parenthesis_right += 1
            if parenthesis_left < parenthesis_right:
                return False

    if parenthesis_left != parenthesis_right:
        return False
    else:
        return True

    """

    stack = []

    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        elif string[i] == ')':
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True

print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))