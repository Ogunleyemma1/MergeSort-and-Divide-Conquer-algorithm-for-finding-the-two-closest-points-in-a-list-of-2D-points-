import pytest
import math
from divconq import Point2D, merge_sort, closest_pair

def test_merge_sort_empty():
    assert merge_sort([], key=lambda p: p.x) == []

def test_merge_sort_single_element():
    assert merge_sort([Point2D(1, 2)], key=lambda p: p.x) == [Point2D(1, 2)]

def test_merge_sort_two_elements():
    assert merge_sort([Point2D(3, 1), Point2D(1, 2)], key=lambda p: p.x) == [Point2D(1, 2), Point2D(3, 1)]

def test_merge_sort_duplicate_elements():
    assert merge_sort([Point2D(1, 2), Point2D(3, 1), Point2D(1, 2)], key=lambda p: p.x) == [Point2D(1, 2), Point2D(1, 2), Point2D(3, 1)]

def test_closest_pair_empty():
    assert closest_pair([]) == (None, None)

def test_closest_pair_single_element():
    assert closest_pair([Point2D(1, 2)]) == (None, None)

def test_closest_pair_two_elements():
    assert closest_pair([Point2D(1, 2), Point2D(3, 4)]) == (Point2D(1, 2), Point2D(3, 4))
    
def test_closest_pair_multiple_elements():
    points = [Point2D(1, 2), Point2D(3, 4), Point2D(2, 2), Point2D(5, 5)]
    result = closest_pair(points)
    assert (result == (Point2D(1, 2), Point2D(2, 2)) or result == (Point2D(2, 2), Point2D(1, 2)))
    
def test_closest_pair_duplicate_elements():
    points = [Point2D(1, 1), Point2D(1, 1), Point2D(1, 1)]
    result = closest_pair(points)
    assert (result == (Point2D(1, 1), Point2D(1, 1)))

def test_closest_pair_positive_negative_elements():
    points = [Point2D(-1, -1), Point2D(1, 1), Point2D(0, 0)]
    result = closest_pair(points)
    assert (
        result == (Point2D(-1, -1), Point2D(0, 0)) or 
        result == (Point2D(0, 0), Point2D(-1, -1)) or
        result == (Point2D(0, 0), Point2D(1, 1)) or
        result == (Point2D(1, 1), Point2D(0, 0))
    )

if __name__ == "__main__":
    pytest.main()