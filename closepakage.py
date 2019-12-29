def make_averager():

    nums = []

    def averager(n):
        nums.append(n)
        return sum(nums) / len(nums)
    return averager


averager = make_averager()

print(averager(10))
print(averager(30))
