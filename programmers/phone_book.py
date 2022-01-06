# 문제 설명
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
#
# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false 를 그렇지 않으면 true 를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# phone_book 의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.

# 조건1 : 다른 번호의 접두어이려면 크기가 작아야한다.

# from collections import deque

phone_book = [["119", "97674223", "1195524421"], ["123", "456", "789"], ["12", "123", "1235", "567", "88"]]


def solution(phone_book_array: list) -> bool:
    answer = True
    phone_book_sort = sorted(phone_book_array)

    for i in range(len(phone_book_sort) - 1):
        if len(phone_book_sort[i]) < len(phone_book_sort[i + 1]):
            if phone_book_sort[i] == phone_book_sort[i + 1][:len(phone_book_sort[i])]:
                answer = False
                break

    return answer


for i in range(len(phone_book)):
    print(solution(phone_book[i]))

# from collections import deque

# phone_book_sort = deque(sorted(phone_book_array, key=len))
#
#     for i in range(len(phone_book_sort) - 1):
#         phone_number_pop = phone_book_sort.popleft()
#
#         for phone_number in phone_book_sort:
#             if phone_number_pop == phone_number[:len(phone_number_pop)]:
#                 answer = False
#                 break

