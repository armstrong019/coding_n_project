class business:
    def __init__(self, name, location, id):
        self.name = name
        self.location = location
        self.id = id


business_List = [business('Starbucks','Seattle',101),
                 business('Peets coffee','San Fran',102),
                 business('Whole foods','Austin',103),
                 business('Starbucks','San Fran',104),
                 business('Peets coffee', 'Austin', 105),
                 business('Starbucks', 'Austin', 106),
                 business('Whole foods', 'Austin', 107),
                 business('Whole foods','Austin',103)]

class business_frequency:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency=frequency

def identify_chain(List, city):
    dic = {}
    for bs in List:
        location = bs.location
        id = bs.id
        name = bs.name
        if location == city:
            if name not in dic:
                dic[name] = set([id])
            else:
                dic[name].add(id)
    if not dic:
        return []
    res = []
    for name in dic:
        res.append(business_frequency(name,len(dic[name])))
    return sorted(res, key=lambda x: [x.frequency], reverse=True)

result = identify_chain(business_List, 'Austin')
print([(x.name, x.frequency) for x in result])


def identifyChainBusiness(List,city):
    chains = []
    businessSet = set()
    businessMap = {}
    for i in range(len(List)):
        if List[i].name != "" and List[i].location != "" and List[i].id != "":
            res = ""
            res += List[i].name
            res += "-"
            res += List[i].location
            res += "-"
            res += str(List[i].id)
            if res not in businessSet:
                businessSet.add(res)
    for bus in businessSet:
        arr = bus.split("-")
        name = arr[0]
        location = arr[1]
        id = arr[2]
        if location == city:
            businessMap[name] = businessMap.get(name,0)+1
    for key, value in sorted(businessMap.items(), key = lambda i:(i[1],i[0]), reverse = False):
        chains.append(business_frequency(key, value))
    return chains

result = identifyChainBusiness(business_List, 'Austin')
print([(x.name, x.frequency) for x in result])


