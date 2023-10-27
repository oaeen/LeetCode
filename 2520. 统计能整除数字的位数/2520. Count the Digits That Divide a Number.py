class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        tmp = num
        while tmp != 0:
            digit = tmp % 10
            tmp //= 10
            if num % digit == 0:
                count += 1
        return count
