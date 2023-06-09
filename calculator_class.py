# Calculator class
from ui_class import UI
class Calculator:
    # initializes variables
    def __init__(self, firstN, secondN, result) -> None:
        self.number1=firstN 
        self.number2=secondN
        self.results=result
    
    # registers input    
    def inputNum1(self, firstN):
        self.number1=float(firstN)
        
    # registers input   
    def inputNum2(self, secondN):
        self.number2=float(secondN)
    
    # adds inputs
    def addition(self):
        result=self.number1+self.number2
        self.results=float(result)
    
    # subtracts inputs
    def subtraction(self):
        result=self.number1-self.number2
        self.results=float(result)
    
    # multiplies inputs
    def multiplication(self):
        result=self.number1*self.number2
        self.results=float(result)
    
    # divides inputs
    def division(self):
        result=self.number1/self.number2
        self.results=float(result)

class ScientificCalculator(Calculator):
    # initializes variables
    def __init__(self, firstN, secondN, result):
        super().__init__(firstN, secondN, result)

    # exponentiation
    def exponentiation(self):
        result = self.number1 ** self.number2
        self.results = float(result)

    # square root
    def squareRoot(self):
        result = self.number1 ** 0.5
        self.results = float(result)
        
    # cube root
    def cubeRoot(self):
        result = self.number1 ** (1/3)
        self.results = float(result)
# HONTIVEROS, JEROME ANDREI O.
# BSCPE 1-5