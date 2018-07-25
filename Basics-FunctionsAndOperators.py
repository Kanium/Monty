# Comment
'''
Multi
Line
Comments
'''

#Variables
helloWorld = "Hello World"
exampleVar = print("whoa")
x,y = (3,5)

#Print formatting and conversions
print("===STRINGS===")
print("Hello World")
print('Hello World with single-quotes')
print("%s %s %s"%("python","is","fun"))
print("%s with variable" %(helloWorld))
print('we\'re escaping single quotes because we\'re using single quotes for text And print')
print('Hi','there with a comma')
print('Hi', str(5),'with comma and string conversion')

#Math
print("===MATH===")
print(1+3)
print(3-1)
print(4*4)
print(5/2)
print(4**4)
print(x)
print(y)
print(x+y)

#Loops
print("===LOOPS===")
condition = 1

while condition < 5:
    print(condition)
    condition += 1

exampleList = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]

#indentation is important (and mandatory!)
for eachNumber in exampleList:
    print(eachNumber)

for x in range(1,4):
    print(x)

#Functions (note the indentation)
def example():
    print('basic function')
    z = 3+9
    print(z)

example()

def simple_addition(num1,num2):
    answer = num1+num2
    print('num1 is', num1)
    print('answer is', answer)

simple_addition(10,42)