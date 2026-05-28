class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for d in details:
            age = d[11:13]
            if int(age) > 60:
                result += 1

        return result