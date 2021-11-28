class Solution:
    def originalDigits(self, s: str) -> str:
        # zero one two three four five six seven eight nine
        # z n-7-2*9 w  h-8   u   f-4   x   s-6    g   i-5-6-8
        count = collections.Counter(s)
        out = {}
        out["0"] = count["z"]
        out["2"] = count["w"]
        out["4"] = count["u"]
        out["6"] = count["x"]
        out["8"] = count["g"]
        out["3"] = count["h"] - out["8"]
        out["5"] = count["f"] - out["4"]
        out["7"] = count["s"] - out["6"]
        out["9"] = count["i"] - out["5"] - out["6"] - out["8"]
        out["1"] = count["n"] - out["7"] - 2 * out["9"]

        return "".join(key * out[key] for key in sorted(out.keys()))