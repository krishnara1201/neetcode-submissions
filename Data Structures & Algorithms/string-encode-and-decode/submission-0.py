class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        n = len(s)
        current_str = ""
        res = []
        i = 0
        current_num = ""
        while i < n:
            if s[i] != "#":
                current_num += s[i]
                i += 1
            else:
                # print(current_num)
                j = int(current_num)
                i += 1
                while j > 0:
                    current_str += s[i]
                    i += 1
                    j -= 1
                res.append(current_str)
                current_str = ""
                current_num = ""

        
        return res
            