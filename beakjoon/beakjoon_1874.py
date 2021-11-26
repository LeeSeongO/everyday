# 반복할 횟수를 입력
n = int(input())

# 수열을 저장할 stack_list, "+", "-"을 저장할 oper_list
stack_list = []
oper_list = []

# 증가하거나 감소하면서 스택에 저장할 숫자
num = 1

# 오류를 체크할 변수 flag
flag = 0


# n 만큼 반복한다
for _ in range(n):
    value = int(input())  # 수열에서 pop 할 값을 입력 받는다

    while num <= value:  # num 과 value 값이 같을때까지 반복
        stack_list.append(num)  # stack_list 에 num 값 push
        oper_list.append("+")  # stack 을 push 하기때문에 oper_list 에 "+" 저장
        num += 1  # num 값을 1만큼 증가

    if stack_list[-1] == value:  # LIFO 문제이기때문에 stack_list TOP 값이 value 값이면 꺼낼 수 있다.
        stack_list.pop()
        oper_list.append("-")  # stack 을 pop 하기때문에 oper_list 에 "-"저장
    else:  # 꺼낼 수 없는 값이면 오류를 체크하는 flag 변수에 1을 저장
        flag = 1

# flag 값이 0 이면 정상적인 oper_list 값들 출력, 1이면 비정상적이므로 NO 를 출력
if flag == 0:
    for i in oper_list:
        print(i)
elif flag == 1:
    print("NO")
