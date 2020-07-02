f_open = open('police_homicides.csv','r')
data = f_open.read()
f_open.close()
# print(data)
data = data.split('\n')
print(data[0])
columns = data[0].split(',')
parseData = {}
for line in data[1:]:
    victimData = line.split(',')
    # print(victim)
    x = {columns[i]: victimData[i] for i in range(len(columns) - 1)}
    parseData[x['name']] = x

# for name in parseData.keys():
#     print(parseData[name])
#     break

print ('processed {} lines.'.format(len(parseData.keys())))
demoData = {}
demoFractions = {'WM': .31, 'WF': .31, }
for name in parseData.keys():
    victim = parseData[name]
    if victim['race'] + victim['gender'] in demoData:
        demoData[victim['race'] + victim['gender']] += 1
    else:
        demoData[victim['race'] + victim['gender']] = 1

print(demoData)

