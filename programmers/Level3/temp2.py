# param0 = ['INT', 'INT', 'BOOL', 'SHORT', 'LONG']
# param0 = ['FLOAT', 'SHORT', 'BOOL', 'BOOL', 'BOOL', 'INT']
param0 = ['BOOL', 'LONG', 'SHORT', 'LONG', 'BOOL', 'LONG', 'BOOL', 'LONG', 'SHORT', 'LONG', 'LONG']

dic = {'BOOL': 1, 'SHORT': 2, 'FLOAT': 4, 'INT': 8, 'LONG': 16}
answer = ''
memory = 0


for x in param0 :

    alloc = dic[x]
    remainder = memory % alloc
    if x != 'LONG' :
        if memory != 0 and memory % 8 == 0 : answer += ','
        if remainder :
            answer += '.' * (alloc - remainder)
            memory += 2*alloc - remainder
        else :
            memory += alloc
        answer += '#' * alloc
    else :
        if remainder :
            ddd = alloc - remainder
            ddd %= 8
            answer += '.' * (ddd) + ',########,########'

            memory += 2*alloc - remainder
        else :
            if memory != 0 : answer += ','
            answer += '########,########'
            memory += alloc



    print(answer, memory)

print(answer, memory)

if memory > 128 :
    print('HALT')
else :
    if memory % 8 :
        answer += '.' * (8 - memory % 8)
    print(answer)