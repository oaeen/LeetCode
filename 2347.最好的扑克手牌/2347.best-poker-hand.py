from collections import Counter


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if max(suits) == min(suits):
            return "Flush"
        same = max(Counter(ranks).values())
        if same >= 3:
            return "Three of a Kind"
        if same == 2:
            return "Pair"
        else:
            return "High Card"
