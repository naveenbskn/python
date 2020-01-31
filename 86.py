def compress(string):
    temp={}
    result=" "
    for x in string:
        if x in temp:
            temp[x] = temp[x]+1
        else:
            temp[x] = 1
    for key, value in temp.items():
        result += str(key) + str(value)

    return result




s = input()
print(compress(s))
