from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def calculator(): #계산기 전체 프로그램을 실행하는 파이썬 함수
    a = float(input("첫 번째 숫자: ")) # 3.14 등 실수 입력 가능
    b = float(input("두 번째 숫자: "))
    op = input("연산자(+, -, *, /): ")

    if op == '+':
        print(add(a, b))
    elif op == '-':
        print(subtract(a, b))
    elif op == '*':
        print(multiply(a, b))
    elif op == '/':
        print(divide(a, b))
    else:
        print("잘못된 연산자입니다.")

if __name__ == "__main__":
    calculator()