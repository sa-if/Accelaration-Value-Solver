''' Make "a" value solver
It's free and open source '''

v = float(input("put the value of v (In m/s) "))
u = float(input("Put the value of u (In m/s) "))
t = float(input("put the value of t (In second) "))

answer = (v-u)/t



print(answer)

if answer > 0:
    print("It is positive")

elif answer == 0:
    print("There is no accelaration")

else:
    print("It is negative")



