class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringLengthS = len(s)
        stringLengthT = len(t)
        characterHashMapS = {}  # val : count
        characterHashMapT = {}  # val : count

        if stringLengthS != stringLengthT:
            return False

        for n in s:
            if n in characterHashMapS:
                characterHashMapS[n] = characterHashMapS[n] + 1
            else:
                characterHashMapS[n] = 1

        for n in t:
            if n in characterHashMapT:
                characterHashMapT[n] = characterHashMapT[n] + 1
            else:
                characterHashMapT[n] = 1

        if characterHashMapS == characterHashMapT:
            return True
        return False


solution = Solution()
result = solution.isAnagram("anagram", "nagaram")
print(result)
