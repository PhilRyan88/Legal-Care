# # for i in range (1,4):  
# #     for j in range(1,i+1):
# #       print("*",end=" ")  
# #     print()

                          
                          
                          
                          
                          
# # print("successully printed the pattern")

# # # *
# # # * *
# # # * * *
# # # * * * *

# s= []
# list = ["ELement 1","Apple","Orange"]
# s.extend(list)
# a=s.pop(1)
# print(a,s)



# a= input("enter word")
# count=0
# for i in a:
#     count = count+1
# print("number of alphabets : ",count)


# w= "munch"

# for i in w:
#     print(i,end='-')

# ? hcnum 

# w= "munch"
# rev=""
# for i in w:
#     rev = i + rev         # rev = m
# print("reverse is :",rev) # rev = u + m = um
#                           # rev = n+ um
#                           # rev = c + num
#                           # rev = h + cnum rev = hcnum
#                           #  



# num = input("enter number") # 10
# num2 = input("enter number") # 20

# print(num+num2)

# to add elements to a list 
# l=[]
# s=[]
# for i in range(3):
#     e=input("enter element") 
#     l.append(e)
# print("list is ",l)
# s.extend(l)
# print("stack",s)
# for i in range(len(s)):
#     s.pop()
#     if s==[]:
#         print("stack is empty")
# print("current stack :",s)
# answer = input("Do you want to add any element to the stack?")

# def automate():
#     l=[]
#     s=[]
#     for i in range(limit):
#         e=input("enter element") 
#         l.append(e)
#     s.extend(l)
#     print("Your new stack is :",s)

# if answer == "yes":
#     limit = int(input("Enter the number of elements : "))
#     automate()
# else:
#     print("Since your answer is No , your program ended here")


# stack = []
# def Push(arr):
#     for i in arr:
#         if i % 5 ==0:
#             stack.append(i)
#         size = len(stack)
#     if size > 0:
#          for i in range(size):
#                 print("current stack",stack[i])
#     else:
#         print("stack is empty")
        
# arr = [20,6,5,77,8]     
# Push(arr)
        
# for i in range(1,5):
#     print("#"*i)  # 
# def no(lis):
#     stk=[]
#     for i in lis:
#         stk.append(i)
#     print("currently stack is :",stk)
#     while True:
#         if stk == []:
#             print(" after deletion the stack is :",stk)
#             break
#         else:
#             stk.pop()
# lis=["john",198,"ray"]
# no(lis)

# stk =[]
# def check(r):
#     stk.extend(r)
#     print("stack is",stk)
    
#     if stk==[]:
#         print("empty")
#     else:
#         s=len(stk)
#         for i in range (s):
#             stk.pop()
#         print("now stack is :",stk)

# r=[1,2,3,4,5,6]
# check(r)












# stk =[]
# def vowels(wd):
#     print("initial stk",stk)
#     for i in wd:
#         if i  in 'aeiouAEIOU':
#            stk.extend(i)
#     print("current stack with vowels :",stk)
# wd ="computer"
# vowels(wd)

# # str = "whiteboard"
# # variable = str[-1::-1]
# # print(variable)

# #  input a string and check whether the string is palindrome or not 

# # str = input("enter string : ")
# # a = str[-1::-1]
# # if str == a:
# #     print("palindrome, ",str)
# # else:
# #     print("not palindrome", a)

# import math
# print(math.sqrt(225))
# print(math.pi)
# print(math.e **1)


#! accept 5 numbers from the user and store it in a list and display it like this [1,2,3,4,5]?

# l = eval(input("enter numbers"))
# list =  list(l)
# print(list)
# new = list(l)
# print(new," this is the required list")



# l= list()
# stop = int(input("enter the number of elements")) # 5 0<5 , i=1, i<5 ,1<5 , 2<5?,3<5?,4<5?,5<5?
# for i in range(0,stop):
#     element = int(input("enter the element"))  # 10 , 20, 30,40,50
#     l.append(element) #to insert value into the empty list
# print("the list is : ",l)

#    # ?  l[10,20,30,40,50]
