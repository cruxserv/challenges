def majorityElement(nums):
    count, candidate = 0, nums[0]
    for num in nums:
        if num == candidate:
            count += 1
        elif count == 0:
            candidate, count = num, 1
        else:
            count -= 1
    return candidate



# def majorityelement(nums):
#     return sorted(nums)[len(nums) // 2]
