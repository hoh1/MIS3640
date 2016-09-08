#Exercise 2_1
print((60*42)+42)

#Exercise 2_2
print(10/1.61)

#Exercise 2_3_a
print(((60*42)+42)/(10/1.61))

#Exercise 2_3_b
print((10/1.61)/(((60*42)+42)/3600))

#In Class Acitivity 2
#Exercise 1_1
r=5
π=3.14159
v=((4/3)*π*(r**3))
print(v)
#Exercise 1_2
Q=60
Price=24.95
DiscountPrice=Price*0.6
FirstShipping=3
AdditionalShipping=0.75
TotalCost=FirstShipping+((Q-1)*AdditionalShipping)+DiscountPrice
print(TotalCost) 
#Exercise 1_3
PaceA=8+(15/60)
PaceB=7+(12/60)
Time=PaceA+(3*PaceB)+PaceA
hour=6+1
minute=(52+Time)-60
message= 'You will get home for breakfast by %d : %d' %(hour, minute)
print(message)
#Exercise 1_4
message ='What is your first grade?'
print(message)
Grade1 = int(input())
message = 'What is your second grade?'
print(message)
Grade2 = int(input())
change = ((Grade2-Grade1)/Grade1)*100
message = 'Your grade has increased by %.1f %%' % change
print(message)

input()