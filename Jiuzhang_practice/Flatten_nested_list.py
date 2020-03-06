# 这道题逻辑比较简单 implementation需要call API
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flat_list = []
        self.flatten_list(nestedList)

    def flatten_list(self, nestedList):
        for lst in nestedList:
            if lst.isInteger():
                self.flat_list.append(lst.getInteger())
            else:
                self.flatten_list(lst.getList())

    def next(self) -> int:
        if self.hasNext:
            return self.flat_list.pop(0)

    def hasNext(self) -> bool:
        return self.flat_list


List = []#[1, 0, [2,5, [3,[], [4]]]]
res = []
def flatten_list(nested_list, result):
    for lst in nested_list:
        if type(lst) is not list:
            result.append(lst)
        else:
            flatten_list(lst, result)

flatten_list(List,res)
print(res)



