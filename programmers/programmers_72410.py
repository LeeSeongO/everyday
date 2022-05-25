"""
프로그래머스 // 카카오 // 신규 아이디 추천 // 72410
"""
import re


def solution(new_id: str) -> str:
    # 얕은 복사
    answer = new_id[:]
    # 1단계 소문자
    answer = answer.lower()
    print(f'1단계: {answer}')
    # 2단계 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    answer = re.sub('[^\w\-\_\.]', '', answer)
    print(f'2단계: {answer}')
    # 3단계 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    answer = re.sub('[\.]{2,}', '.', answer)
    print(f'3단계: {answer}')
    # 4단계 마침표(.)가 처음이나 끝에 위치한다면 제거
    answer = re.sub('^[\.]|[\.]$', '', answer)
    print(f'4단계: {answer}')
    # 5단계 new_id가 빈문자열이면 a를 대입
    if answer == "":
        answer = 'a'
    print(f'5단계: {answer}')
    # 6단계 new_id 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지는 제거, 만약 제거 후 마침표(.) 가 마지막에 위치한다면 마침표도 제거
    if len(answer) >= 16:
        answer = answer[:15]
        answer = re.sub('[\.]$', '', answer)
    print(f'6단계: {answer}')
    while len(answer) <= 2:
        answer += answer[-1]
    print(f'7단계: {answer}')

    return answer


test_str = 'z-+.^.'
test_str1 = '...!@BaT#*..y.abcdefghijklm'
solution('')

