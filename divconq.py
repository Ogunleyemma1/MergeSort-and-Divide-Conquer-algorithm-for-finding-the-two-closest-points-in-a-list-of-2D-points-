import math
from typing import Tuple

class Point2D:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return f"@Point2D ({self._x}, {self._y})"
    
    def __eq__(self, value: object) -> bool:
        return self.x == value.x and self.y == value.y; 

    @property
    def x(self) -> float:
        return self._x
    
    @property
    def y(self) -> float:
        return self._y
    
def merge_sort(points: list[Point2D], key=lambda p: p) -> list[Point2D]:
    #Implementing a condition if list is empty or has one element, it is already sorted
    if len(points) <= 1:
        return points
    
    #Find the pivot of the list which is the middle
    midPivot = len(points) // 2

    #Recursively sorting the left and right parts of the list
    leftPart = merge_sort(points[:midPivot], key)
    rightPart = merge_sort(points[midPivot:], key)

    #Merge the LHS and RHS with a helper function
    return merge(leftPart, rightPart, key)


#Helper function to help merge the list
def merge(left: list[Point2D], right: list[Point2D], key) -> list[Point2D]:
    # define an array of the sorted list
    sortedList = []

    #initialize counter i and j
    i = j = 0

    #Perform merge on the left and right list based on the key function
    while i < len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
            sortedList.append(left[i])
            i += 1
        else:
            sortedList.append(right[j])
            j += 1
    
    #Appending the remaining elements from the left list
    while i < len(left):
        sortedList.append(left[i])
        i += 1
    
    #Appending the remaining elements for the left list
    while j < len(right):
        sortedList.append(right[j])
        j += 1

    #return the sorted list
    return sortedList

def closest_pair(points: list[Point2D]) -> Tuple[Point2D, Point2D]:
    
    if len(points) < 2:
        return (None, None)
    
    #Sort points by X and by y
    sortedPointX = merge_sort(points, key=lambda p: p.x)
    sortedPointY = merge_sort(points, key=lambda p: p.y)

    #Call the recursive function
    p1, p2, min_dist = closest_pair_recursive(sortedPointX, sortedPointY)

    return p1, p2

#Defining a helper function to help calculate the distances between two points
def distance(p1: Point2D, p2: Point2D) -> float:
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

#Helper function to help calculate recurssively
def closest_pair_recursive(sortedPointX: list[Point2D], sortedPointY: list[Point2D]) -> Tuple[Point2D, Point2D, float]:
    n = len(sortedPointX)

    #Base Case: if there are 2 or 3 points, use brute force
    if n <= 3:
        minPair = (sortedPointX[0], sortedPointX[1])
        minDistance = distance(minPair[0], minPair[1]) 
        for i in range(n):
            for j in range(i + 1, n):
                if i != j:
                    d = distance(sortedPointX[i], sortedPointX[j])
                    if d < minDistance:
                        minDistance = d
                        minPair = (sortedPointX[i], sortedPointX[j])
        return minPair[0], minPair[1], minDistance
    
    #if the point exceeds 3 we divide the points into left and right part
    midPivot = n // 2
    midPoint = sortedPointX[midPivot]

    leftRegionX = sortedPointX[:midPivot]
    rightRegionX = sortedPointX[midPivot:]

    #Define an array to take the Y coordinates of the left and right region
    leftRegionY = []
    rightRegionY = []

    #Append the Y coordinated based on Left and Right sorted region point in X
    for point in sortedPointY:
        if point.x <= midPoint.x:
            leftRegionY.append(point)
        else:
            rightRegionY.append(point)
    
    #Recursively find the smallest distances in the left and right halves
    (p1_left, p2_left, dist_left) = closest_pair_recursive(leftRegionX, leftRegionY)
    (p1_right, p2_right, dist_right) = closest_pair_recursive(rightRegionX, rightRegionY)

    #Find the smallest distance in the left and right region
    if dist_left < dist_right:
        min_dist = dist_left
        minPair = (p1_left, p2_left)
    else:
        min_dist = dist_right
        minPair = (p1_right, p2_right)
    
    #Create a strip of points within the minimum distance of the middle line
    strip = [point for point in sortedPointY if abs(point.x - midPoint.x) < min_dist]

    #Check the points in the strip and find the closest pair
    stripLength = len(strip)
    for i in range(stripLength):
        for j in range(i + 1, min(i +7, stripLength)): #Only need to check 7 next neighbour points
            if i != j:
                d = distance(strip[i], strip[j])
                if d < min_dist:
                    min_dist = d
                    minPair = (strip[i], strip[j])
    return minPair[0], minPair[1], min_dist






