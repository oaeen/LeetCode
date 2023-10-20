from sortedcontainers import SortedList


# copy from https://leetcode.com/problems/avoid-flood-in-the-city/solutions/2850099/Python-HashMap-+-SortedList-Solution-or-Faster-than-91-or-Commented-or-Simple/
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # dryDays = Set of available days that can be used for drying a full lake.
        dryDays, numDays = SortedList(), len(rains)
        # fullLakes is a hashMap which stores Lake number -> day on which it became full.
        fullLakes, ans = defaultdict(int), []
        for idx in range(numDays):
            if rains[idx] == 0:
                # This day can be used as a day to dry some lake.
                dryDays.add(idx)
                # Any number would be ok. This will get overwritten eventually.
                # If it doesn't get overwritten, its totally ok to dry a lake
                # irrespective of whether it is full or empty.
                ans.append(1)
            # Rained in rains[i]-th lake.
            else:
                lake = rains[idx]
                if lake in fullLakes:
                    # We must dry this lake before it rains in this lake.
                    # So find a day in "drydays" to dry this lake. Obviously, that day must be
                    # a day that is after the day on which the lake was full.
                    # i.e. if the lake got full on 7th day, we must find a dry day that is
                    # greater than 7.
                    dryDayIdx = dryDays.bisect_left(fullLakes[lake])
                    # If there is no available dry day to dry the lake, flooding is inevitable.
                    if dryDayIdx == len(dryDays):
                        return []
                    # Great, we found a day which we can use to dry this lake.
                    dryDay = dryDays[dryDayIdx]
                    # Overwrite the "1" and dry "lake"-th lake instead.
                    ans[dryDay] = lake
                    # We dried "lake"-th lake on "dryday", and we can't use the same day to
                    # dry any other lake, so remove the day from the set of available drydays.
                    dryDays.remove(dryDay)
                # Update that the "lake" became full on "i"-th day.
                fullLakes[lake] = idx
                # As the problem statement expects.
                ans.append(-1)
        return ans
