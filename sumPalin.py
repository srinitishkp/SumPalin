def rev(a):
    temp=a
    r=0
    rev=0
    while(a>0):
        r=a%10
        rev=rev*10+r
        a=int(a/10)
    return rev
def checkPalin(temp,rev):    
     if(temp==rev):
          return True
     else :
          return False
num=int(input("Enter a 2 or 3  digit number:"))
print("Initially sum is the given number:")
for i in range(5):
     print("Current sum:",num,"Reverse:",rev(num))
     num=num+rev(num)
     if(checkPalin(num,rev(num))):
         break
print("\nFinal sum after loop:",num,"\nFinal reverse after loop:",rev(num))
if(num==rev(num)):
    print("\nPalindrome")
else:
    print("\nNot a palindrome")