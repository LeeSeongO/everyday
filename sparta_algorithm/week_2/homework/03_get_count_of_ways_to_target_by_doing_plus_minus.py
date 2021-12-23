numbers = [1, 1, 1, 1, 1]
target_number = 3


# BFS를 이용한 풀이
def get_count_of_ways_to_target_by_doing_plus_or_minus(arrays, target):
    number_of_cases = [0]  # 모든 경우의 수를 저장할 리스트
    answer = 0  # number_of_cases 와 target 값을 비교후 카운트할 변수

    for array in arrays:
        temp = []  # number_of_cases 의 값이 변하면 연산할 수 없으므로 임시 리스트 선언
        for number in number_of_cases:
            temp.append(number + array)  # number_of_cases 값들에 + 연산
            temp.append(number - array)  # number_of_cases 값들에 - 연산
        number_of_cases = temp  # 다음 숫자의 +, - 한 경우의 수들을 다시 number_of_cases 에 저장

    # number_of_cases 값들과 target 비교해서 answer 값을 카운트하는 부분
    for num in number_of_cases:
        if num == target:
            answer += 1

    return answer


# DFS 풀이
def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer

def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else: return 0
    else:
        answer += DFS(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth+1)
        return answer


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!