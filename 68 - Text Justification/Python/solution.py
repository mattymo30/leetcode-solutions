class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        curr_row = []
        num_of_chars = 0
        num_of_words = 0
        index = 0
        n = len(words)
        while index < n:
            word = words[index]
            len_word = len(word)
            # can add the word to this current row
            if num_of_chars + len(curr_row) + len_word <= maxWidth:
                num_of_chars += len_word
                num_of_words += 1
                curr_row.append(word)
                index += 1
            # need to finalize the row and account for spaces
            else:
                num_spaces_needed = maxWidth - num_of_chars
                if len(curr_row) == 1:
                    # only one word
                    ans.append(curr_row[0] + " " * num_spaces_needed)
                else:
                    spaces_split = num_spaces_needed // (num_of_words - 1)
                    # keep track of spaces, empty slots on the left assigned more
                    spaces = [spaces_split] * (num_of_words - 1)
                    leftover_spaces = num_spaces_needed % (num_of_words - 1)
                    j = 0
                    while leftover_spaces != 0:
                        spaces[j] += 1
                        leftover_spaces -= 1
                        j += 1
                        if j == len(spaces):
                            j = 0
                    row_str = curr_row[0]
                    for i in range(num_of_words - 1):
                        row_str += " " * (spaces[i])
                        row_str += curr_row[i + 1]
                    ans.append(row_str)

                num_of_chars = 0
                num_of_words = 0
                curr_row = []

        final_line = " ".join(curr_row)
        len_final = len(final_line)
        final_line = final_line + " " * (maxWidth - len_final)
        ans.append(final_line)
        return ans

        
