def remove_element(nums, val):
    while nums.count(val) != 0:
        nums.remove(val)
    k = len(nums)
