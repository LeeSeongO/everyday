input = 5

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

# n = 3
# Fibo(100) -> Fibo(99) -> Fibo(98) 위에서 Top Down 방식
# Fibo(1) -> Fibo(2) -> Fibo(3) -> Bottom up 방식
def fibo_dynamic_programming_top_down(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming_top_down(n - 1, fibo_memo) + fibo_dynamic_programming_top_down(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return fibo_memo[n]

def fibo_dynamic_programming_bottom_up(n):
    bottom_up = {1: 1, 2: 1}

    for num in range(3, n+1):
        bottom_up[num] = bottom_up[num - 1] + bottom_up[num - 2]

    return bottom_up[n]


print(fibo_dynamic_programming_top_down(input, memo))
print(fibo_dynamic_programming_bottom_up(input))