import math

def square(side):
    area = side * side
    return math.ceil(area) if not isinstance(side, int) else area

test_cases = [5, 3.2, 4.6, 7]

print("Сторона -> Площадь:")
for side in test_cases:
    print(f"{side} -> {square(side)}")