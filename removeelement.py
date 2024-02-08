def remove_element(nums, val):
    k = 0  # Initialize count of elements not equal to val
   
    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is not equal to val
        if nums[i] != val:
            # Move the element to the front of the array
            nums[k] = nums[i]
            # Increment count of elements not equal to val
            k += 1
   
    return k