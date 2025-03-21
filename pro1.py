'''marks = 20 
result = ""
if marks < 30:
   result = "Failed"
elif marks > 75:
   result = "Passed with distinction"
else:
   result = "Passed"

print(result)'''



"""num=int(input("enter then umber"))
if num%2==0:
    print("it  is even numbre")
else:
    print("it it odd number")"""

"""
for i in range(11):
    print("hello sona rag kore na")"""



"""name=input("enter the name")
res=name.lower()
print(res)"""



def sum(a, b):
    res = a + b
    return res

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = sum(num1, num2)
print("The sum is:", result)
