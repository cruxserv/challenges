def divisors(integer):
    ans = []
    for num in range(2, integer):
        if integer % num == 0:
            ans.append(num)
    if ans == []:
        return f"{integer} is prime"
    else:
        return ans
    # return ans if ans else f"{integer} is prime"
