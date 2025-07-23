from manim import *

import numpy as np


class Book1Prop1Intro(Scene):
    def construct(self):
        c1 = Circle(radius=2).set_stroke(PINK)
        c2 = Circle(radius=2).set_stroke(BLUE)

        l1 = Line().set_stroke(ORANGE)
        l2 = Line(start=np.array([1, 0, 0]), end=np.array([-1, 0, 0])).set_stroke(GREEN)
        l3 = Line().set_stroke(PURPLE)

        self.play(FadeIn(c1, c2, l1, l2, l3), run_time=3)
        self.wait(1)
        self.play(
            l1.animate.put_start_and_end_on(
                np.array([-1, 0, 0]), np.array([0, 2 * np.sin(PI / 3), 0])
            ),
            l2.animate.put_start_and_end_on(
                np.array([1, 0, 0]), np.array([0, 2 * np.sin(PI / 3), 0])
            ),
            l3.animate.put_start_and_end_on(np.array([-1, 0, 0]), np.array([1, 0, 0])),
            c1.animate.shift(LEFT * 1),
            c2.animate.shift(RIGHT * 1),
            run_time=3,
        )

        lab_l1 = Text("A", font_size=24).move_to(c1.get_center()).shift(LEFT * 0.4)
        lab_l2 = Text("B", font_size=24).move_to(c2.get_center()).shift(RIGHT * 0.4)
        lab_l3 = Text("Γ", font_size=24).next_to(l3, UP * 8)

        lab_c1_del = Text("Δ", font_size=24).next_to(c1, LEFT)
        lab_c2_eps = Text("Ε", font_size=24).next_to(c2, RIGHT)

        lab_c1 = Text("ΒΓΔ", font_size=36).next_to(c1, DOWN)
        lab_c2 = Text("ΑΓΕ", font_size=36).next_to(c2, DOWN)

        title = Title("Euclid's Elements Proposition 1.1")

        detail = Text(
            "To construct an equilateral triangle on a given, finite, straight line",
            font_size=20,
        ).shift(DOWN * 3)

        labels = {
            l1: lab_l1,
            l2: lab_l2,
            l3: lab_l3,
            "c1_del": lab_c1_del,
            "c2_eps": lab_c2_eps,
            c1: lab_c1,
            c2: lab_c2,
        }

        # Bring in all labels
        self.play(
            *[
                Write(x)
                for x in (
                    lab_l1,
                    lab_l2,
                    lab_l3,
                    lab_c2_eps,
                    lab_c1_del,
                    lab_c1,
                    lab_c2,
                )
            ],
            Write(title),
            run_time=2
        )

        self.wait(1)

        self.play(Write(detail), run_time=3)

        self.wait(3)

        # Bring out everything but first circle DBC
        self.play(
            FadeOut(
                c2, l1, l2, l3, *[labels[x] for x in [c1, c2, l1, "c2_eps"]], detail
            ),
            rune_time=3,
        )

        self.wait(1)

        # Bring in radius AB of c1
        self.play(Write(l3), Write(labels[l1]), rune_time=2)

        self.wait(1)

        # Bring in c2 with radius BA
        self.play(
            Write(c2),
            Write(labels["c2_eps"]),
            run_time=2,
        )

        self.wait(1)

        # Bring back in other two radii
        self.play(Write(l1), Write(l2), run_time=2)

        self.wait(1)

        self.play(Write(detail), run_time=3)

        self.wait(3)
