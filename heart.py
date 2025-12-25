from manim import *
import numpy as np


TEXTS = [
    "A đi tắm xíu đã nha",
    "Iu Thảo\nrất nhèoooo",
    "Thảo công túa\ncute nhất thế giớiii",
    "Chúc Thảo thi tốt",
    "Chủ Nhật a đưa\nđi ăn lẩu nhaa"
]


class Heart(Scene):
    def construct(self):
        heart = ParametricFunction(
            lambda t: np.array([16 * np.sin(t) ** 3, 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t), 0]) / 4.5,  # scale down
            t_range=[0, TAU],
            stroke_width=6,
            color=RED,
        )
        heart.shift(UP * 0.5)

        # heart.scale(2)
        # heart.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        self.play(Create(heart), run_time=2)

        for txt in TEXTS:
            sub_texts = txt.split("\n")
            texts = VGroup(*[Text(text, gradient=(RED, PINK, WHITE)) for text in sub_texts]).arrange(DOWN).shift(UP * 0.5)
            self.play(Write(texts), run_time=3)
            self.wait()
            self.play(Unwrite(texts), run_time=3)

        self.play(Uncreate(heart), run_time=2)
        self.wait()
