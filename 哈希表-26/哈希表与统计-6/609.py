class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        res = []
        for path in paths:
            files = path.split(" ")
            for i in range(1, len(files)):
                root_path = files[i].split("(")[0]
                content = files[i].split("(")[1]
                content = content.replace(")", "")
                file_path = files[0] + '/' + root_path
                if content in dic:
                    dic[content].append(file_path)
                else:
                    dic[content] = [file_path]
        for key in dic:
            if len(dic[key]) > 1:
                res.append(dic[key])
        return res