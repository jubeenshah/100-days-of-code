# Enter your code here. Read input from STDIN. Print output to STDOUT

def isPrime(n):
    if (n <= 1) : 
        return "Not prime"
    if (n <= 3) : 
        return "Prime"
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return "Not prime"
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return "Not prime"
        i = i + 6
  
    return "Prime"

for _ in range(int(input())):
    x = int(input())
    print(isPrime(x))