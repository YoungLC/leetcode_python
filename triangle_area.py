class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        points_len = len(points)
        area_list = []
        for i in range(0, points_len - 2):
            (x1, y1) = points[i]
            for j in range(1, points_len - 1):
                (x2, y2) = points[j]
                for k in range(2, points_len):
                    (x3, y3) = points[k]
                    area = abs(float(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
                    area_list.append(area)
        print area_list
        return max(area_list)


if __name__ == '__main__':
    points = [[1, 0], [0, 0], [0, 1]]
    print Solution().largestTriangleArea(points)
