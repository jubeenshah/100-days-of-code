# Enter your code here. Read input from STDIN. Print output to STDOUT
numberOfStamps = int(input())
countrylist = set()
for _ in range(numberOfStamps):
    countrylist.add(input())
print(len(countrylist))
