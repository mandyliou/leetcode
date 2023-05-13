class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        new = []
        desc = []
        for x,y in zip(heights, names):
            new.append((x,y))
        new.sort(reverse = True)

        for height, name in new:
            desc.append(name)
        return desc

