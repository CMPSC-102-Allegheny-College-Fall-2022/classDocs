# Build and return a list
# ref: https://wiki.python.org/moin/Generators

def listBuilder(n):
    num = 0; nums = []
    while num < n:
        nums.append(num)
        num += 1
    return nums
#end of listBuilder()
sum_of_first_n = sum(listBuilder(1000000))
print("\t The sum of first n :",sum_of_first_n)
