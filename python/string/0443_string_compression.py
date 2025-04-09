# LeetCode 443: String Compression
# https://leetcode.com/problems/string-compression

class Solution:
    def compress(self, chars: list[str]) -> int:
        """
        Given an array of characters chars, compress it using the following algorithm:
        
        Begin with an empty string s. For each group of consecutive repeating characters in chars:
        - If the group's length is 1, append the character to s.
        - Otherwise, append the character followed by the group's length.
        
        The compressed string should be stored in the original array chars, and the new length of chars should be returned.
        
        The problem can be solved in O(n) time and O(1) space complexity (excluding the input array).
        """
        write_index = 0
        read_index = 0
        
        while read_index < len(chars):
            current_char = chars[read_index]
            count = 0
            
            # Count the number of occurrences of current_char
            while read_index < len(chars) and chars[read_index] == current_char:
                read_index += 1
                count += 1
            
            # Write the character to the array
            chars[write_index] = current_char
            write_index += 1
            
            # If count > 1, convert it to string and write to the array
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1
        
        return write_index