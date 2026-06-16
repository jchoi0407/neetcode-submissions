class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        
        return encoded
            
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            # j finds the anchor '#'
            j = i
            while s[j] != "#":
                j += 1
            
            # Slice the length and convert to integer
            length = int(s[i:j])
            
            # Slice the exact word using the length
            word = s[j + 1 : j + 1 + length]
            decoded.append(word)
            
            # Move the main pointer past the processed word
            i = j + 1 + length
            
        return decoded 
            
        
        
