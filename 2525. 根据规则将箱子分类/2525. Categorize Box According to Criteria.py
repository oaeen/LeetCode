class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        vol = length * width * height

        bulky_flag = False
        heavy_flag = False if mass < 100 else True
        if max(length, width, height) >= 10**4 or vol >= 10**9:
            bulky_flag = True

        if bulky_flag and heavy_flag:
            return "Both"
        elif bulky_flag:
            return "Bulky"
        elif heavy_flag:
            return "Heavy"
        else:
            return "Neither"


# index version
class Solution:
    """
    from: https://leetcode.com/problems/categorize-box-according-to-criteria/solutions/3015443/python-3-2-lines-w-explanation-t-m-100-100/
    Bulky    Heavy    idx         bits    string
    –––––    ––––––   –––––––     ––––    –––––––
    False    False    0+0 = 0     00      Neither
    True     False    1+0 = 1     01      Bulky
    False    True     0+2 = 2     10      Heavy
    True     True     1+2 = 3     11      Both
    """

    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        vol = length * width * height
        bulky = int(max(length, width, height) >= 10**4 or vol >= 10**9)
        heavy = 2 * (mass >= 100)
        idx = bulky + heavy
        return ("Neither", "Bulky", "Heavy", "Both")[idx]
