class Calculator():
    """Performs the four basic mathematical operations

    Methods:
     add(number, number)
     subtract(number, number)
     multiply(number, number)
     divide(number,number)
    """

    def add(self, firstOperand, secondOperand):
      return firstOperand + secondOperand

    def subtract(self, firstOperand, secondOperand):
      return firstOperand - secondOperand

    def multiply(self, firstOperand, secondOperand):
      return round(firstOperand * secondOperand, 3)

    def divide(self, firstOperand, secondOperand):
      return round(firstOperand / secondOperand, 3)