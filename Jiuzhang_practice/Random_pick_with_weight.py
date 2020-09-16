# Apple interview question
# using bisect
import numpy as np
from bisect import bisect
from random import uniform


class Solution:

    def __init__(self, w: List[int]):
        self.reference = np.cumsum(w) / float(sum(w))

    def pickIndex(self) -> int:
        rnd = uniform(0, 1)
        ind = bisect(self.reference, rnd)
        return ind
