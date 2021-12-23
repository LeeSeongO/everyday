input = "hello my name is sparta"


def find_max_occurred_alphabet(string):

    alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ,'k', 'n', 'm',
                      'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    max_occurrence = 0  # 순차적으로 이 알파벳이 몇번 발생했는지 체크하기 위한 변수
    max_alphabet = alphabet_array[0]  # max_occurrence를 이용해 제일 많이 발생한 경우 그 반문의 알파벳을 저장하는 변수


    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1

                if occurrence > max_occurrence:
                    max_occurrence = occurrence
                    max_alphabet = alphabet

        return alphabet



result = find_max_occurred_alphabet(input)
print(result)