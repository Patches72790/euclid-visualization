from math import sqrt
from manim import *
from manim.typing import Vector3D
import numpy as np


class EuclidPointWithLabel(AnnotationDot):
    def __init__(
        self,
        radius=0.05,
        stroke_width=5,
        stroke_color=GREEN,
        fill_color=GREEN,
        label="A",
        position: Vector3D = LEFT,
        font_size: int = 20,
        **kwargs
    ):
        super().__init__(radius, stroke_width, stroke_color, fill_color, **kwargs)

        self.label = Text(label, font_size=font_size).next_to(self, position)
        self.add(self.label)


class Book1Prop5(Scene):
    def construct(self):
        baseBC = Line(color=BLUE)
        lineAB = Line(color=PINK).put_start_and_end_on(
            np.array([-1, 0, 0]), np.array([0, 3 * np.sin(PI / 4), 0])
        )
        lineAC = Line(color=PURPLE).put_start_and_end_on(
            np.array([1, 0, 0]), np.array([0, 3 * np.sin(PI / 4), 0])
        )

        lineBD = Line(color=PINK).put_start_and_end_on(
            np.array([-1, 0, 0]), np.array([0, 3 * np.sin(PI / 4), 0])
        )
        lineCE = Line(color=PURPLE).put_start_and_end_on(
            np.array([1, 0, 0]), np.array([0, 3 * np.sin(PI / 4), 0])
        )

        pA = EuclidPointWithLabel(label="A").shift(LEFT * 1)
        pB = EuclidPointWithLabel(label="B", position=RIGHT).shift(RIGHT * 1)
        pC = EuclidPointWithLabel(label="C", position=UP).move_to(
            UP * (np.sqrt(1 + (3 * np.sin(PI / 4)) ** 2))
        )

        # sqrt(1 + (3*sin(pi/4))^2)

        self.add(baseBC, lineAB, lineAC, pA, pB, pC)
        self.wait(3)
