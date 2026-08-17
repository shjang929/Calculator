def divide(a, b): # 두 숫자 a, b를 입력받음
    try:
        return a / b # a를 b로 나눈 값을 반환
    except ZeroDivisionError:
        return "Error: 0으로 나눌 수 없습니다."