class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        n = len(s)

        for i in range(n):
            count = {}

            for j in range(i, n):
                count[s[j]] = count.get(s[j], 0) + 1

                window_size = j - i + 1
                max_frequency = max(count.values())
                replacements = window_size - max_frequency

                if replacements <= k:
                    max_length = max(max_length, window_size)
                else:
                    break

        return max_length