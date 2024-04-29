import math
def main():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=int(input("enter a number"))
    disc=(b**2)-4*a*c
    if disc<0:
        print("there are no real roots")
    else:
        root1=(-b+math.sqrt(disc))/(2*a)
        root2=(-b-math.sqrt(disc))/(2*a)
        print("the roots are",root1,root2)
main()
    
