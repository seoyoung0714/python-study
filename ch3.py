#연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) #제곱
print(5%3) #나머지
print(10%3) 
print(5//3) #몫

print(10 > 3)
print(4 >=7)
print(10 < 3)
print(5 <= 5)

print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)

print(1 != 3)
print(not (1 != 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 > 5))

print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))

print(5 > 4 > 3)
print(5 > 4 > 7)

#간단한 수식
print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)

number %= 5
print(number)

#숫자처리함수
print(abs(-5))  #절댓값
print(pow(4, 2))  #제곱
print(max(5, 12))
print(min(5, 12))
print(round(3.14))  #반올림
print(round(4.99))

from math import *
print(floor(4.99))  #내림, 4
print(ceil(3.14))  #올림, 4
print(sqrt(16))  #제곱근, 4

#랜덤함수
from random import *
print(random())  #0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)  #0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  #0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)  #1 ~ 10 이하의 임의의 값 생성

print(int(random() * 45) + 1)  #1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46))  #1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45))  #1 ~ 45 이하의 임의의 값 생성