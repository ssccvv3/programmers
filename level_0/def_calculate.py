def solution(money):
    cups = int(money) // 5500
    left = int(money) % 5500
    result = [cups, left]
    return result

coffee = solution(15000)
print(coffee)