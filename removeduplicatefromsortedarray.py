def removeDuplicates(nums):
    if not nums:
        return 0

    # Initialize the counter and the second pointer.
    i = 0
    
    for j in range(1, len(nums)):
        # If the current element is not equal to the previous element,
        # increment the counter and update the nums array.
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    # The length of the unique elements is i + 1
    return i + 1
