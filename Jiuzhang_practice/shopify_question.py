# just had the shopify pair programming test for senior data scientist
# the question was given an input string, write a function outputting a list of all strings where '?' corresponds to 0 or 1
# so e.g.
# '0' -> ['0']
# '0?' -> ['00', '01']
# '10?1?' -> ['10010', '10110', '10011', '10111']
# after i solved it, the questions were "what's the time complexity of the solution, space complexity"
# "what would you do to move this to production"



def dfs(s, res, i, current_path):
    if i == len(s):
        res.append(current_path)
        return
    if s[i] != '?':
        dfs(s, res, i+1, current_path+s[i])
    else:
        dfs(s, res, i+1, current_path+'0')
        dfs(s, res, i+1, current_path+'1')

def convert_string(s):
    result = []
    dfs(s, result, 0, '')
    return result

result = convert_string('10?1?')
print(result)
