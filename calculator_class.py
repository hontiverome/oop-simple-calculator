# Calculator class
from ui_class import UI
class Calculator:
    def __init__(self, firstN, secondN) -> None:
        self.number1=firstN 
        self.number2=secondN
    
    def inputNum(self, firstN, secondN):
        self.number1=float(firstN)
        self.number2=float(secondN)
        