def readPoints(filename):
    points = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y = map(int, line.split(","))
            points.append((x, y))
    return points


def largestRectArea(points):
    maxArea = 0

    for i in range(len(points)):
        x1, y1 = points[i]
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]

            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1

            area = width * height
            maxArea = max(maxArea, area)

    return maxArea


if __name__ == "__main__":
    points = readPoints("adventinput9")
    print(largestRectArea(points))


#4761598821
