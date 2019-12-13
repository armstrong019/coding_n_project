class sort_array:
    def __init__(self, a1,a2):
        self.p1 = 0
        self.p2 = 0
        self.a1 = a1
        self.a2= a2
    def __iter__(self):
        return self
    def __next__(self):
        if self.p1<len(self.a1) and self.p2<len(self.a2):
            if self.a1[self.p1]<self.a2[self.p2]:
                self.p1 += 1
                return self.a1[self.p1-1]
            else:
                self.p2 += 1
                return self.a2[self.p2-1]
        elif self.p1<len(self.a1):
            self.p1 += 1
            return self.a1[self.p1 - 1]
        elif self.p2<len(self.a2):
            self.p2 += 1
            return self.a2[self.p2 - 1]
        else:
            raise StopIteration

for x in sort_array([],[]):
    print(x)




