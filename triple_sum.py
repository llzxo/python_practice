def sum(num1 = 0, num2 = 0, num3 = 0):
    return num1 + num2 + num3

def avg(num1 = 0, num2 = 0, num3 = 0):
    return sum(num1,num2,num3)/3.0


a = input("input first number:")
b = input("input second number:")
c = input("input third number:")
print(avg(a,b,c))
