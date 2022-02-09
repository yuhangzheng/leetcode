class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # step = i = 0
        # while i < len(data):
        #     if 127 < data[i] < 192:
        #         return False
        #     if 191 < data[i] < 224:
        #         if i >= len(data) -1:
        #             return False
        #         if 127 < data[i+1] < 192:
        #             i += 1
        #         else:
        #             return False
        #     if 223 < data[i] <240:
        #         if i >= len(data) -2:
        #             return False
        #         if 127 < data[i+1] < 192 and 127 < data[i+2] < 192:
        #             i += 2
        #         else:
        #             return False
        #     if 239 <data[i] < 248:
        #         if i >= len(data) -3:
        #             return False
        #         if 127 < data[i+1] < 192 and 127 < data[i+2] < 192 and 127< data[i+3] < 192:
        #             i += 3
        #         else:
        #             return False
        #     if data[i] >247:
        #         return False
        #     i += 1
        # return True

        # 官解1
        # Number of bytes in the current UTF-8 character
        n_bytes = 0

        # For each integer in the data array.
        for num in data:

            # Get the binary representation. We only need the least significant 8 bits
            # for any given number.
            bin_rep = format(num, '#010b')[-8:]

            # If this is the case then we are to start processing a new UTF-8 character.
            if n_bytes == 0:

                # Get the number of 1s in the beginning of the string.
                for bit in bin_rep:
                    if bit == '0': break
                    n_bytes += 1

                # 1 byte characters
                if n_bytes == 0:
                    continue

                # Invalid scenarios according to the rules of the problem.
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                # Else, we are processing integers which represent bytes which are a part of
                # a UTF-8 character. So, they must adhere to the pattern `10xxxxxx`.
                if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                    return False

            # We reduce the number of bytes to process by 1 after each integer.
            n_bytes -= 1

        # This is for the case where we might not have the complete data for
        # a particular UTF-8 character.
        return n_bytes == 0

        # ## 官解2
        #         # Number of bytes in the current UTF-8 character
        # n_bytes = 0

        # # Mask to check if the most significant bit (8th bit from the left) is set or not
        # mask1 = 1 << 7

        # # Mask to check if the second most significant bit is set or not
        # mask2 = 1 << 6
        # for num in data:

        #     # Get the number of set most significant bits in the byte if
        #     # this is the starting byte of an UTF-8 character.
        #     mask = 1 << 7
        #     if n_bytes == 0:
        #         while mask & num:
        #             n_bytes += 1
        #             mask = mask >> 1

        #         # 1 byte characters
        #         if n_bytes == 0:
        #             continue

        #         # Invalid scenarios according to the rules of the problem.
        #         if n_bytes == 1 or n_bytes > 4:
        #             return False
        #     else:

        #         # If this byte is a part of an existing UTF-8 character, then we
        #         # simply have to look at the two most significant bits and we make
        #         # use of the masks we defined before.
        #         if not (num & mask1 and not (num & mask2)):
        #             return False
        #     n_bytes -= 1
        # return n_bytes == 0    