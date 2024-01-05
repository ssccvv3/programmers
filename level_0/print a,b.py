a, b = map(int, input("두 정수를 공백으로 구분하여 입력하세요: ").split())

# 제한사항 확인
if -100000 <= a <= 100000 and -100000 <= b <= 100000:
    print(f"a = {a}")
    print(f"b = {b}")
else:
    print("입력된 숫자가 제한 범위를 벗어났습니다.")