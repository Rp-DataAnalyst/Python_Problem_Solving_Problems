class Calculator:
      def addition(self,a,b):
            print(a+b)
      def subtraction(self,a,b):
            print(a-b)
      def division(self,a,b):
            if b!=0:
                  print(a/b)
            else:
                  print('Division by zero is not possible')
      def floor_division(self,a,b):
            if b!=0:
                  print(a//b)
            else:
                  print('Floor division by zero is not possible')
      def remainder(self,a,b):
            if b!=0:
                  print(a%b)
            else:
                  print('Mod division by zero is not possible')
      def multiply(self,a,b):
            print(a*b)
      def exponential(self,a,b):
            print(a**b)
      def display(self):
            print('Model_Number' ,self.Model_no)
            print('Company', self.Company)
            print('Color',self.color)
            print('discount',self.discount)

      
#Creating Objects:
cal1=Calculator()
cal2=Calculator()
print(" Using Calculator class methods with cal1 object")
cal1.addition(5,6)
cal1.subtraction(5,6)
cal1.division(5,6)
cal1.multiply(5,6)
cal1.exponential(5,6)
cal1.remainder(5,6)
cal1.floor_division(5,6)
cal1.Model_no='Casio xyz'
cal1.Company='Casio'
cal1.color='Brown'
cal1.discount=0
cal1.display()
print('\n using calculator class with cal2 object ')
cal2.addition(3,5)
cal2.subtraction(3,5)
cal2.multiply(3,5)
cal2.division(3,5)
cal2.floor_division(3,5)
cal2.remainder(3,5)
cal2.Model_no='Casio abc'
cal2.Company='Casio'
cal2.color='Green'
cal2.discount='20%'
cal2.display()



