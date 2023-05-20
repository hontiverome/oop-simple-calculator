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
        sum=self.number1+self.number2
        return sum
    
    def subtraction(self):
        difference=self.number1-self.number2
        return difference
    
    def multiplication(self):
        product=self.number1*self.number2
        return product
    
    def division(self):
        quotient=self.number1/self.number2
        return quotient