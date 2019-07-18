import sys
from solution import Solution


if __name__ == "__main__":
    sol = Solution()
    n = int(sys.argv[1])
    # print(sol._compute_start(n))
    s1 = sol.findNthDigit(n)
    print("Solution = ", s1)
