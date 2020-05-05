def findComplement(num):
    result = bin(num)[2:]
    res = ''
    for i in result:
        if i=='0':
            res+='1'
        else:
            res+='0'
    return int(res,2)

print(findComplement(8))