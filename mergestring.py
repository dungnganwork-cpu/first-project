class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result =""
        len1, len2 = len(word1), len(word2)
        i = 0
        j = 0      
        while i < len1 or j < len2:
            if i < len1:
                result += word1[i]
                i += 1
            if j < len2:
                result += word2[j]
                j += 1
        return result
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

solution_instance = Solution()

merged_string = solution_instance.mergeAlternately(s1, s2)

print("Kết quả đã trộn:", merged_string)   
        
