class Solution:
    def compress(self, chars: list[str]) -> int:
        write = read = 0
        ans = 0
        count = 0

        while read < len(chars):
            char = chars[read]
            while read < len(chars) and char == chars[read]:
                read += 1
                count += 1
            chars[write] = char
            ans += 1
            write += 1
            if count > 1:
                for n in str(count):
                    chars[write] = n
                    write += 1
                    ans += 1
            count = 0
        return ans 
