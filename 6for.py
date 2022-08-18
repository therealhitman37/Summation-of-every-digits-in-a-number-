#Summation of every digits in a number 

n = int(input("Enter a number: "))

def sums(n):
    x = sum(int(digit)for digit in str(n))
    if n < 10:
        return n
    else:
        return x

print(sums(n))