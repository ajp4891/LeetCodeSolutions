class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1: 'I',
            4: "IV",
            5: 'V',
            9: "IX",
            10: 'X',
            40: "XL",
            50: 'L',
            90: "XC",
            100: 'C',
            400: "CD",
            500: 'D',
            900: "CM",
            1000: 'M',
        }
        
        res = []
        for n in sorted(d.keys(), reverse=True):
            count, num = divmod(num, n)
            res.append(d[n] * count)

        return "".join(res) 