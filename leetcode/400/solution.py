class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        size = 1
        stop = 9
        limit = size * stop
        while n > limit:
            n -= limit
            size += 1
            stop *= 10
            limit = size * stop
        start = stop / 9 + (n - 1) // size
        return int(str(start)[(n - 1) % size])
