
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s)<len(t):
            return ""
        # 1. Declare Variable and get count of our target
        count_t = Counter(t)
        window = {}
        have = 0
        need = len(count_t)
        l = 0
        res = [-1,-1]
        min_len = float('inf')
        #2. Add elemnts to the window and their count
        for r,char in enumerate(s):
            window[char] = window.get(char,0)+1

            if char in count_t and window[char] == count_t[char]:
                have+=1
            #3. Shrink the window after the elements are found from left
            while need == have:
                if (r-l+1) < min_len:
                    res = [l,r]
                    min_len = r-l+1
                left_char = s[l]
                window[left_char]-=1
                if left_char in count_t and window[left_char]< count_t[left_char]:
                    have-=1
                l+=1

        l,r = res  # Save the Value of left and right ptr
        return s[l:r+1] if min_len != float('inf') else ""


       

        