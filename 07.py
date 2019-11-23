# Eerie Mob

def mob(n):
    default = '(O_o)'
    if not n or not (1 <= n <= 255):
        return default

    guy = '(-_-)'
    guy_sl = '(-_'
    guy_sr = '_-)'
    guy_pl = '(-_-'
    guy_pr = '-_-)'
    guy_fl = '(-'
    guy_fr = '-)'

    guys = [''] * n

    # Guy in the middle
    middle = n // 2
    guys[middle] = guy

    for i in range((n - middle) // 3):
        g = middle - (i + 1) * 3
        if 0 <= g < n:
            guys[g] = guy_pl

        g = middle + (i + 1) * 3
        if 0 <= g < n:
            guys[g] = guy_pr

    for i in range(n):
        if guys[i]:
            continue
        if i < middle:
            guys[i] = guy_sl
        else:
            guys[i] = guy_sr

    if n > 7:
        guys[0] = guy_fl
        guys[-1] = guy_fr

    return ''.join(guys)
