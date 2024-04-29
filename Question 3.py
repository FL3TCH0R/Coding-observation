import math
def main():
    try:
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        c=int(input("enter a number"))
        disc=(b**2)-4*a*c
        root1=(-b+math.sqrt(disc))/(2*a)
        root2=(-b-math.sqrt(disc))/(2*a)
        print("the roots are",root1,root2)
    except ValueError:
        print("You cannot compute the square root of a negative number")
main()
