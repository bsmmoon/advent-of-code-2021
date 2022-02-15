# base is brute force O(N)
#
# i-1 < i < i+1 => i is peak
#
# if it is downhil, we know that peak is to the leftz
# if it is uphil, we know that peak is to the right

import requests

input_url = 'https://raw.githubusercontent.com/bsmmoon/AdventOfCode2021/main/day1.input'
data = requests.get(url=input_url).text.split("\n")


class Solution(object):
    def solve(self, nums):
        return len(data)


class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output


tests = [
    Test([[199, 200, 208, 210, 200, 207, 240, 269, 260, 263, ]], (1, 3))]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.solve(*test.input), test.output))
