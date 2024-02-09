def majorityelement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate


# def majorityelement(nums):
#     return sorted(nums)[len(nums) // 2]
