class Solution:
    # the solution to this problem is somewhat similar to Daily Temperature problem
    # the intuition behind the solution considers the fact, that for rectangle area we need height, left border and right border
    # now we may notice that while the heights are going one after another strictly in ascending order,
    # then we're only dealing with left borders of the rectangle
    # and only once the current height is less than previous, then we encounter the right border of the rectangle
    #
    # thus, we can populate the stack with heights and their positions, while they go in ascending order
    # and once the current height is lower, than previous one, then we can treat it as a right border
    # and calculate the area of all rectangles that closed on this position
    # in the end we'll get a list of all rectangles areas and return the max one
    #
    # this solution performed better than 99% of Neetcode solutions in terms of memory and speed
    #
    # the stack will consist of heights and their positions
    def largestRectangleArea(self, heights: List[int]) -> int:
        # rename list for convinience
        h = heights
        s = []
        res_list = []

        for i, h1 in enumerate(h):
            pos = i
            # once we encounter the right border (meaning that current height is lower than the top of the stack)
            # we remove all heights from the stack, that are higher than current height
            # and calculate respective rectangle areas
            while s and s[-1][0] > h1:
                res_list.append(s[-1][0] * (i - s[-1][1]))
                pos = s[-1][1]
                s.pop()
            # we add to the stack only if it's empty or current height is higher than top of the stack
            if (s and s[-1][0] < h1) or not s:
                s.append([h1, pos])
        # at then end we compute the remaining rectangles in the stack
        for item in s:
            res_list.append(item[0] * (len(heights) - item[1]))
        return max(res_list)
