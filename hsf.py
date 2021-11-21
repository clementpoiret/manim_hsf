from manim import *
from manim_editor import PresentationSectionType


class BaseHsf(Scene):

    def construct(self):
        logo = SVGMobject("assets/images/hsf.svg").scale(0.2).to_corner(UL)
        authorship = Text(
            "C. Poiret, A. Bouyeure, S. Patil, E. Duchesnay, A. Grigis, M. Noulhiane",
            weight="THIN",
            font="Open Sans")
        affiliations = Text("CEA Saclay | NeuroSpin | UNIACT/Inserm U1141",
                            weight="THIN",
                            font="Open Sans")

        self.add(logo.move_to(LEFT * 6.6 + UP * 3.6),
                 authorship.scale(0.25).next_to(logo, RIGHT * 0.5),
                 affiliations.scale(0.25).move_to(DOWN * 3.6 + LEFT * 5))


class Introduction(Scene):

    def construct(self):
        logo = SVGMobject("assets/images/hsf.svg").scale(0.2)
        hsf = Text("HSF", font="Open Sans")
        hippocampal = Text("Hippocampal", weight=BOLD, font="Open Sans")
        segmentation = Text("Segmentation", slant=ITALIC, font="Open Sans")
        factory = Text("Factory", weight="LIGHT", font="Open Sans")
        authorship = Text(
            "C. Poiret, A. Bouyeure, S. Patil, E. Duchesnay, A. Grigis, M. Noulhiane",
            weight="THIN",
            font="Open Sans")
        affiliations = Text("CEA Saclay | NeuroSpin | UNIACT/Inserm U1141",
                            weight="THIN",
                            font="Open Sans")

        self.next_section("Intro", PresentationSectionType.NORMAL)
        self.add(hsf)
        self.add(logo.move_to(LEFT * 6.6 + UP * 3.6))
        self.add(affiliations.scale(0.25).move_to(DOWN * 3.6 + LEFT * 5))
        self.wait(2)

        self.next_section("Intro.1", PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(hsf))
        self.play(Write(hippocampal.move_to(UP * 2)),
                  Write(segmentation.next_to(hippocampal, DOWN)),
                  Write(factory.next_to(segmentation, DOWN)),
                  FadeIn(authorship.scale(0.5).next_to(factory, DOWN)))
        self.wait(2)

        self.next_section("Intro.End", PresentationSectionType.SUB_SKIP)
        self.play(FadeOut(hippocampal, segmentation, factory),
                  authorship.animate.scale(0.5).next_to(logo, RIGHT * 0.5))

        # tex = MathTex(r"f(x) &= 5 + 1 + 1\\ &= 6 + 1\\ &= 7", font_size=122)

        # circle = Circle()  # create a circle
        # circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        # square = Square()  # create a square
        # square.rotate(PI / 4)  # rotate a certain amount

        # self.next_section("A", PresentationSectionType.NORMAL)
        # self.play(Create(square))  # animate the creation of the square

        # self.next_section("B", PresentationSectionType.NORMAL)
        # self.play(Transform(square,
        #                     circle))  # interpolate the square into the circle

        # self.next_section("C", PresentationSectionType.NORMAL)
        # self.play(FadeOut(square))  # fade out animation

        # self.next_section("D", PresentationSectionType.NORMAL)
        # self.play(Write(tex))  # animate the creation of the tex

        # self.next_section("E", PresentationSectionType.NORMAL)
        # self.play(FadeOut(tex))  # fade out animation


class StateOfNeed(BaseHsf):

    def construct(self):
        super().construct()

        title = Text("State of Need", font="Open Sans")

        self.next_section("StateOfNeed", PresentationSectionType.NORMAL)

        self.play(FadeIn(title))
        self.play(title.animate.scale(0.75).move_to(UP * 3))
        self.wait(2)

        self.next_section("StateOfNeed.End", PresentationSectionType.SUB_SKIP)
        self.play(FadeOut(title))


class Preprocessing(ZoomedScene):

    def __init__(self, **kwargs):
        ZoomedScene.__init__(self,
                             zoom_factor=0.3,
                             zoomed_display_height=1.5,
                             zoomed_display_width=3.5,
                             image_frame_stroke_width=20,
                             zoomed_camera_config={
                                 "default_frame_stroke_width": 3,
                             },
                             **kwargs)

    def construct(self):
        logo = SVGMobject("assets/images/hsf.svg").scale(0.2).to_corner(UL)
        authorship = Text(
            "C. Poiret, A. Bouyeure, S. Patil, E. Duchesnay, A. Grigis, M. Noulhiane",
            weight="THIN",
            font="Open Sans")
        affiliations = Text("CEA Saclay | NeuroSpin | UNIACT/Inserm U1141",
                            weight="THIN",
                            font="Open Sans")

        self.add(logo.move_to(LEFT * 6.6 + UP * 3.6),
                 authorship.scale(0.25).next_to(logo, RIGHT * 0.5),
                 affiliations.scale(0.25).move_to(DOWN * 3.6 + LEFT * 5))

        title = Text("Preprocessing", font="Open Sans")
        subtitle = Text("ROILoc", slant=ITALIC, weight=LIGHT,
                        font="Open Sans").scale(0.4)

        self.next_section("Preprocessing", PresentationSectionType.NORMAL)
        self.play(FadeIn(title))
        self.play(title.animate.scale(0.75).move_to(UP * 3))
        self.play(FadeIn(subtitle.next_to(title, DOWN)))
        self.wait(2)

        self.next_section("Preprocessing.1", PresentationSectionType.SUB_NORMAL)
        t2w = ImageMobject("assets/images/t2w.png").scale(0.4).move_to(LEFT * 4)
        self.play(FadeIn(t2w))
        self.wait(2)

        self.next_section("Preprocessing.2", PresentationSectionType.SUB_NORMAL)
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(5 * LEFT + 0.6 * UP)
        frame.set_color(WHITE)
        zoomed_display_frame.set_color(WHITE)
        self.wait(2)

        zoomed_display.move_to(UP)

        zd_rect = BackgroundRectangle(zoomed_display,
                                      fill_opacity=0,
                                      buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)

        unfold_camera = UpdateFromFunc(
            zd_rect, lambda rect: rect.replace(zoomed_display))

        self.play(Create(frame))
        self.activate_zooming()

        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)
        self.wait(1)
        hr = MathTex("H_r").set_color(RED).move_to(zoomed_display)
        self.play(FadeIn(hr), frame.animate.shift(1.9 * RIGHT),
                  zoomed_display.animate.move_to(DOWN))
        self.wait(1)
        hl = MathTex("H_l").set_color(PURPLE).move_to(zoomed_display)
        self.play(FadeIn(hl))
        self.play(self.get_zoomed_display_pop_out_animation(),
                  unfold_camera,
                  rate_func=lambda t: smooth(1 - t))
        self.play(Uncreate(zoomed_display_frame), FadeOut(frame), FadeOut(t2w))
        self.play(hr.animate.move_to(0.5 * UP + 4 * LEFT),
                  hl.animate.move_to(0.5 * DOWN + 4 * LEFT))
        self.wait(1)

        hippocampi = VGroup(hr, hl)
        self.play(Circumscribe(hippocampi, color=WHITE))

        self.next_section("Preprocessing.End", PresentationSectionType.SUB_SKIP)
        self.play(FadeOut(title, subtitle, hippocampi))


class Segmentation(BaseHsf):

    def construct(self):
        super().construct()

        title = Text("Segmentation", font="Open Sans")
        subtitle = Text(
            "Many Models as Independant Lies (Lu Hong & Scott Page)",
            slant=ITALIC,
            weight=LIGHT,
            font="Open Sans").scale(0.4)

        self.next_section("Segmentation", PresentationSectionType.NORMAL)

        self.play(FadeIn(title))
        self.play(title.animate.scale(0.75).move_to(UP * 3))
        self.play(FadeIn(subtitle.next_to(title, DOWN)))
        self.wait(2)

        # Condorcet Jury Theorem
        self.next_section("Segmentation.2", PresentationSectionType.SUB_NORMAL)
        cj = Text("Condorcet Jury Theorem", font="Open Sans")
        cj_desc = Text("""
A majority vote classifies correctly with
higher probability than any person (model),
and as the number of people (models)
becomes large, the accuracy of the
majority vote approaches 100%.""",
                       font="Open Sans",
                       weight=LIGHT).scale(0.4)

        self.play(FadeIn(cj))
        self.play(cj.animate.scale(0.5).move_to(UP + LEFT * 4))
        self.play(FadeIn(cj_desc.next_to(cj, DOWN).shift(RIGHT * 0.15)))
        self.wait(2)

        # Diversity Prediction Theorem
        self.next_section("Segmentation.3", PresentationSectionType.SUB_NORMAL)
        dp = Text("Diversity Prediction Theorem",
                  font="Open Sans").scale(0.5).move_to(UP + RIGHT * 4)
        self.play(FadeOut(cj, cj_desc))
        dp_theorem_0 = MathTex(r"(\bar{M} - V)^2")
        dp_theorem_eq = MathTex(r"=")
        dp_theorem_1 = MathTex(r"\sum_{i=1}^{N}{\frac{(M_i-V)^2}{N}")
        dp_theorem_minus = MathTex(r"-")
        dp_theorem_2 = MathTex(r"\sum_{i=1}^{N}{\frac{(M_i-\bar{M})^2}{N}}}")
        dp_theorem_eq.next_to(dp_theorem_0, RIGHT)
        dp_theorem_1.next_to(dp_theorem_eq, RIGHT)
        dp_theorem_minus.next_to(dp_theorem_1, RIGHT)
        dp_theorem_2.next_to(dp_theorem_minus, RIGHT)

        dp_theorem = VGroup(dp_theorem_0, dp_theorem_eq, dp_theorem_1,
                            dp_theorem_minus, dp_theorem_2).move_to(ORIGIN)

        dp_sub = Tex(
            r"where $M_i$ equals model $i$'s prediction,\\$\bar{M}$ equals the average of the model's values\\and V equals the true value."
        ).scale(0.75)
        self.play(Write(dp_theorem))

        brace_0 = Brace(dp_theorem_0, UP)
        eq_text_0 = brace_0.get_text("Many-Model Error").scale(0.65)
        brace_1 = Brace(dp_theorem_1, UP)
        eq_text_1 = brace_1.get_text("Average-Model Error").scale(0.65)
        brace_2 = Brace(dp_theorem_2, UP)
        eq_text_2 = brace_2.get_text("Diversity of Model Prediction").scale(
            0.65)

        self.play(GrowFromCenter(brace_0), FadeIn(eq_text_0))
        self.play(GrowFromCenter(brace_1), FadeIn(eq_text_1))
        self.play(GrowFromCenter(brace_2), FadeIn(eq_text_2))

        self.play(FadeIn(dp_sub.next_to(dp_theorem, DOWN)))
        self.wait(2)

        self.next_section("Segmentation.4", PresentationSectionType.SUB_NORMAL)
        line = Line(UP * 0.5, DOWN * 0.5)
        dp_all = VGroup(dp_theorem, dp_sub, brace_0, eq_text_0, brace_1,
                        eq_text_1, brace_2, eq_text_2)
        self.play(FadeIn(dp), dp_all.animate.scale(0.5).next_to(dp, DOWN))
        self.play(Create(line), FadeIn(cj, cj_desc))
        self.wait(2)

        self.next_section("Segmentation.End", PresentationSectionType.SUB_SKIP)
        self.play(FadeOut(title, subtitle, dp, dp_all, line, cj, cj_desc))


class BaggingTta(BaseHsf):

    def construct(self):
        super().construct()

        self.next_section("BaggingTta", PresentationSectionType.NORMAL)
        tta = Text("Test-Time Augmentation", font="Open Sans")
        self.play(FadeIn(tta))
        self.play(Circumscribe(tta, color=WHITE))
        self.wait()

        self.next_section("BaggingTta.1", PresentationSectionType.SUB_NORMAL)
        mri = Text("This is an MRI", font="Open Sans").scale(0.75)
        mri.to_corner(UP + LEFT)
        mri.shift(DOWN)
        self.play(Transform(tta, mri))

        grid = NumberPlane()
        affine = Text("Affine Transformations", font="Open Sans").scale(0.5)
        affine.move_to(mri).shift(DOWN * 0.6)
        affine.align_to(mri, LEFT)

        self.add(grid)  # Make sure title is on top of grid
        self.play(Create(grid, run_time=3, lag_ratio=0.1))

        self.next_section("BaggingTta.2", PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(affine),
                  grid.animate.scale(1.5).shift(UP * 0.3 + LEFT * 0.4).rotate(
                      PI / 6),
                  run_time=3)
        self.wait()

        self.next_section("BaggingTta.3", PresentationSectionType.SUB_NORMAL)
        elastic = Text("Elastic Transformations", font="Open Sans").scale(0.5)
        elastic.move_to(affine, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            Transform(affine, elastic),
            grid.animate.apply_function(lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ])),
            run_time=3,
        )
        self.wait(2)

        self.next_section("BaggingTta.End", PresentationSectionType.SUB_SKIP)
        self.play(FadeOut(tta, affine, grid))


class Postprocessing(BaseHsf):

    def construct(self):
        super().construct()

        title = Text("Postprocessing", font="Open Sans")
        subtitle = Text("Aleatoric Uncertainty",
                        slant=ITALIC,
                        weight=LIGHT,
                        font="Open Sans").scale(0.4)

        self.next_section("Postprocessing", PresentationSectionType.NORMAL)

        self.play(FadeIn(title))
        self.play(title.animate.scale(0.75).move_to(UP * 3))
        self.play(FadeIn(subtitle.next_to(title, DOWN)))
        self.wait(2)

        self.next_section("Postprocessing.End",
                          PresentationSectionType.SUB_SKIP)
        self.play(FadeOut(title, subtitle))


class PreliminaryResults(BaseHsf):

    def construct(self):
        super().construct()

        title = Text("Preliminary Results", font="Open Sans")
        subtitle = Text("From unseen cases",
                        slant=ITALIC,
                        weight=LIGHT,
                        font="Open Sans").scale(0.4)

        self.next_section("Results", PresentationSectionType.NORMAL)

        self.play(FadeIn(title))
        self.play(title.animate.scale(0.75).move_to(UP * 3))
        self.play(FadeIn(subtitle.next_to(title, DOWN)))
        self.wait(2)

        self.next_section("Results.End", PresentationSectionType.SUB_SKIP)
        self.play(FadeOut(title, subtitle))
