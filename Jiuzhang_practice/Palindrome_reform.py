
example = 'facexzface'

def check_reform(s):
    dic = {}
    for i in range(len(s)):
        if s[i] in dic:
            dic[s[i]]+=1
        else:
            dic[s[i]]=1
    count_odd = 0
    for key in dic:
        if dic[key]%2 == 1:
            count_odd += 1
            if count_odd > 1:
                return False
    return True

print(check_reform(example))
