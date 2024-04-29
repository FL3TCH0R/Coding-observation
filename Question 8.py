def main():
    sum=0
    count=0
    while True:
        n=int(input("Enter a number"))
        m=input("Do you have more numbers(yes or no)?")
        if m=="no":
            break
        count=count+1
        sum=sum+n
    print("Average is",sum/count)
main()
        
