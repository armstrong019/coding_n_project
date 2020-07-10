class Average_in_stream:
    def __init__(self):
        self.cache = []
    def add(self, number):
        self.cache.append(number)

    def average_between_numbers(self, startn, endn):
        if startn not in self.cache or endn not in self.cache:
            raise Exception('values not exits')
        for i in range(len(self.cache)):
            if self.cache[i] == startn:
                start_ind = i
            if self.cache[i] == endn:
                end_ind = i
        res = []
        for j in range(start_ind, end_ind):
            res.append((self.cache[j]+self.cache[j+1])/2)
        return res

solu = Average_in_stream()
solu.add(2)
solu.add(3)
solu.add(4)
solu.add(5)
solu.add(6)
solu.add(7)
solu.add(8)
print(solu.average_between_numbers(1,8))


