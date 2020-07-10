

user = [[1, 'x.com','y.com'], [1,'x.com','y.com'],[1,'x.com','y1.com'], [1, 'x.com','y2.com'], [2,'x.com','z.com'], [3,'x1.com','z.com'], [2,'x.com','z.com']]

def count_percentage(user_data):
    dic = {}
    for i in range(len(user_data)):
        id = user_data[i][0]
        src_url = user_data[i][1]
        dest_url = user_data[i][2]
        # count the frequencies of the data
        if (id, src_url) not in dic:
            dic[(id, src_url)] = {dest_url:1}
        else:
            if dest_url in dic[(id, src_url)]:
                dic[(id, src_url)][dest_url]+=1
            else:
                dic[(id, src_url)][dest_url]=1
    # count the percentage of the data
    for key in dic.keys():
        stats = dic[key] # this is a dict
        total_counts = sum(stats.values())
        for key0 in dic[key].keys():
            dic[key][key0] = float(dic[key][key0])/float(total_counts)
    return dic


print(count_percentage(user))



