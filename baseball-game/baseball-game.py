class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new = []
        for i in operations:
            try:
                new.append(int(i))
            except ValueError:
                if i == '+':
                    new.append(new[-1] + new[-2])
                elif i == 'D':
                    new.append(new[-1] * 2)
                elif i == 'C':
                    new.pop(-1)
        return sum(new)