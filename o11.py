
class base(object):
    d1=1000
    __d2= 200
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __function_two(self,c):
        self.c = c
        return c
    def function_one(self):
        d = 100
        print(self.a)
        print(self.b)
        print(self.__function_two(100))
        return
    
class derived(base):
    c1=200
    def function_three(self):
        print("function three ")



b1 = base(100,200)
print(b1.d1)
b1.function_one()


    
