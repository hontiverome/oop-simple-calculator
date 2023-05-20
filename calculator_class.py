# Calculator class
from ui_class import UI
class Calculator:
    def __init__(self, firstN, secondN) -> None:
        self.number1=firstN 
        self.number2=secondN
    
    def inputNum1(self, firstN):
        self.number1=float(firstN)

    def inputNum2(self, secondN):
        self.number2-float(secondN)
    
    def addition(self):
        result=self.number1+self.number2
        return result
    
    def subtraction(self):
        result=self.number1-self.number2
        return result
    
    def multiplication(self):
        result=self.number1*self.number2
        return result
    
    def division(self):
        result=self.number1/self.number2
        return result