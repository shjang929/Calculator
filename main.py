from add import add # add.py의 add 함수를 가져옴
from subtract import subtract # subtract.py의 subtract 함수를 가져옴
from multiply import multiply # multiply.py의 multiply 함수를 가져옴
from divide import divide # divide.py의 divide 함수를 가져옴

def calculator(): # 계산기 전체 프로그램을 실행하는 파이썬 함수
    a = float(input("첫 번째 숫자: ")) # 3.14 등 실수 입력 가능
    b = float(input("두 번째 숫자: "))
    op = input("연산자(+, -, *, /): ") # 연산자 입력

    if op == '+':
        print(add(a, b)) # 덧셈
    elif op == '-':
        print(subtract(a, b)) # 뺄셈
    elif op == '*':
        print(multiply(a, b)) # 곱셈
    elif op == '/':
        print(divide(a, b)) # 나눗셈
    else:
        print("잘못된 연산자입니다.") # 그 외 오류 메시지

if __name__ == "__main__": # 이 파일을 직접 실행했을 때만 아래 코드 실행 (엔트리 포인트)
    calculator() # 계산기 프로그램 실행 시작