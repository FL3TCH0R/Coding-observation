def main():
    speed=int(input("Enter the speed"))
    limit=int(input("enter the limit"))
    if 90>speed>=limit:
        over_lim=speed-limit
        Fine=50+(5*over_lim)
        print("Your fine is",Fine)
    elif speed>90:
        over_lim=speed-limit
        Fine2=50+(5*over_lim)+200
        print("your fine is",Fine2)
    else:
        print("Your speed is legal")
main()
