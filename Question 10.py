def syr(x):
    if x%2==0:
        syrX=x/2
    else:
        syrX=3*x+1
    return syrX
def main():
    x=int(input("Enter a number"))
    print(x)
    while x>1:
        syrX=syr(x)
        x=syrX
        print(syrX)
main()
