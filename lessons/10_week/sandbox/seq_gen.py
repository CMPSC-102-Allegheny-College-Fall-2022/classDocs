# Using the generator pattern (an iterable)
# ref: https://wiki.python.org/moin/Generators

class listBuilder(object):
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()

sum_of_first_n = sum(listBuilder(1000000))
print("\t The sum of first n :", sum_of_first_n)
