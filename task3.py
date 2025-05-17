import math
from task2 import logger

def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return b*b - 4*a*c

@logger("log_task3.log")
def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    d = discriminant(a,b,c)
    if d < 0:
        print("корней нет")
    elif d ==0:
        print(-b / (2*a))
    else:
        print((-b + math.sqrt(d)) / (2 * a), end=' ')
        print((-b - math.sqrt(d)) / (2*a))

if __name__ == '__main__':
    solution(1, 8, 15) 
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)