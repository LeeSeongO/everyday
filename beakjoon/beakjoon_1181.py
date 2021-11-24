"""
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로

# 입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
"""


cnt = int(input())  # 루프 반복 횟수
input_list = []  # 입력받은 단어를 저장

for i in range(cnt):
    input_list.append(input())

# 중복제거
set_list = list(set(input_list))

sort_list1 = []
sort_list2 = []
sort_list3 = []

# 길이, 값을 리스트에 추가
for i in set_list:
    sort_list1.append((len(i), i))
    sort_list2.append((i, len(i)))
    sort_list3.append(i)

# 길이 정렬 후, 값 정렬 (오름차순)
result1 = sorted(sort_list1)  # reversed는 내림차순
result2 = sorted(sort_list2)
sort_list3.sort(key=len)
result3 = sort_list3
result4 = sorted(sort_list3)

print(result1)
print(result2)
print(result3)
print(result4)

"""
sorted : 정렬과 함께 반환해서 변수에 바로 저장할 수 있다
sort : sorted 와 같은 처리를 하지만 정렬과 동시에 반환하면 None 을 반환한다.
정렬할때 튜플을 사용해서 여러가지 조건을 한번에 처리할 수 있다.
예를 들어 단어의 크기를 정렬한 다음 알파벳 순으로 정렬하려 할때
단어의 크기 : size, 단어: item
(size, item)라는 튜플을 만들어 정렬처리하면 좋다.
주의 사항은 튜플의 앞자리부터 정렬하기때문에 앞과 뒤가 바뀌면 값이 전혀 다르게 나온다
(size, item)과 (item, size)는 정렬처리했을때 결과 값이 전혀 다름
"""