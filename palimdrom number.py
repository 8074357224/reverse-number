def reverse(n):
    out=0
    a=n
    while n>0:
        rem=n%10
        out=out*10+rem
        n=n//10
    if a==out:
        return("palindromic number")
    else:
        return("not a palindromic")
n=int(input("enter the number:"))
print(reverse(n))