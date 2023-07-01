#chapter 02-2
#파이썬 완전기초
#파이썬 변수

# 기본 선언
n = 700
print(n)
print(type(n))
print()
# 동시 선언
x = y = z = 700
print(x, y, z)
print()
#선언
var = 75
#재선언
var = "Change Value"
#출력
print(var)
print(type(var))
print()

# object references
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 에2)
n = 777
print(n, type(n))

# 에 3)
m = n
print(m, n)
print(type(m), type(n))
print()

# id 확인: 객체의 고유값 확인
m = 800
n = 655
print(id(m))
print(id(n))
print(id(m)==id(n))
print()

# 같은 오브젝트 참조
m = 800; n = 800
print(id(m))
print(id(n))
print(id(m)==id(n))

t = 100
print(t)
t = 105.4
print(t)