# chapter06-1
# 파이썬 클래스
# oop, self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해

# 예제1
class Dog(object):
    """
    test
    """
    species = 'firstdog'
    
    # def __init__(self, name):
    #     self.name = name
        
    # def __init__(self, age):
    #     self.age = age

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"개이름: {self.name}")
        print(f"개나이: {self.age}")


if __name__=='__main__':
    # dog0 = Dog()
    # dog1 = Dog(name='개1')
    # dog2 = Dog(age=10)
    dog3 = Dog(name='개3', age=12)
    dog4 = Dog(name='개4', age=13)
    dog10 = Dog(name='개10', age=20)

    # dog0.bark()
    # dog1.bark()
    # dog2.bark()
    dog3.bark()
    dog4.bark()

    print(dog3==dog4, id(dog3), id(dog4))
    
    print('dog3', dog3.__dict__)
    print('dog4', dog4.__dict__)

    # print('dog10.__annotations__', dog10.__annotations__)
    print('dog10.__class__', dog10.__class__)
    print('dog10.__delattr__', dog10.__delattr__)
    print('dog10.__dict__', dog10.__dict__)
    print('dog10.__dir__', dog10.__dir__)
    print('dog10.__doc__', dog10.__doc__)
    print('dog10.__getattribute__', dog10.__getattribute__)
    print('dog10.__dict__', dog10.__dict__)

    print('dog10.__str__', dog10.__str__)
    print('dog10.__eq__', dog10.__eq__)
    print('dog10.__ne__', dog10.__ne__)
    print('dog10.__format__', dog10.__format__)
    print('dog10.__subclasshook__', dog10.__subclasshook__)
    print('dog10.__reduce__', dog10.__reduce__)
    print('dog10.__new__', dog10.__new__)

    print("all: ", all([1,2,3]))
    print("all: ", all([1,3,5]))
    print("all: ", all([1,2,4]))

    print("all: ", all([1,2,4,7]))
    print("all: ", all([1,2,4,8]))
    print("all: ", all([1,2,4,9]))

    print("all: ", all([1,0,4]))