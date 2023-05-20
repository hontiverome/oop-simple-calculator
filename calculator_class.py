# Calculator class
from ui_class import UI
class Calculator:
    def __init__(self, firstN, secondN, result) -> None:
        self.number1=firstN 
        self.number2=secondN
        self.results=result
        
    def inputNum1(self, firstN):
        self.number1=float(firstN)

    def inputNum2(self, secondN):
        self.number2=float(secondN)
    
    def addition(self):
        result=self.number1+self.number2
        self.results=float(result)
    
    def subtraction(self):
        result=self.number1-self.number2
        self.results=float(result)
    
    def multiplication(self):
        result=self.number1*self.number2
        self.results=float(result)
    
    def division(self):
        result=self.number1/self.number2
        self.results=float(result)
        
# HONTIVEROS, JEROME ANDREI O.
# BSCPE 1-5