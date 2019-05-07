from unittest import TestCase
from typing import List

from entities.geometry import Rectangle, Point2D


class RectangleTest(TestCase):

    def test_points_for_rectangle_at_origin(self):
        width = 5
        height = 3
        rect = Rectangle(width, height)
        expected_points = [Point2D(0, 0), Point2D(width, 0), Point2D(width, height), Point2D(0, height)]
        actual_points = rect.points
        self._assert_points_are_equal(expected_points, actual_points)

    def test_points_for_positioned_rectangle(self):
        width = 5
        height = 3
        position = Point2D(1, 2)
        rect = Rectangle(width, height)
        rect.position = position
        expected_points = [position,
                           Point2D(position.x + width, position.y),
                           Point2D(position.x + width, position.y + height),
                           Point2D(position.x, position.y + height)]
        actual_points = rect.points
        self._assert_points_are_equal(expected_points, actual_points)

    def test_points_for_rotated_rectangle_at_origin(self):
        width = 5
        height = 3
        rect = Rectangle(width, height)
        rect.rotate(90)
        expected_points = [Point2D(0, 0), Point2D(0, width), Point2D(-height, width), Point2D(-height, 0)]
        actual_points = rect.points
        self._assert_points_are_equal(expected_points, actual_points)

    def test_points_for_positioned_rotated_rectangle(self):
        width = 5
        height = 3
        position = Point2D(1, 2)
        rect = Rectangle(width, height)
        rect.rotate(90)
        rect.position = position
        expected_points = [position,
                           Point2D(position.x, position.y + width),
                           Point2D(position.x - height, position.y + width),
                           Point2D(position.x - height, position.y)]
        actual_points = rect.points
        self._assert_points_are_equal(expected_points, actual_points)

    def test_rotate_360_degrees(self):
        width = 5
        height = 3
        rect = Rectangle(width, height)
        rect.rotate(360)
        expected_points = [Point2D(0, 0), Point2D(width, 0), Point2D(width, height), Point2D(0, height)]
        actual_points = rect.points
        self._assert_points_are_equal(expected_points, actual_points)

    def test_rotate_over_360_degrees(self):
        width = 5
        height = 3
        rect = Rectangle(width, height)
        rect.rotate(450)
        expected_points = [Point2D(0, 0), Point2D(0, width), Point2D(-height, width), Point2D(-height, 0)]
        actual_points = rect.points
        self._assert_points_are_equal(expected_points, actual_points)

    def test_rotate_clockwise(self):
        width = 5
        height = 3
        rect = Rectangle(width, height)
        rect.rotate(-90)
        expected_points = [Point2D(0, 0), Point2D(0, -width), Point2D(height, -width), Point2D(height, 0)]
        actual_points = rect.points
        self._assert_points_are_equal(expected_points, actual_points)

    def test_rotate_2_times(self):
        width = 5
        height = 3
        rect = Rectangle(width, height)
        rect.rotate(45)
        rect.rotate(45)
        expected_points = [Point2D(0, 0), Point2D(0, width), Point2D(-height, width), Point2D(-height, 0)]
        actual_points = rect.points
        self._assert_points_are_equal(expected_points, actual_points)

    def test_rotate_0_degrees(self):
        width = 5
        height = 3
        rect = Rectangle(width, height)
        rect.rotate(0)
        expected_points = [Point2D(0, 0), Point2D(width, 0), Point2D(width, height), Point2D(0, height)]
        actual_points = rect.points
        self._assert_points_are_equal(expected_points, actual_points)

    def _assert_points_are_equal(self, expected_points: List[Point2D], actual_points: List[Point2D]):
        for i in range(0, len(actual_points)):
            actual_point = actual_points[i]
            expected_point = expected_points[i]
            self.assertEqual(expected_point, actual_point, "Did not match for point {0}".format(i))
