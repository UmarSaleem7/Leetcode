def minAddToMakeValid(self, s: str) -> int:
    c1 = 0
    c2 = 0
    count = 0
    for parenthesis in s:
        if parenthesis == '(':
            c1 += 1
        else:
            c2 += 1
        if c2 > c1:
            count += 1
            c2 = c1
    return count + (c1 - c2)
