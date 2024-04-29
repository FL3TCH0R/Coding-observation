def main():
    x,y,z=eval(input("Enter numbers"))
    if x>y:
        if x>z:
            print("x is the maximum")  
    elif y>x:
        if y>z:
            print("y is the maximum")
    elif z>x:
        if z>y:
            print("z is the maximum")
main()
