
    def __init__(self, arr):
        self.__elements = arr
    def computeDifference(self):
        maxN = max(self.__elements)
        minN = min(self.__elements)
        self.maximumDifference = abs(maxN - minN)

