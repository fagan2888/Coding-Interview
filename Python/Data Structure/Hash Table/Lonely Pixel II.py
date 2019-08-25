import collections
class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        w, h = len(picture), len(picture[0])
        rows, cols = [0] * w, [0] * h
        for x in range(w):
            for y in range(h):
                if picture[x][y] == 'B':
                    rows[x] += 1
                    cols[y] += 1

        sdict = collections.defaultdict(int)
        for idx, row in enumerate(picture):
            sdict[''.join(row)] += 1

        ans = 0
        for x in range(w):
            row = ''.join(picture[x])
            if sdict[row] != N:
                continue
            for y in range(h):
                if picture[x][y] == 'B':
                    if rows[x] == N:
                        if cols[y] == N:
                            ans += 1
        return ans