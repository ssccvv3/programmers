# 1인분 12,000
# 음료수 2,000원
# 10인분 120,000원
# 10인분 마다 음료수 1개 / 

def solution(n, k):
    food = n * 12000
    service = int(n // 10) * 2000
    drink = k * 2000
    answer = food + drink - int(service)
    return answer

