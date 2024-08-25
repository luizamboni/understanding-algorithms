def has_robot_returned(moves: str):
    x = 0
    y = 0

    for m in moves:
        if m == "U":
            y+= 1
        if m == "D":
            y-= 1
        if m == "R":
            x+=1
        if m == "L":
            x-= 1

    if x == 0 and y == 0:
        return True

    return False

moves = "UDRL"
print(
    has_robot_returned(moves)
)