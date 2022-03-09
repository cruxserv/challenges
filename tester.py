dict = {"NORTH": "SOUTH", "EAST": "WEST", "SOUTH": "NORTH", "WEST": "EAST"}
stack = []
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
for d in a:
    if d in dict:
        if stack and stack[-1] == dict[d]:
            stack.pop()
            print(stack)
        else:
            stack.append(d)
            print(stack)
# print(stack)
