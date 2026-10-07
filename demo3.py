#Method overloading
class Summation :
    def sum(self,*args):
        ans = 0
        for i in args:
            ans += i
        return ans

summation1 = Summation()
print(summation1.sum(2,45,67,98,99))

#Method overriding
class Father:
    def __init__(self):
        print('father constructor')

    def say_hello(self):
        print('helllo from father')

class Child(Father):
    def __init__(self):
        print('child construtor')

    def say_hello(self,name):
        print('hello from child',name)

child = Child()
child.say_hello('deepz')

father = Father()
print(father.say_hello())
