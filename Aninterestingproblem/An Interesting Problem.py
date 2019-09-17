#An interesting problem

#Part 1

p=(1000)

r=(0.05)

n=(12)

t = int(input("How many years will you be saving for?"))

print("You will have ", p*(1+r/n)**(n*t), "in" ,t, "years" )

#Part 2

a=int(input("How much money do you want to invest?"))

b=int(input("How much interest (in decimals) is the bank giving you?"))

c=(12)

d = int(input("How many years will you be saving for?"))

print("You will have ", a*(1+b/c)**(c*d), "in" ,d, "years" )

print("You will have ", a*(1+b/c)**(c*5), "in 5 years" )

print("You will have ", a*(1+b/c)**(c*10), "in 10 years" )

print("You will have ", a*(1+b/c)**(c*20), "in 20 years" )
