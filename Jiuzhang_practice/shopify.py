
def dfs(current_path, rest, result):
    if not rest:
        result.append(current_path)
        return
    if rest[0] == '?':
        dfs(current_path + '0', rest[1:], result)
        dfs(current_path + '1', rest[1:], result)
    else:
        dfs(current_path + rest[0], rest[1:], result)

def find_output(string):
    result = []
    dfs('', string, result)
    return result


s = '?1??'
print(find_output(s))
