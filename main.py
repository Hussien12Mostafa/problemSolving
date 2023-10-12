user_input = input()
user_input=user_input.split()
x=  int( user_input[0])
y=  int( user_input[1])
# print(x,"   ",y)
count=0
while x<=y:
    x*=3
    y*=2
    count+=1
print(count)