class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        if image[sr][sc] == newColor:
            return image

        origColor = image[sr][sc]
        self.fill(image, sr, sc, origColor, newColor)
        return image

    def fill(self, image, row, col, origColor, newColor):
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != origColor:
            return

        image[row][col] = newColor

        self.fill(image, row + 1, col, origColor, newColor) # down
        self.fill(image, row - 1, col, origColor, newColor) # up
        self.fill(image, row, col + 1, origColor, newColor) # right
        self.fill(image, row, col - 1, origColor, newColor) # left
