# print("Day 09 starts here !!")
# print('Practicing Python')
# i=1
# o= int(input('Enter Number : '))
# u= int(input("Enter Length : "))
# while i <=u :
#         print(o,'* ',i,'=',i*o )
#         i+=1
# # Another Approach :
# # '''Generalise  Approach '''
# p= int(input('Enter Number : '))
# y= int(input("Enter Length : "))
# # for i in range(1,y) :
# #     print(2,'*',i,'=',2*i)
# x=1
# while x in range(1,y,1):
#         print(p,'*',x,'=',p*x)
#         x+=1

# checking the Palindrome  :
'''
def palindrome(x):
        if x[0::] == x[::-1]:
                print(f"The string ' {x} ': is a Palindrome !!")
        else:
                print("its not")
y=input("Enter the string :")
palindrome(y)
'''
s=input("Enter the sentance : ")
# print(s.count(s))
# print(''.join(s.split()))
x=s.split()
print('Number of words are : ')
print(len(x))
# b="ahmad"
# print(b[:-1])
# print(b[0::])