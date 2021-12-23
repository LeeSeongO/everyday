all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


# 해쉬 테이블은 시간 극대화 시킬 수 있는대신 공간을 대신 사용하는 자료구조이다.

def get_absent_student(all_array, present_array):
    student_dict = {}
    for key in all_array:    # O(N)
        student_dict[key] = True  # 공간복잡도도 O(N)

    for key in present_array:
        del student_dict[key]

    for key in student_dict.keys():
        return key

    return


print(get_absent_student(all_students, present_students))