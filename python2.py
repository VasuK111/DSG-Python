# Python Object Oriented Programming
# method is a function that is associated with a class


class Employee:

  raise_amount = 1.04

  def __init__(self, first, last, pay, ):
       self.first = first
       self.last = last
       self.pay = pay
       self.email = first + '.' + last + '@gmail.com'

  def fullname(self):
      return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
      self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Vasu','Khanna',50000)
emp_2 = Employee('Vansh','Khanna',39000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)

# To access the class variables, we need to access them from the class within or through an instance of that class.

# pass
""" pass statement is used when u don't pass any value 
 to a class/function but don't want any error to return """
# class is a blueprint for creating instances
# defining this init for auto updation for more employees as they add up


#emp_1 = Employee()
#emp_2 = Employee()

#print(emp_1)
#print(emp_2)

#emp_1.first = 'Vasu'
#emp_1.last = 'Khanna'
#emp_1.email = 'Vasu.Khanna@gmail.com'
#emp_1.pay =  50000

#emp_2.first = 'Vansh'
#emp_2.last = 'Khanna'
#emp_2.email = 'Vansh.Khanna@gmail.com'
#emp_2.pay =  39000














