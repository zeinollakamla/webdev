def make_bricks(small, big, goal):
    if goal >= 5 * big:
        a = goal - (5 * big)
    else:
        a = goal % 5
        
    return small >= a