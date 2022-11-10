#python revision day 12:

#student mark report program:
subjects=["tamil","english","maths","science","social science"]
roll_no=int(input("enter the number of students"))
report={}
for student in range(roll_no):
	marks=[]
	name=input("enter name of roll no %d :"%(student+1))
	for subject in subjects:
		marks.append(int(input("enter mark of %s: "%subject)))
	report[name]=marks
for name,marks in report.items():
	total=sum(marks)
	print("%s's total mark %d"%(name,total))
	if total<125:
		print("%s is failed"%name)
	else:
		print("%s is passed"%name)
		
#---------------------------------------------------------------------------
#BINARY SEARCHING USING PYTHON:

arr=[10,20,30,40,50,60,70] 
x=90
start=0
end=len(arr)-1
while end>=start:
    mid=start+(end-start)//2 
    if x==arr[mid]:
        result=mid
        break
    elif x<arr[mid]:
        end=mid-1
    else:
        start=mid+1
else:
    result=-1
if result!=-1:
    print("element is presented at index",result)
else:
    print("element not presented")
#-----------------------------------------------------------------------	
#BUBBLE SORT USING PYTHON:

lst=[20,10,5,1]
length=len(lst)-1
for count in range(length):
	for i in range(len(lst)-1):		
		if lst[i]>lst[i+1]:
			lst[i],lst[i+1]=lst[i+1],lst[i]
	length-=1
print(lst)
#--------------------------------------------------------------------------
#FUNCTION AND FUNCTION DEFINITION:

#once we write a code into a separate block and then we can call anytime with function name.functions must need () at end of the function name.functions use for code reusability.def keyword use for define a function.return keyword return a value to function.the return statement terminates the execution of a functio and returns control to the calling function. 

def sum(num1,num2): #----->function definition
	return num1+num2
result=sum(5,4) #--------->function calling
print(result)

output:
9
#-----------------------------------------------------------------------------
#PALINDROME PROGRAM:
def palindrome(word):
	if word==word[::-1]:
		return print("word is palindrome")
	else:
		print("not a palindrome word")
	
word=input("enter your word")
palindrome(word)
#-----------------------------------------------------------------------------
#SCOPE OF VARIABLES:local variable,global variable:
#local variables only access within a function.
#we can access  global variables in every function.

#DIFFERENCE BETWEEN PARAMETER AND ARGUMENTS:
#the input when we give to a function calling called parameter.inputs to a function when function definition is called arguments.

def changemoney(money):#---> arguments
	money=2000 #local variable
	print("need to change rs",money)
money=10000    #global variable
print("need to be spend rs",money)
changemoney(money)  #---->parameters
#------------------------------------------------------------------------------
#global keyword:without using global keyword we cannot change a global variable value within function definition.using of global keyword we can change a global variable value.

price=1
def calculate():
	global price
	price+=2
	print(price)
calculate()

output:
3
#S-----------------------------------------------------------------------------
x=8
def loc():
	x="local"
	print("local x value",x)
loc()
print("globl x value",x)

output:
local x value local
globl x value 8
#-----------------------------------------------------------------------------
#DEFAULT ARGUMENT:
#we can a assign a value to argument when function definition and its called default argument.whenever we want to change a default argument value, we can change it in function calling.
def find_discount(price,percentage=10):
	discount=price*(percentage/100) 
	new_price=price-discount
	print(new_price)
find_discount(100)
find_discount(100,25)

output:
90.0
75.0
#------------------------------------------------------------------------------
#KEYWORD ARGUMENTS:we can pass multiple parameter as one argument using * symbol before the argument it's called keyword argument.

def tell_name(*names):
	for name in names:
		print(name)
tell_name("sanjay","naveen","gopal","vinoth")

output:
sanjay
naveen
gopal
vinoth
#-----------------------------------------------------------------------------
#VARIABLE LENGTH ARGUMENTS:we can pass multiple parameter as multiple arguments using * symbol before the argument name it's called variable length argument.

def product_detail(*amount):
	for price in amount:
		print(price)
product_detail(200,100,180,350)

output:
200
100
180
350
#------------------------------------------------------------------------------
# ** symbol as keyword argument(kwargs):whenever we want to pass multiple dict value as argument we use ** before the argument name.
def mrp(selling,buying,**tax):
	print(selling)
	print(buying)
	for key,value in tax.items():
		print(key)
mrp(100,90,sgst=5,cgst=8)

output:
100
90
sgst
cgst
#------------------------------------------------------------------------------
#COMPOSITION IN FUNCTIONS:
#sometimes we give a function as parameter to another function its called composition in function.
name="kumar"
print(len(name)) #---> first a len function execute and then print function execute.
#------------------------------------------------------------------------------
#SOME BUILT IN MATHEMATICAL FUNCTIONS:
print(abs(5.4))     #-->5.4 absolute value
print(ord("a"))     #-->97 ordinal value
print(chr(65))      #-->"A" character value
print(bin(5))       #-->"ob101" binary value
print(min(20,5))    #-->5 for finding minimum value
print(max(20,5))    #-->20 for finding maximum value
print(sum(5,1))     #-->6 for finding addition of values
print(round(3.5))   #-->4 for roundup a value
print(round(3.457,2)) #-->3.46
print(pow(2,2))       #-->4 for finding power value
#---------------------------------------------------------------------------
















	
	


















































	
	
	
	
	
	
	
	
	
	
	
	
	