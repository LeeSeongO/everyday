#-*- coding: utf-8 -*-
# 기존의 함수의 같은 경우 def type_hint(b)와 같이 파라미터 b의 값이 숫자인지 문자를 넘겨야 하는지 전혀 알 수 없으며
# 함수의 리턴값이 무엇인지도 알 수 없다. 그렇기 때문에 나중에 프로젝트의 규모가 커지면 가독성을 떨어뜨리게 되기때문에 사용함.
# python version 3.5부터 사용가능

# 다음과 같이 오류도 체크해 볼 수 있다.
# pip install mypy
# mypy main.py


def type_hint(b: int) -> str:
    a = 3
    return str(a)


