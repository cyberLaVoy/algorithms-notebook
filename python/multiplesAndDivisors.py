def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# nums: a list of integers
# Output: the gcd of all values in nums
def gcdList(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result = gcd(result, nums[i])
    return result

def lcm(a, b):
    return a*b//gcd(a, b)

# nums: a list of integers
# Output: the lcm of all values in nums
def lcmList(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result = lcm(result, nums[i])
    return result
