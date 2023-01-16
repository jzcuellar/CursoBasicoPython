def is_valid_walk(walk):
    n_s = 0
    w_e = 0
    for i in walk:
        if i == 'n':
            n_s += 1
        elif i == 's':
            n_s -= 1
        elif i == 'w':
            w_e += 1
        elif i == 'e':
            w_e -= 1
    return True if n_s == 0 and w_e == 0 and len(walk) == 10 else False

print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))