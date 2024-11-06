from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Using '#' as a separator between length and string for unambiguous parsing
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}#{s}"  # Include '#' as separator
        return encoded_string

    def decode(self, encoded_string: str) -> List[str]:
        final_array = []
        i = 0
        while i < len(encoded_string):
            # Find the position of the separator
            j = encoded_string.find('#', i)
            # Parse the length of the next word
            length = int(encoded_string[i:j])
            # Move to the actual string part after '#'
            i = j + 1
            # Extract the string based on the parsed length
            final_array.append(encoded_string[i:i + length])
            # Move the pointer to the next encoded part
            i += length
        return final_array

# Example usage
solution = Solution()
encoded = solution.encode(["neet", "code", "love", "you"])
print("Encoded:", encoded)
decoded = solution.decode(encoded)
print("Decoded:", decoded)
