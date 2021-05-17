# https://blog.csdn.net/zcx1203/article/details/89187495
class Person:
    print("Enter the Dog Class")

    def __init__(self, name, age, gender):
        """

        :rtype: object
        """
        self.name = name
        self.age = age
        self.gender = gender
        print(self)

    def eat(self):
        print('%s正在吃饭...'%(self.name))


K = Person('Kitty', 12, '女')

print(K.name)
K.eat()
