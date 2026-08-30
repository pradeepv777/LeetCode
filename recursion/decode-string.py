class Solution:
    def decodeString(self, s: str) -> str:
        result = []
        count = ""
        string = ""
        i = 0
        n = len(s)
        
        while i < n:
            if s[i].isnumeric():
                count += s[i]
            elif s[i] == '[':
                # Push the current string state and count onto result, then reset them
                result.append((string, int(count)))
                string = ""
                count = ""
            elif s[i] == ']':
                # Pop the last state and rebuild the string
                prev_string, repeat_count = result.pop()
                string = prev_string + (string * repeat_count)
            else:
                string += s[i]
            i += 1
            
        return string
