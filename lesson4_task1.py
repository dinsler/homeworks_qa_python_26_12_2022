# Write code that removes from the list all numbers that are less than 21 and greater than 74.
nums = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]
print(id(nums))

for i in range(len(nums) - 1, -1, -1):
    if not 21 < nums[i] < 74:
        nums.remove(nums[i])
print(f'Modified list is {nums}')
