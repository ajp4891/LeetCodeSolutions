class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def get_words(i):
            # get a list of words per line
            curr_line = []
            curr_length = 0

            while i < len(words) and curr_length + len(words[i]) <= maxWidth:
                curr_line.append(words[i])
                curr_length += len(words[i]) + 1
                i += 1

            return curr_line

        def create_line(words_per_line, ind):
            # return the line with spaces
            start_len = -1

            for word in words_per_line:
                start_len += len(word) + 1

            extra_space = maxWidth - start_len

            if len(words_per_line) == 1 or ind == len(words):
                return " ".join(words_per_line) + " " * extra_space

            word_count = len(words_per_line) - 1
            space_per_word = extra_space // word_count
            left_over_space = extra_space % word_count

            for j in range(left_over_space):
                words_per_line[j] += " "

            for j in range(word_count):
                words_per_line[j] += " " * space_per_word

            return " ".join(words_per_line)

        ans = []
        i = 0

        while i < len(words):
            curr_line = get_words(i)
            i += len(curr_line)
            ans.append(create_line(curr_line, i))

        return ans