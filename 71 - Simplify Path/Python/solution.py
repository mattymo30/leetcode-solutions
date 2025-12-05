class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        print(path)

        stack = []

        for p in path:
            if p == "" or p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)
