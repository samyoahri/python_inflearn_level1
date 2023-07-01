import time
# chapter02-1
# 파이썬 완전 기
# Print 사용법

# 기본 출력
print("=====기본출력=====")
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")
print()

# separator 옵션
print("=====separator옵션=====")
print('P', 'Y', 'T', 'H', 'O', 'N')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('python', 'google.com', sep='@')
print('010', '7777', '1234', sep='-')
print("apple1", "apple2", "apple3", sep="!!!", end="\n\n\n")
# help(print)

# end 옵션
print("Welcome to", end='')
print("IT NEWS", end='!')
print()

# file 옵션
import sys
print("Learn python", file=sys.stdout)
with open('test.txt', 'w') as f:
    print("Hello txt!", file=f)

#format 사용(d, s, f)

print('%s %s' %('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
one = "one"; two = "two"
print(f"{one} {two}")

# %s
print("%10s" %("nice"))
print("{:10}".format("nice"))
print("{:<10}".format("nice"))
print("{:>10}".format("nice"))
print()

print("%-10s" %("nice"))
print("{:<10}".format("nice"))

print("{:_<10s}".format("nice"))
print("{:^10s}".format("nice"))

print("%.5s"%("pythonstudy"))
print('{:.5}'.format('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))


# print()
# for i in range(10):
#     print(i, end = ' ')
#     time.sleep(1)
# print()
# for i in range(10):
#     print(i, end = ' ', flush= True)
#     time.sleep(2)
# print()
