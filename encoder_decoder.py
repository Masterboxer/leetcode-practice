from typing import List


class Solution:
    def encode(self, list_of_strings: List[str]) -> str:
        encoded_string_parts = []
        for string in list_of_strings:
            part = f"{len(string)}#{string}"  # Length + delimiter + actual string
            encoded_string_parts.append(part)
        final_encoded_string = "".join(encoded_string_parts)
        return final_encoded_string

    def decode(self, encoded_string: str) -> List[str]:
        decoded_strings = []
        current_index = 0
        total_length = len(encoded_string)

        while current_index < total_length:
            # Step 1: Read characters until we find the delimiter '#'
            length_string = ""
            while encoded_string[current_index] != "#":
                length_string += encoded_string[current_index]
                current_index += 1

            string_length = int(length_string)  # Convert to integer
            current_index += 1  # Move past the '#'

            # Step 2: Extract the string using the length
            current_string = encoded_string[
                current_index : current_index + string_length
            ]
            decoded_strings.append(current_string)

            # Step 3: Move the index forward by the length of the string
            current_index += string_length

        return decoded_strings


solution = Solution()
encoded = solution.encode(["neet", "code", "love", "you"])

print(encoded)
print(solution.decode(encoded))
