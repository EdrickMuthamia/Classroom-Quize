def find_missing_number(nums):
    n = len(nums)
    for i in range(n + 1):
        if i not in nums:
            return i


print(find_missing_number([3, 0, 1]))  