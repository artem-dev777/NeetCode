class Solution:
    # this is a reverse version of solution_1
    # unlike solution_1, where the stack contained temperatures to the right of current day in ascending order
    # here we'll loop from the beginning to the end and keep the temperatures to the left of current day in descending order
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        n = len(t)
        s = [0]
        res = [0] * n

        for i in range(n):
            # once we reach a day with temperature higher than previous
            # we'll remove all positions from the stack that have lower temperature than current and log them in the result
            while s and t[i] > t[s[-1]]:
                res[s[-1]] = i - s[-1]
                s.pop()
            s.append(i)
        return res
