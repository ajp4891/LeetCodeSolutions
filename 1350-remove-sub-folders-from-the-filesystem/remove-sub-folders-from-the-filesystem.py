class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda x:  x)
        d = set(folder)
        res = [folder[0]]

        for i in range(1, len(folder)):
            last_folder = res[-1]
            last_folder += "/"

            if not folder[i].startswith(last_folder):
                res.append(folder[i])

        return res