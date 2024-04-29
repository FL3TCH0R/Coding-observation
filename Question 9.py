def main():
    sum=0
    count=0
    while True:
        n=int(input("Enter a number"))
        if n==999:
            break
        sum=sum+n
        count=count+1
    print("Average is",sum/count)
main()
