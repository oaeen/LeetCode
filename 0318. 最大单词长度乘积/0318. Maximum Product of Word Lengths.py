class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        brute force
        """
        max_count = 0
        s_words = [set(w) for w in words]
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                intersection = set(s_words[i]) & set(s_words[j])
                if len(intersection) == 0:
                    max_count = max(len(words[i]) * len(words[j]), max_count)

        return max_count


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        使用 Bit Manipulation 优化
        """
        masks = [
            sum(1 << (ord(char) - ord("a")) for char in set(word)) for word in words
        ]
        lengths = [len(word) for word in words]
        max_product = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if masks[i] & masks[j] == 0:
                    max_product = max(max_product, lengths[i] * lengths[j])

        return max_product
