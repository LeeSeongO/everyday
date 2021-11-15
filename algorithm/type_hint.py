"""
def type_hint(b):
    a = b
    return str(a)

파라미터 b는 integer, 반환타입은 string
변수 a는 integer로 변환

타입힌트형식으로 작성하면 mypy기능 사용할 수 있다.
# pip install mypy
# mypy main.py
"""


def type_hint(b: int) -> str:
    a: int = b
    return str(a)
