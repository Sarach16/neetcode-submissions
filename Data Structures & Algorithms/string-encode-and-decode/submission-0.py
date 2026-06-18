class Solution:

    def encode(self, strs: List[str]) -> str:
        # I need a delimeter followed by the count for each string
        encoded_str = []
        for s in strs:
            encoded_str.append(str(len(s)))
            encoded_str.append("|")
            encoded_str.append(s)
        encoded_str = "".join(encoded_str)

        return encoded_str
        

  


    def decode(self, s: str) -> List[str]:
        count =""
        build_str =""
        decoded_str =[]
        i= 0

        while i < len(s):
            if s[i] == '|':
                build_str = s[i+1 : i+1 + int(count)]
                decoded_str.append(build_str)
                build_str = ""
                i += 1 + int(count)
                count =""
            else:
                count += s[i]
                i += 1
        
        return decoded_str






