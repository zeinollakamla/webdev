def make_chocolate(small, big, goal):
    if goal >= 5 * big:
        a = goal - 5 * big
    else:
        a = goal % 5
        
    if a <= small:
        return a
        
    return -1