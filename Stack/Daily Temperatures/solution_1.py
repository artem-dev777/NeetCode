class Solution:
    # for this problem, if we loop from the end to the beginning of the list, we only care about temperatures
    # that are higher than current temperature
    # so for each new element we can remove from the stack all temperatures, that are lower than current
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        n = len(t)
        s = [n - 1]
        res = [0] * n

        for i in range(n - 2, -1, -1):
            # here on each loop the stack will contain only the current temperature positions
            # and those that have higher temperature than current
            # this way, the stack is already sorted both in terms of positions and temperatures
            while s and t[i] >= t[s[-1]]:
                s.pop()
            s.append(i)

            # so here if the second element in the stack (from the top) exists
            # it will give us information on the answer for current day
            if len(s) > 1:
                res[i] = s[-2] - i
        return res
