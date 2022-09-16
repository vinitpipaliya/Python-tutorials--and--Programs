def ispalindrome(number):
    return number==number[::-1]

print("------------------------")
number=input("Enter a number: ")
print("------------------------")
if number.isnumeric():
    ans = ispalindrome(number)
    if ans:
        print("Given number is Palindrome")
    else:
        print("Given number is not Palindrom")
print("------------------------")