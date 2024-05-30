from manim import *
import numpy as np


class intro(Scene):
    def construct(self):
        t1 = MathTex(r"\text{A property}")
        t1.set_color_by_tex_to_color_map({"property": GREEN})
        t2 = MathTex(r"\text{of}")
        t3 = MathTex(r"\text{Analytic functions}")
        t3.set_color_by_tex_to_color_map({"Analytic": RED})
        t1.shift(UP)
        t1.scale(1.5)
        t3.shift(DOWN)
        t3.scale(1.7)

        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.wait(2)


class definition(Scene):
    def construct(self):
        t1 = MathTex(r"\text{Theorem:}")
        t1.set_color(GREEN)
        t1.to_edge(UP + LEFT)
        t2 = MathTex(r"\text{If f is}")
        t2.next_to(t1, DOWN, buff=0.5)
        t3 = MathTex(r"\text{analytic}")
        t3.set_color(RED)
        t3_dup = MathTex(r"\text{analytic}")
        t3.next_to(t2, RIGHT, buff=0.3)
        t3_dup.next_to(t2, RIGHT, buff=0.3)
        t4 = MathTex(r"\text{on a domain D, and if } \grave{f\left( z \right)} = 0 \ \forall \ z \in D")
        t4.next_to(t3, RIGHT, buff=0.3)
        t5 = MathTex(r"\text{then f is constant in D}")
        t5.next_to(t2, DOWN, buff=0.3)
        t5.shift(1.3 * RIGHT)
        r = Rectangle(height=2, width=14, fill_color=BLUE, fill_opacity=0.7, color=BLUE)
        r.shift(DOWN * 0.8)
        self.play(FadeIn(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Write(t4))
        self.play(Write(t5))
        self.wait(2)
        self.play(ReplacementTransform(t3_dup, r))
        self.wait(1)
        t6a = MathTex(
            r"f \text{ is said to be analytic in D if and only if }")
        t6a.scale(0.7)
        t6a.set_color(WHITE)
        t6a.shift(DOWN * 0.5)
        t6c = MathTex(
            r"u(x,y) \text{ and } v(x,y) \text{ have continuous first partial derivatives on D }")
        t6c.scale(0.7)
        t6c.set_color(WHITE)
        t6c.shift(DOWN * 1)
        t6b = MathTex(
            r"\text{and } u_{x} = v_{y} \text{ and } u_{y} = -v_{x} \text{ where } f(z) = u(x,y) + iv(x,y)")
        t6b.scale(0.7)
        t6b.set_color(WHITE)
        t6b.shift(DOWN * 1.5)
        self.add(t6a)
        self.add(t6c)
        self.add(t6b)
        self.wait(4)


class connection1(Scene):
    def construct(self):
        t1 = MathTex(r"\text{Let's analyse this }")
        factorial = MathTex(r"\text{!}")
        factorial.scale(2.5)
        factorial.next_to(t1, RIGHT)
        factorial.shift(UP*0.25)
        factorial.set_color(GREEN)
        t1.set_color_by_tex_to_color_map({"analyse": BLUE})
        self.play(Write(t1))
        self.play(Write(factorial))
        self.wait(2)


class pictorial(Scene):
    def construct(self):
        t1 = MathTex(r"\text{Consider some domain, D }")
        img = ImageMobject("amoeba.png")
        img.scale(3)
        img.shift(LEFT*3)
        self.play(Write(t1))
        self.wait(1)
        self.play(FadeOut(t1))
        self.play(FadeIn(img))
        t2 = MathTex(r"\text{Now consider some disc, } B_{ r }(a) \text{ inside D }")
        t2.scale(0.7)
        t3 = MathTex(r"\text{which represents a set of complex numbers, }")
        t3.scale(0.7)
        number = MathTex(r"|z-z_{ 0 }| \le r ")
        number.scale(1.5)
        t2.shift(3.5 * RIGHT + 2 * UP)
        t3.shift(3.5 * RIGHT + 2 * UP)
        number.shift(4 * RIGHT + 2 * UP)
        self.play(Write(t2))
        self.wait(1.5)
        self.play(ReplacementTransform(t2, t3))
        self.wait(1.5)
        self.play(ReplacementTransform(t3, number))
        self.wait(2)
        center = Dot(color=BLACK, radius=0.03)
        center.shift(2.5 * LEFT)
        line = DashedLine(start=LEFT * 2.5, end=LEFT * 2.1, color=BLACK)
        line.scale(0.7)
        r = MathTex("r")
        r.scale(0.4)
        r.shift(LEFT * 2.3 + UP * 0.1)
        c1 = Circle(radius=0.4, fill_color=PURPLE_E, fill_opacity=0.7, color=PURPLE_E)
        c2 = Circle(radius=1.7, fill_color=PURPLE_E, fill_opacity=0.7, color=PURPLE_E)
        c2.shift(3 * RIGHT)
        c1.shift(2.5 * LEFT)
        self.play(ReplacementTransform(number, c1))
        self.play(Write(center), Create(line))
        self.play(Write(r))
        self.wait(2)

        self.play(FadeOut(line), FadeOut(center), FadeOut(r))
        an = MathTex("a")
        an.scale(0.5)
        an.shift(2.8 * RIGHT)
        self.play(ReplacementTransform(c1, c2))
        center.move_to(3 * RIGHT)
        self.add(center)
        self.play(Write(an))
        self.wait(1.2)

        t4 = MathTex(r"\text{Let c } \in B_{ r }(a) ")
        t4.shift(2.5 * DOWN + 3.3 * RIGHT)
        t4.scale(0.7)
        self.play(Write(t4))
        self.wait(0.2)
        c = Dot(radius=0.03, color=BLACK)
        c.shift(3.9 * RIGHT + UP)
        cn = MathTex(r"c")
        cn.scale(0.5)
        cn.shift(RIGHT * 3.9 + UP * 1.2)
        self.play(Write(c))
        self.play(Write(cn))
        self.wait(1)

        t5 = MathTex(r"\text{Now pick a point b } \in B_{ r }(a) \text{ as shown }")
        t5.shift(2.5 * DOWN + 3.3 * RIGHT)
        t5.scale(0.7)
        b = Dot(radius=0.03, color=BLACK)
        b.shift(3.9 * RIGHT)
        bn = MathTex(r"\text{b }")
        bn.scale(0.5)
        bn.shift(RIGHT * 3.9 + DOWN * 0.2)

        self.play(ReplacementTransform(t4, t5))
        self.play(Write(b))
        self.play(Write(bn))
        self.wait(1)

        dl1 = DashedLine(start=RIGHT * 3, end=RIGHT * 3.9, color=BLACK)
        dl2 = DashedLine(start=RIGHT * 3.9, end=RIGHT * 3.9 + UP, color=BLACK)
        self.play(Write(dl1), Write(dl2))
        self.wait(0.5)

        t6 = MathTex(r"\text{Since given } \grave { f\left( z \right)  } \text{=0 }, ")
        t7 = MathTex(r"u_{ x }=u_{ y }=v_{ x }=v_{ y } \text{=0 }")
        t8 = MathTex(r"u_{ y }=v_{ y }=0 \text{ implies u(b)=u(c) and v(b)=v(c) }")
        t9 = MathTex(r"\text{and } u_{ x }=v_{ x }=0 \text{ implies u(a)=u(b) and v(a)=v(b) }")
        t9a = MathTex(r"\text{(i.e. a,b,c are coincident) }")
        t6.scale(0.7)
        t7.scale(0.7)
        t8.scale(0.7)
        t9.scale(0.7)
        t9a.scale(0.7)
        t6.shift(2.5 * DOWN + 3.3 * RIGHT)
        t7.shift(2.5 * DOWN + 3.3 * RIGHT)
        t8.shift(2.5 * DOWN + 3.3 * RIGHT)
        t9.shift(2.5 * DOWN + 3.3 * RIGHT)
        t9a.shift(2.3 * UP + 3.3 * RIGHT)
        self.play(ReplacementTransform(t5, t6))
        self.wait(1.5)
        self.play(ReplacementTransform(t6, t7))
        self.wait(1.5)
        self.play(ReplacementTransform(t7, t8))
        self.wait(1.5)
        self.play(FadeOut(dl2))
        self.play(ApplyMethod(c.shift, DOWN), ApplyMethod(cn.shift, DOWN))
        self.wait(1)
        self.play(ReplacementTransform(t8, t9))
        self.play(FadeOut(dl1))
        self.play(ApplyMethod(b.shift, LEFT * 0.9), ApplyMethod(c.shift, LEFT * 0.9), ApplyMethod(bn.shift, LEFT * 0.9),
                  ApplyMethod(cn.shift, LEFT * 0.9))
        self.wait(1)
        self.play(Write(t9a))
        self.wait(1.4)

        self.play(FadeOut(t9a))
        t10 = MathTex(r"\text{Since c was an arbitrary point in } B_{ r }(a) ")
        t11 = MathTex(r"\text{Thus u and v are constant in } B_{ r }(a) ")
        t12 = MathTex(r"\text{ therefore f is constant in } B_{ r }(a) ")
        t10.scale(0.7)
        t11.scale(0.7)
        t12.scale(0.7)
        t10.shift(2.5 * DOWN + 3.3 * RIGHT)
        t11.shift(2.5 * DOWN + 3.3 * RIGHT)
        t12.shift(2.5 * DOWN + 3.3 * RIGHT)
        self.play(ReplacementTransform(t9, t10))
        self.wait(1.5)
        self.play(ReplacementTransform(t10, t11))
        self.wait(1.5)
        self.play(ReplacementTransform(t11, t12))
        self.wait(2)
        self.play(FadeOut(t12), FadeOut(center), FadeOut(an), FadeOut(c), FadeOut(cn), FadeOut(b), FadeOut(bn))
        self.wait(0.4)
        c1 = Circle(radius=0.4, fill_color=PURPLE_E, fill_opacity=0.7, color=PURPLE_E)
        c1.shift(2.5 * LEFT)
        self.play(ReplacementTransform(c2, c1))
        self.wait(1)

        t13 = MathTex(r"\text{Now let b } \notin B_{ r }(a) \text{ and be an arbitrary point in D }")
        t13.scale(0.7)
        t13.shift(2 * UP + 3.3 * RIGHT)
        c3 = Circle(radius=0.4, fill_color=GREEN_E, fill_opacity=0.7, color=GREEN_E)
        c3.shift(2 * LEFT + UP)
        a = Dot(color=BLACK, radius=0.03)
        an = MathTex(r"\text{a}")
        b = Dot(color=BLACK, radius=0.03)
        bn = MathTex(r"\text{b}")
        an.scale(0.4)
        bn.scale(0.4)
        a.shift(3.5 * LEFT + DOWN)
        an.shift(3.5 * LEFT + DOWN * 0.8)
        b.shift(2 * LEFT + UP)
        bn.shift(2 * LEFT + 1.2 * UP)
        self.play(Write(t13))
        self.play(ApplyMethod(c1.shift, LEFT + DOWN))
        self.play(Write(a), Write(an))
        self.play(Write(c3))
        self.play(Write(b), Write(bn))
        self.wait(1.4)

        t14 = MathTex(r"\text{Since D is connected, } \exists \text{ some curve connecting a and b }")
        t14.scale(0.7)
        t14.shift(2 * UP + 2.9 * RIGHT)
        arc = ArcBetweenPoints(start=3.5 * LEFT + DOWN, end=2 * LEFT + UP, angle=TAU / 6, color=DARK_BROWN)
        self.play(ReplacementTransform(t13, t14))
        self.wait(0.5)
        self.play(Create(arc))
        self.wait(1.5)

        t15 = MathTex(r"\text{ therefore we can draw discs along the same curve }")
        t15.scale(0.7)
        t15.shift(2 * UP + 3.1 * RIGHT)
        circles = [0, 0, 0, 0]
        circles_dup = [0, 0, 0, 0]
        circles[0] = Circle(radius=0.34, color=BLUE)
        circles[1] = Circle(radius=0.24, color=YELLOW)
        circles[2] = Circle(radius=0.3, color=GREEN)
        circles[3] = Circle(radius=0.35, color=RED)
        circles[0].shift(2.9 * LEFT + 0.7 * DOWN)
        circles[1].shift(2.65 * LEFT + 0.3 * DOWN)
        circles[2].shift(2.3 * LEFT)
        circles[3].shift(2 * LEFT + 0.4 * UP)

        c1_dup = Circle(radius=0.4, color=WHITE)
        c1_dup.shift(3.5 * LEFT + DOWN)
        circles_dup[0] = Circle(radius=0.34, color=WHITE)
        circles_dup[1] = Circle(radius=0.24, color=WHITE)
        circles_dup[2] = Circle(radius=0.3, color=WHITE)
        circles_dup[3] = Circle(radius=0.35, color=WHITE)
        circles_dup[0].shift(2.9 * LEFT + 0.7 * DOWN)
        circles_dup[1].shift(2.65 * LEFT + 0.3 * DOWN)
        circles_dup[2].shift(2.3 * LEFT)
        circles_dup[3].shift(2 * LEFT + 0.4 * UP)
        c3_dup = Circle(radius=0.4, color=WHITE)
        c3_dup.shift(2 * LEFT + UP)

        self.play(ReplacementTransform(t14, t15))
        self.play(Write(circles[0]))
        self.play(Write(circles[1]))
        self.play(Write(circles[2]))
        self.play(Write(circles[3]))
        self.wait(1)

        t16 = MathTex(r"\text{Since f is constant in the disc }")
        t17 = MathTex(r"\text{around the point 'a', similarly f should be constant }")
        t18 = MathTex(r"\text{in it's neighbouring disk and so on. }")
        # t19=TextMobject("Since the two disks overlap, the two constants must be equal.Similarly if we continue,we reach disc b. $\\therefore$ we get f(a)=f(b).Thus f is constant in D")
        t19 = MathTex(r"\text{Since the two discs overlap, }")
        t20 = MathTex(r"\text{the two constants must be equal }")
        t21 = MathTex(r"\text{Similarly if we continue,we reach disc b }")
        t22 = MathTex(r"\text{therefore we get f(a)=f(b) }")
        t23 = MathTex(r"\text{Thus f is constant in D }")
        t16.scale(0.7)
        t17.scale(0.7)
        t18.scale(0.7)
        t19.scale(0.7)
        t20.scale(0.7)
        t21.scale(0.7)
        t22.scale(0.7)
        t23.scale(0.7)
        t16.shift(2 * UP + 3.15 * RIGHT)
        t17.next_to(t16, DOWN, buff=0.3)
        t18.next_to(t17, DOWN, buff=0.3)
        g1 = VGroup(t16, t17, t18)
        g2 = VGroup(t19, t20, t21)
        self.play(ReplacementTransform(t15, t16))
        self.play(Write(t17))
        self.play(Write(t18))
        self.wait(1.4)

        self.play(FadeOut(g1))
        t19.shift(2 * UP + 3.15 * RIGHT)
        self.play(Write(t19), FadeIn(c1_dup), FadeIn(circles_dup[0]))
        t20.next_to(t19, DOWN, buff=0.3)
        self.play(Write(t20))
        t21.next_to(t20, DOWN, buff=0.3)
        self.play(FadeOut(c1_dup), FadeOut(circles_dup[0]))
        self.play(Write(t21))
        self.play(FadeIn(c1_dup))
        self.play(FadeIn(circles_dup[0]))
        self.play(FadeIn(circles_dup[1]))
        self.play(FadeIn(circles_dup[2]))
        self.play(FadeIn(circles_dup[3]))
        self.play(FadeIn(c3_dup))
        self.wait(0.7)
        self.play(FadeOut(circles_dup[0]), FadeOut(circles_dup[1]), FadeOut(circles_dup[2]), FadeOut(circles_dup[3]))
        self.wait(1.4)

        self.play(FadeOut(g2), FadeOut(c1_dup), FadeOut(c3_dup))
        t22.shift(2 * UP + 3.15 * RIGHT)
        self.play(Write(t22))
        self.wait(1)
        t23.shift(2 * UP + 3.15 * RIGHT)
        t23.scale(1.3)
        self.play(ReplacementTransform(t22, t23))
        self.wait(1)

        self.play(FadeOut(circles[0]), FadeOut(circles[1]), FadeOut(circles[2]), FadeOut(circles[3]))
        self.play(FadeOut(arc))
        self.play(ApplyMethod(c3.shift, 1.5 * LEFT + 2 * DOWN), ApplyMethod(bn.shift, 1.35 * LEFT + 1.95 * DOWN),
                  ApplyMethod(b.shift, 1.5 * LEFT + 2 * DOWN))
        self.wait(2)


class conclusion(Scene):
    def construct(self):
        t1 = MathTex(r"\text{Hence the property is satisfied }")
        t2 = MathTex(r"\forall \text{ z } \in \text{ D }")
        t1.shift(UP)
        t2.next_to(t1, DOWN, buff=0.4)
        t1.set_color_by_tex_to_color_map({"property ": BLUE, "satisfied ": YELLOW})
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(3)