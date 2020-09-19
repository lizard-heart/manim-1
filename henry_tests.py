from manimlib.imports import *
import numpy as np


class Integral(GraphScene):
    CONFIG = {"y_max": 8, "y_axis_height": 5}

    def construct(self):
        self.show_function_graph()

    def show_function_graph(self):
        self.setup_axes(animate=True)

        def func(x):
            return 0.1 * (x-2) * (x-8) * (x-5) + 5
        graph = self.get_graph(func, x_min=-5, x_max=10)
        graph.set_color(BLUE)
        self.play(ShowCreation(graph), run_time=3)
        self.wait(1)
        kwargs = {
            "x_min": 2,
            "x_max": 8,
            "fill_opacity": 0.9,
            "stroke_width": 0.2
        }
        # self.graph = graph
        iterations = 6
        self.rect_list = self.get_riemann_rectangles_list(
            graph, iterations, start_color=PURPLE, end_color=ORANGE, **kwargs)
        flat_rects = self.get_riemann_rectangles(self.get_graph(
            lambda x: 0), dx=0.5, start_color=invert_color(PURPLE), end_color=invert_color(ORANGE), **kwargs)
        rects = self.rect_list[0]
        self.transform_between_riemann_rects(
            flat_rects, rects, replace_mobject_with_target_in_scene=True, run_time=2)

        for j in range(1, 5):
            self.transform_between_riemann_rects(
                self.rect_list[j-1], self.rect_list[j], dx=1, replace_mobject_with_target_in_scene=True, run_time=2)


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
