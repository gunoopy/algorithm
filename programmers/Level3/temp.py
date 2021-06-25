# param0 = ['/a/a_v2.x', '/b/a.x', '/c/t.z', '/d/a/t.x', '/e/z/t_v1.z', '/k/k/k/a_v9.x']
# param0 = ['/t.z', '/z/z_v2.z', '/a.z', '/d/b.z', '/d/a/t.z']
param0 = ['/t.z', '/b/b.z', '/a.z', '/e/k.z', '/d/a/x_v2.z']



file_names = []
answer = []

for x in param0 :
    file_name = x.split('/')[-1]
    if len(file_name) > 3 :
        file_name = file_name[0] + file_name[-2:]
    file_names.append(file_name)

for x in file_names :
    cnt = file_names.count(x)
    if cnt > 1 and x not in answer :
        answer.append(x)
        answer.append(str(cnt))

print(answer)