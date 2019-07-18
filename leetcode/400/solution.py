class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_found = ""
        numbers, counter = self._compute_start(n)
        if not counter:
            counter = 1
        if not numbers:
            numbers = 1
        counter += 1
        digits = n - numbers
        if digits == 0:
            return 1
        if not digits:
            digits = 1
        print("digits= ", digits)
        print("counter= ", counter)
        print("numbers= ", numbers)
        while digits > 0:
            s = str(counter)
            digits -= len(s)
            counter += 1
        digit_found = s[digits - 1]
        return int(digit_found)

    def _compute_start(self, n):
        import math
        start = 0
        numbers = 0
        skip = math.floor(math.log10(n))
        for i in range(skip - 1):
            length = i + 1
            case = int((int(math.pow(10, i + 1)) - int(math.pow(10, i))))
            numbers += case
            start += length * case
        return start, numbers