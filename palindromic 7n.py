def unique(num):
    for char in str(num):
        if str(num).count(char) > 1:
            return False
    return True

print([x for x in range(1000,10000)
       if (x%7 is 0
           and int(''.join(list(reversed([char for char in str(x)])))) %7) is 0
       and unique(x)])