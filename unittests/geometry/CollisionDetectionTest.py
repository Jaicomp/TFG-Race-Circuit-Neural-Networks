from unittest import TestCase
from typing import List

from entities.geometry import Shape, Point2D, CollisionDetection


class CollisionablePolygonExample(Shape):

    def __init__(self, points: List[Point2D]):
        self.__points = points

    @property
    def points(self) -> List[Point2D]:
        return self.__points


class CollisionDetectionTest(TestCase):
    def test_not_colliding_axis_aligned_boxes(self):
        box1 = CollisionablePolygonExample([Point2D(0, 1), Point2D(1, 1), Point2D(1, 0), Point2D(0, 0)])
        box2 = CollisionablePolygonExample([Point2D(1.02, 1), Point2D(2.02, 1), Point2D(2.02, 0), Point2D(1.02, 0)])
        self.assertFalse(CollisionDetection.are_colliding(box1, box2))

    def test_touching_axis_aligned_boxes(self):
        box1 = CollisionablePolygonExample([Point2D(0, 1), Point2D(1, 1), Point2D(1, 0), Point2D(0, 0)])
        box2 = CollisionablePolygonExample([Point2D(1, 1), Point2D(2, 1), Point2D(2, 0), Point2D(1, 0)])
        self.assertTrue(CollisionDetection.are_colliding(box1, box2))

    def test_partially_overlapping_axis_aligned_boxes(self):
        box1 = CollisionablePolygonExample([Point2D(0, 1), Point2D(1, 1), Point2D(1, 0), Point2D(0, 0)])
        box2 = CollisionablePolygonExample([Point2D(0.5, 1), Point2D(2.5, 1), Point2D(2.5, 0), Point2D(1.5, 0)])
        self.assertTrue(CollisionDetection.are_colliding(box1, box2))

    def test_fully_overlapping_axis_aligned_boxes(self):
        box1 = CollisionablePolygonExample([Point2D(0, 1), Point2D(1, 1), Point2D(1, 0), Point2D(0, 0)])
        box2 = CollisionablePolygonExample([Point2D(0, 1), Point2D(1, 1), Point2D(1, 0), Point2D(0, 0)])
        self.assertTrue(CollisionDetection.are_colliding(box1, box2))

    def test_touching_oriented_boxes(self):
        box1 = CollisionablePolygonExample([Point2D(-1, 1), Point2D(0, 2), Point2D(1, 1), Point2D(0, 0)])
        box2 = CollisionablePolygonExample([Point2D(-1, -1), Point2D(0, 0), Point2D(1, -1), Point2D(0, -2)])
        self.assertTrue(CollisionDetection.are_colliding(box1, box2))

    def test_partially_overlapping_oriented_boxes(self):
        box1 = CollisionablePolygonExample([Point2D(-1, 1), Point2D(0, 2), Point2D(1, 1), Point2D(0, 0)])
        box2 = CollisionablePolygonExample([Point2D(-1, 1.5), Point2D(0, 2.5), Point2D(1, 1.5), Point2D(0, 0.5)])
        self.assertTrue(CollisionDetection.are_colliding(box1, box2))

    def test_fully_overlapping_oriented_boxes(self):
        box1 = CollisionablePolygonExample([Point2D(-1, 1), Point2D(0, 2), Point2D(1, 1), Point2D(0, 0)])
        box2 = CollisionablePolygonExample([Point2D(-1, 1), Point2D(0, 2), Point2D(1, 1), Point2D(0, 0)])
        self.assertTrue(CollisionDetection.are_colliding(box1, box2))

    def test_touching_oriented_vs_axis_aligned_boxes(self):
        box1 = CollisionablePolygonExample([Point2D(-1, 1), Point2D(0, 2), Point2D(1, 1), Point2D(0, 0)])
        box2 = CollisionablePolygonExample([Point2D(0.5, 0.5), Point2D(1, 0.5), Point2D(1, 0), Point2D(0.5, 0)])
        self.assertTrue(CollisionDetection.are_colliding(box1, box2))

    def test_falla(self):
        box1 = CollisionablePolygonExample([Point2D(15, 5), Point2D(15.0, 3.0),
                                            Point2D(24.43, -2.92), Point2D(25, -1)])
        box2 = CollisionablePolygonExample([Point2D(18.6, -0.5),
                                            Point2D(20.6, -0.5),
                                            Point2D(20.6, 0.5),
                                            Point2D(18.6, 0.5)])
        self.assertTrue(CollisionDetection.are_colliding(box1, box2))
        # [Point2D(18.599999999999994, -0.5), Point2D(20.599999999999994, -0.5), Point2D(20.599999999999994, 0.5), Point2D(18.599999999999994, 0.5)]
