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

# figure out how many people of each type exist in US
totalPop = 327167439
races = {'W':197033939, 'B':46261485, 'H':59763631, 'A':22137269, 'O':16879839, 'N':5710410}
genders = {"M": .4924, "F": .5076}
demoData = {'BM': 0, 'HM': 0, 'NM': 0, 'OM': 0, 'WM': 0, 'AM': 0, 'BF': 0, 'NF': 0, 'HF': 0, 'OF': 0, 'WF': 0, 'AF': 0}
for name in parseData.keys():
    victim = parseData[name]
    if victim['race'] + victim['gender'] in demoData:
        demoData[victim['race'] + victim['gender']] += 1
    # else:
    #     demoData[victim['race'] + victim['gender']] = 1

# the average death rate among all Americans, as a basis for comparison
averageDeathRate = len(parseData.keys()) / totalPop

print ('total populations:')
for subGroup in demoData.keys():
    subGroupPop = races[subGroup[0]] * genders[subGroup[1]]
    print (f'{subGroup}: {subGroupPop}')
    # adjust relative to national average
    subGroupDeathRate = demoData[subGroup] / subGroupPop
    demoData[subGroup] = subGroupDeathRate / averageDeathRate

print(demoData)

