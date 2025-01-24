import random

class MathOp:
    def __init__(self, num1, num2):
        self.__num1 = num1  
        self.__num2 = num2  

    def op(self):
        
        op = random.choice(['+', '-', '*', '/'])
        if op == '+':
            return self.__num1 + self.__num2
        elif op == '-':
            return self.__num1 - self.__num2
        elif op == '*':
            return self.__num1 * self.__num2
        elif op == '/':
            return self.__num1 / self.__num2
            

    def __str__(self):
        
        return str(self.op())

ope = MathOp(10, 5)
print(ope) 