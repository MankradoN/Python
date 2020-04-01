a="Naomi"
                #Exercise 1
#print(a[1]) 
#print ("Hello", a)

                #Exercise 2
#firstName=input("What is your first name? ")
#secondName=input("What is your surname? ")
#print("Hello",firstName,secondName)


                #Exercise 3
#number1 = float(input('pick a number: '))
#number2= float(input('pick a decimal: '))
#answer = number1 + number2
#print(number1, ' + ',number2,' = ', answer)


               #Exercise 4               
#num1 =float(input("Please enter another decimal: "))
#answer2=num1 ** num2
#print(num1,'to the power of ',num2 , 'is',answer2)


               #Exercise 5
#numA=float(input('Input final number: '))
#numB=float(input("And another decimal please: "))
#numC=numA%numB
#print(numA,' modulo ',numB,' is ',numC)

"""long=float(input('what is the lenght of the longest side of the rectangle? '))
short=float(input('what is the lenght of the shortest side of the rectangle?'))
def area(long,short):
    area=long*short
    print('The area of the rectangle is', area)

def perimeter(long,short):
    perimeter_of_rectangle=(2*long)+(2*short)
    print('The perimeter of the rectangle is ',perimeter_of_rectangle)
area(long,short)
perimeter(long,short)

num= ( 92**8)/1998
statement='This output of `${num} is much simpler than the calculation'
print(statement)
c=input('Whats your name? ')
a='Good '
b='day '
print(a +b +c)


                #Exercise 7

num1=int(input("Give me a number. "))
num2=float(input("Give me a decimal. "))
integer=int(num1)
decimal=float(num2)
rounded_decimal=round(num2)
print ('Your integer is ',integer,'.Your decimal is ',decimal,'.Your rounded number is ',rounded_decimal)


a=input("Give me a number: )
b=input("Give me a number: )
ans=float(a)*float(b)
print("The answer as a decimal is",float(ans))
print("The answer as a decimal is",int(ans))


                        #Method 1
a= input("Give me 3 animals")
b= input()
c= input()

ans=[a,b,c]
ans.sort()
#print(list(ans))

for a in ans:
    print (a)


dictionary={ "Child1":{"name":"Naomi","age":21,"ethnicity":"Ghanaian"},\
   "Child2":{"name":"Solomon","age":23,"ethnicity":"Ghanaian"},\
   "Child3":{"name":"Gloria","age":20,"ethnicity":"Ghanaian"}
}
print(dictionary["Child3"])

a= "Hello world"
"".join(a)
print(a)
"""

Yellow_pages={'1':{"Name1","number"},\
              '2':{"Name2","number"},\
              '3':{"Name3","number"},\
              '4':{"Name4","number"},\
              '5':{"Name5","number"},\
              '6':{"Name6","number"},\
              '7':{"Name7","number"},\
              '8':{"Name8","number"},\
              '9':{"Name9","number"},\
              '10':{"Name10","number"}
              }

# A=Yellow_pages.get('1'),Yellow_pages.get('3'),Yellow_pages.get('5'),Yellow_pages.get('7'),Yellow_pages.get('9'))
# B=Yellow_pages.get('10'),Yellow_pages.get('9'),Yellow_pages.get('8'),Yellow_pages.get('7'),Yellow_pages.get('6'),Yellow_pages.get('5'))

                            
A=list(Yellow_pages.values())
x=0
C=[]
'''
# Function below iterates through only one -CORRECT
for a in A:
    if x % 2 == 0:
        C.append(A[x])
        x +=1

D= A[:6]

print (C)
print (D)
'''
new_YP=[]
new1_YP=[]
P=",".join(map(str,Yellow_pages))])
p.replace("'"," ")
print(p)
'''for x,y in Yellow_pages.items():
    n =[",".join(map( str ,Yellow_pages.keys()))]
    if n % 2 == 0:
      new_YP.append(Yellow_pages.values())
print(new_YP)    
   '''           
