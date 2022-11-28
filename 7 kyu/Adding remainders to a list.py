def solve(nums, div):
    return [i + i % div for i in nums]