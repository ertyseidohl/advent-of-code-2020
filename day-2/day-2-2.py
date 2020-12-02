valid = 0
with open('input', 'r') as f:
    for line in f:
        r, p = line.split(': ')
        mm, l = r.split(' ')
        mi, ma = mm.split('-')
        mi = int(mi) - 1
        ma = int(ma) - 1
        if (p[mi] == l or p[ma] == l) and not p[mi] == p[ma]:
            valid += 1
print(valid)
