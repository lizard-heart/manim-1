from manimlib.imports import *
import numpy as np


class Integral(GraphScene):
    CONFIG = {"y_max": 8, "y_axis_height": 5}

    def construct(self):
        self.show_function_graph()

    def show_function_graph(self):
        self.setup_axes(animate=True)

        def func(x):
            return x**2
        graph = self.get_graph(func, x_min=-5, x_max=5)
        graph.set_color(BLUE)
        self.play(ShowCreation(graph), run_time=3)
        self.wait(1)


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class FakeScene(Scene):
    def construct(self):
        ...
