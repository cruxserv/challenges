def dirReduc(a):
    dict = {"NORTH": "SOUTH", "EAST": "WEST", "SOUTH": "NORTH", "WEST": "EAST"}
    stack = []

    for d in a:
        if d in dict:
            if stack and stack[-1] == dict[d]:
                stack.pop()
            else:
                stack.append(d)

    return stack
