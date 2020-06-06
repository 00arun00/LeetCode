class Solution:
    def __init__(self, w: List[int]):
        import random
        total_w = sum(w)
        self.w = []
        curr = 0 
        # go through each element and create a cumulative sum array 
        for i in w:
            self.w.append(curr/total_w)
            curr += i

    def pickIndex(self) -> int:
        rand = random.random()
        import bisect 
        # return idx using binary serch
        return bisect.bisect_left(self.w,rand)-1
