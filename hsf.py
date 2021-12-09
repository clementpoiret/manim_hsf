import imageio
import numpy as np
from manim import *
from manim_editor import PresentationSectionType


class BaseHsf(Scene):

    def construct(self):
        logo = SVGMobject("assets/images/hsf.svg").scale(0.2).to_corner(UL)
        authorship = Text(
            "C. Poiret, A. Bouyeure, S. Patil, E. Duchesnay, A. Grigis, F. Lemaître, M. Noulhiane",
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
        cea = SVGMobject("assets/logos/cea.svg").scale(0.3).move_to(DOWN * 1 +
                                                                    LEFT * 4.8)
        neurospin = ImageMobject("assets/logos/neurospin.png").scale(
            0.8).next_to(cea, RIGHT)
        ups = ImageMobject("assets/logos/ups.png").scale(0.08).next_to(
            neurospin, RIGHT)
        up = ImageMobject("assets/logos/up.png").scale(0.15).next_to(ups, RIGHT)
        idris = ImageMobject("assets/logos/idris.png").scale(0.5).next_to(
            up, RIGHT)
        genci = ImageMobject("assets/logos/genci.png").scale(0.20).next_to(
            idris, RIGHT)
        onnx = ImageMobject("assets/logos/onnx.png").scale(0.06).next_to(
            genci, RIGHT)
        neuralmagic = ImageMobject("assets/logos/neuralmagic.png").scale(
            0.15).next_to(onnx, RIGHT)
        self.add(cea, neurospin, ups, up, idris, genci, onnx, neuralmagic)

        logo = SVGMobject("assets/images/hsf.svg").scale(0.2)
        hsf = Text("HSF", font="Open Sans")
        subtitle = Text("as a Future-Proof Solution to",
                        font="Open Sans").next_to(hsf, RIGHT)
        title_1 = VGroup(hsf, subtitle)
        subsubtitle = Text("Hippocampal Subfields Segmentation in MRI",
                           font="Open Sans").next_to(title_1, DOWN)
        title = VGroup(title_1, subsubtitle).scale(0.75).move_to(ORIGIN + UP)

        hippocampal = Text("Hippocampal", weight=BOLD, font="Open Sans")
        segmentation = Text("Segmentation", slant=ITALIC,
                            font="Open Sans").next_to(hippocampal, DOWN)
        factory = Text("Factory", weight="LIGHT",
                       font="Open Sans").next_to(segmentation, DOWN)
        hsf_full = VGroup(hippocampal, segmentation, factory).move_to(ORIGIN)

        url = Text("https://hsf.rtfd.io/",
                   font="Open Sans",
                   color=BLUE,
                   slant=ITALIC).scale(0.5).next_to(hsf_full, DOWN)
        ul = Underline(url, buff=0, color=BLUE)

        authorship = Text(
            "C. Poiret, A. Bouyeure, S. Patil, E. Duchesnay, A. Grigis, F. Lemaître, M. Noulhiane",
            weight="THIN",
            font="Open Sans")
        affiliations = Text("CEA Saclay | NeuroSpin | UNIACT/Inserm U1141",
                            weight="THIN",
                            font="Open Sans")

        self.next_section("Intro", PresentationSectionType.NORMAL)
        self.add(title, logo.move_to(LEFT * 6.6 + UP * 3.6),
                 affiliations.scale(0.25).move_to(DOWN * 3.6 + LEFT * 5),
                 authorship.scale(0.5).next_to(title, DOWN))
        self.wait(4)

        self.next_section("Intro.1", PresentationSectionType.SUB_NORMAL)
        self.play(
            FadeOut(subtitle, subsubtitle),
            authorship.animate.scale(0.5).next_to(logo, RIGHT * 0.5),
            FadeOut(cea, neurospin, ups, up, idris, genci, onnx, neuralmagic))
        self.play(Transform(hsf, hsf_full), FadeIn(url, ul))
        self.wait(2)

        self.next_section("Intro.End", PresentationSectionType.SUB_SKIP)
        self.play(FadeOut(hsf, hsf_full, url, ul))


class StateOfNeed(BaseHsf):

    def construct(self):
        super().construct()

        title = Text("State of Need", font="Open Sans")
        subtitle = Text(
            "Segmenting Hippocampal Subfields in Heterogeneous Datasets",
            slant=ITALIC,
            weight=LIGHT,
            font="Open Sans").scale(0.4)

        self.next_section("StateOfNeed", PresentationSectionType.NORMAL)

        self.play(FadeIn(title))
        self.play(title.animate.scale(0.75).move_to(UP * 3))
        self.play(FadeIn(subtitle.next_to(title, DOWN)))
        self.wait(2)
        self.next_section("StateOfNeed.1", PresentationSectionType.SUB_NORMAL)

        freesurfer_title = Text(
            "FreeSurfer",
            font="Open Sans").to_edge(LEFT).scale(.6).shift(UP * 1.5 + RIGHT)
        self.play(FadeIn(freesurfer_title))

        fs_speed = Text("Speed: 8~12h /Subject", font="Open Sans",
                        weight=LIGHT).scale(0.4).next_to(
                            freesurfer_title, DOWN)
        fs_quality = Text("Quality: Far from manual",
                          font="Open Sans",
                          weight=LIGHT).scale(0.4).next_to(fs_speed, DOWN)
        self.play(FadeIn(fs_speed, fs_quality))

        fs = VGroup(freesurfer_title, fs_speed, fs_quality)
        self.wait(2)

        self.next_section("StateOfNeed.2", PresentationSectionType.SUB_NORMAL)
        ashs_title = Text(
            "ASHS",
            font="Open Sans").to_edge(RIGHT).scale(.6).shift(UP * 1.5 + LEFT)
        self.play(FadeIn(ashs_title))

        ashs_speed = Text("Speed: 1~2h /Subject",
                          font="Open Sans",
                          weight=LIGHT).scale(0.4).next_to(ashs_title, DOWN)
        ashs_quality = Text("Quality: Good but not generalizable",
                            font="Open Sans",
                            weight=LIGHT).scale(0.4).next_to(ashs_speed, DOWN)
        self.play(FadeIn(ashs_speed, ashs_quality))

        ashs = VGroup(ashs_title, ashs_speed, ashs_quality)
        self.wait(2)

        self.next_section("StateOfNeed.3", PresentationSectionType.SUB_NORMAL)
        deep_title = Text("Deep Learning",
                          font="Open Sans").scale(0.6).shift(UP * 1.5)
        deep_desc = Text(
            "Speed: ~1mn /Subject, but:\n1/ private implementation,\n2/ need to be trained,\n3/ lack of generalization.",
            font="Open Sans",
            weight=LIGHT).scale(0.4).next_to(deep_title, DOWN)

        self.play(fs.animate.scale(0.75), ashs.animate.scale(0.75),
                  FadeIn(deep_title))
        self.play(FadeIn(deep_desc))
        self.wait(2)

        self.next_section("StateOfNeed.4", PresentationSectionType.SUB_NORMAL)
        deep = VGroup(deep_title, deep_desc)
        line = Line(start=LEFT * 4, end=RIGHT * 4, color=WHITE)
        self.play(deep.animate.scale(0.75))
        self.play(
            fs.animate.scale(0.8).shift(.5 * UP),
            ashs.animate.scale(0.8).shift(.5 * UP),
            deep.animate.scale(0.8).shift(.5 * UP))
        self.play(Create(line.next_to(deep, DOWN)))

        hsf_title = Text("HSF", font="Open Sans").scale(0.75)
        affiliation = Text("HPE Jean-Zay Supercomputer (IDRIS/GENCI)",
                           font="Open Sans",
                           weight=LIGHT,
                           slant=ITALIC).scale(0.5).next_to(hsf_title,
                                                            RIGHT,
                                                            aligned_edge=DOWN)
        hsf = VGroup(hsf_title, affiliation).next_to(line, DOWN)
        self.play(FadeIn(hsf, affiliation))

        sota_impl = Text("SotA Implementation",
                         font="Open Sans").scale(0.5).next_to(hsf, DOWN).shift(
                             LEFT * 4)
        impl = Text("""1/ U-Net w/ self-attention (Oktay et al., 2018),
2/ AdamW w/ weight decay (Loshchilov, et al., 2017),
3/ Stochastic Weight Averaging (Izmailov, et al., 2019),
4/ SwitchNorm (Luo, et al., 2019),
5/ Pruning & int8 Quantization.
""",
                    font="Open Sans",
                    weight=LIGHT).scale(0.4).next_to(sota_impl,
                                                     DOWN).shift(.5 * RIGHT)
        self.play(FadeIn(sota_impl, impl))

        datasets = Text("12 Datasets", font="Open Sans").scale(0.5).next_to(
            hsf, DOWN).shift(RIGHT * 4)
        datadesc = Text("""Age: 4-80 years old,
Condition: Healthy, Epileptic, Sclerosis, MCI,
    Alzheimer's Disease, Post-Mortem,
Magnetic Field: 3T, 4T, 7T,
Contrast: T1w, 3D T2w, Coro T2w.
""",
                        font="Open Sans",
                        weight=LIGHT).scale(0.4).next_to(datasets, DOWN)

        self.play(FadeIn(datasets, datadesc))

        self.wait(4)

        self.next_section("StateOfNeed.End", PresentationSectionType.SUB_SKIP)
        self.play(
            FadeOut(title, subtitle, fs, ashs, deep_title, deep_desc, line, hsf,
                    sota_impl, impl, datasets, datadesc))


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
            "C. Poiret, A. Bouyeure, S. Patil, E. Duchesnay, A. Grigis, F. Lemaître, M. Noulhiane",
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
        self.wait(1)

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
        self.wait(1)

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
        self.wait(0.5)
        hr = MathTex("H_r").set_color(RED).move_to(zoomed_display)
        self.play(FadeIn(hr), frame.animate.shift(1.9 * RIGHT),
                  zoomed_display.animate.move_to(DOWN))
        self.wait(0.5)
        hl = MathTex("H_l").set_color(PURPLE).move_to(zoomed_display)
        self.play(FadeIn(hl))
        self.play(self.get_zoomed_display_pop_out_animation(),
                  unfold_camera,
                  rate_func=lambda t: smooth(1 - t))
        self.play(Uncreate(zoomed_display_frame), FadeOut(frame), FadeOut(t2w))
        self.play(hr.animate.move_to(0.5 * UP + 5 * LEFT),
                  hl.animate.move_to(0.5 * DOWN + 5 * LEFT))
        self.wait(0.5)

        self.next_section("Preprocessing.3", PresentationSectionType.SUB_NORMAL)
        hippocampi = VGroup(hr, hl)
        arrow_1 = Arrow(start=LEFT * 4.5, end=LEFT * 3)
        z_norm = Text("- Z-normalization\n- Shape .% 8 == 0",
                      font="Open Sans").scale(0.75)
        arrow_2 = Arrow(start=RIGHT, end=RIGHT * 2.5)
        segmentation = Text("Segmentation", font="Open Sans").scale(0.75)
        self.play(Circumscribe(hippocampi, color=WHITE))
        self.play(Create(arrow_1))
        self.play(FadeIn(z_norm.next_to(arrow_1, 1.5 * RIGHT)))
        self.play(Create(arrow_2))
        self.play(FadeIn(segmentation.next_to(arrow_2, 1.5 * RIGHT)))
        self.play(Circumscribe(segmentation, color=WHITE))
        self.wait(2)

        self.next_section("Preprocessing.End", PresentationSectionType.SUB_SKIP)
        self.play(
            FadeOut(title, subtitle, hippocampi, arrow_1, z_norm, arrow_2),
            segmentation.animate.scale(1.25).move_to(ORIGIN))


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

        self.add(title)
        self.play(title.animate.scale(0.75).move_to(UP * 3))
        self.play(FadeIn(subtitle.next_to(title, DOWN)))
        self.wait(2)

        # Condorcet Jury Theorem
        self.next_section("Segmentation.1", PresentationSectionType.SUB_NORMAL)
        cj_eq = Tex(
            r"$p_m = \sum_{i = \lceil m / 2 \rceil}^{m}{\left(\frac{m!}{(m-i)! \cdot i!}\right)} \cdot p^i \cdot (1-p)^{m-i}$"
        )
        cj = Text("Condorcet Jury Theorem", font="Open Sans").move_to(UP)
        cj_desc_1 = Tex(r"""If there are $m$ voters that\\
decide by simple majority voting, and each\\
voter has the probability $p$ of making the\\
right decision, then the probability of the\\
entire jury of making the right decision is:\\""").scale(0.4)
        cj_desc_2 = Tex(r"""Thus, if $p > 0.5$ then $p_m > p$. This means\\
that the ensemble has a higher probability\\
of making the correct decision than any\\
individual voter. When the number of voters\\
increases, the probability of the ensemble to\\
make the right decision also increases. Ideally,\\
when $m \rightarrow \infty$, $p_m \rightarrow 1$.\\""").scale(0.4)

        self.play(FadeIn(cj), Write(cj_eq))

        self.next_section("Segmentation.2", PresentationSectionType.SUB_NORMAL)
        self.play(
            cj.animate.scale(0.5).move_to(UP + LEFT * 4),
            cj_eq.animate.scale(0.5).move_to(LEFT * 4 + DOWN))

        self.play(FadeIn(cj_desc_1.next_to(cj_eq, UP)),
                  FadeIn(cj_desc_2.next_to(cj_eq, DOWN)))
        self.wait(2)

        # Diversity Prediction Theorem
        self.next_section("Segmentation.3", PresentationSectionType.SUB_NORMAL)
        dp = Text("Diversity Prediction Theorem",
                  font="Open Sans").scale(0.5).move_to(UP + RIGHT * 4)
        self.play(FadeOut(cj, cj_desc_1, cj_desc_2, cj_eq))
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
        self.play(Create(line), FadeIn(cj, cj_desc_1, cj_desc_2, cj_eq))
        self.wait(2)

        self.next_section("Segmentation.End", PresentationSectionType.SUB_SKIP)
        self.play(
            FadeOut(title, subtitle, dp, dp_all, line, cj, cj_desc_1, cj_desc_2,
                    cj_eq))


class BayesError(MovingCameraScene):

    def construct(self):
        logo = SVGMobject("assets/images/hsf.svg").scale(0.2).to_corner(UL)
        authorship = Text(
            "C. Poiret, A. Bouyeure, S. Patil, E. Duchesnay, A. Grigis, F. Lemaître, M. Noulhiane",
            weight="THIN",
            font="Open Sans")
        affiliations = Text("CEA Saclay | NeuroSpin | UNIACT/Inserm U1141",
                            weight="THIN",
                            font="Open Sans")

        self.add(logo.move_to(LEFT * 6.6 + UP * 3.6),
                 authorship.scale(0.25).next_to(logo, RIGHT * 0.5),
                 affiliations.scale(0.25).move_to(DOWN * 3.6 + LEFT * 5))

        self.next_section("Bayes", PresentationSectionType.NORMAL)

        self.camera.frame.save_state()

        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        labels = ax.get_axis_labels(x_label=Tex("$N_{models}$"),
                                    y_label=Tex("Error"))

        loss = ax.plot(lambda x: 1 / x + 1, color=BLUE, x_range=[0.115, 9])
        label_1 = Tex("$Loss_{seg}$", color=BLUE).move_to(DOWN + 2.5 * LEFT)
        optimal = DashedVMobject(ax.plot(lambda x: 1, color=RED, x_range=[0,
                                                                          9]))
        label_2 = Text("Bayes Optimal Error",
                       color=RED).scale(0.5).next_to(optimal,
                                                     0.5 * DOWN).shift(3 * LEFT)

        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(loss.t_min, loss), color=WHITE)
        dot_1 = Dot(ax.i2gp(loss.t_min, loss))
        dot_2 = Dot(ax.i2gp(loss.t_max, loss))

        self.play(FadeIn(ax, labels, loss, dot_1, dot_2, moving_dot))
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, loss, rate_func=linear))
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame), FadeIn(label_1))
        self.wait(1)

        self.next_section("Bayes.1", PresentationSectionType.SUB_NORMAL)
        self.play(Create(optimal), FadeIn(label_2))
        self.wait(4)

        self.next_section("Bayes.End", PresentationSectionType.SUB_SKIP)
        self.play(
            FadeOut(ax, labels, loss, dot_1, dot_2, moving_dot, optimal,
                    label_1, label_2))


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
        subtitle = Text("Plurality Voting & Aleatoric Uncertainty",
                        slant=ITALIC,
                        weight=LIGHT,
                        font="Open Sans").scale(0.4)

        self.next_section("Postprocessing", PresentationSectionType.NORMAL)

        self.play(FadeIn(title))
        self.play(title.animate.scale(0.75).move_to(UP * 3))
        self.play(FadeIn(subtitle.next_to(title, DOWN)))
        self.wait(2)

        self.next_section("Postprocessing.1",
                          PresentationSectionType.SUB_NORMAL)

        voting_title = Text("Label Fusion as\nPlurality Voting",
                            font="Open Sans").scale(0.5).next_to(
                                subtitle, DOWN).shift(4 * LEFT + .5 * DOWN)
        voting = Text(
            "The winning class (i.e. hippocampal\nsubfields) is the candidate that has the\nmaximum total number of votes.",
            font="Open Sans",
            weight=LIGHT).scale(0.4).next_to(voting_title, DOWN)

        self.play(FadeIn(voting_title, voting))
        self.wait(2)

        self.next_section("Postprocessing.2",
                          PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(voting_title, voting))
        unc = Text("Aleatoric Uncertainty",
                   font="Open Sans").scale(0.5).next_to(
                       subtitle, DOWN).shift(4 * RIGHT + .5 * DOWN)
        unc_sub = Text(
            "The uncertainty is estimated by measuring how\ndiverse the predictions for a given image are.",
            font="Open Sans",
            weight=LIGHT).scale(0.4).next_to(unc, DOWN)
        unc_eq = Tex(
            r"$H(Y^i|X) \approx - \sum^M_{m=1}{\hat{p}^i_m \ln \hat{p}^i_m}$")

        unc_desc_1 = Tex(
            r"Given a set $Y$ of $i$ predictions, in HSF\\the voxel-wise Aleatoric Uncertainty\\$H(Y^i|X)$ is defined as in Wang, et al., 2019:"
        ).scale(0.75).next_to(unc_eq, UP)
        unc_desc_2 = Tex(
            r"where $\hat{p}^i_m$ is the frequency\\of the $m$th unique value in $Y^i$."
        ).scale(0.75).next_to(unc_eq, DOWN)
        self.play(Write(unc_eq), FadeIn(unc_desc_1, unc_desc_2))
        self.wait(2)

        self.next_section("Postprocessing.3",
                          PresentationSectionType.SUB_NORMAL)
        unc_all = VGroup(unc_eq, unc_desc_1, unc_desc_2)
        self.play(FadeIn(unc), FadeIn(unc_sub),
                  unc_all.animate.scale(0.8).next_to(unc_sub, DOWN))
        line = Line(UP * 0.5, DOWN * 0.5)
        self.play(Create(line), FadeIn(voting_title, voting))
        self.wait(2)

        self.next_section("Postprocessing.End",
                          PresentationSectionType.SUB_SKIP)
        self.play(
            FadeOut(title, subtitle, unc, unc_sub, unc_all, line, voting,
                    voting_title))


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
        self.wait(1)

        segmentation = Text("Segmentation", font="Open Sans").scale(0.4).rotate(
            np.pi / 2).to_edge(LEFT).shift(UP + RIGHT)
        uncertainty = Text("Uncertainty", font="Open Sans").scale(0.4).rotate(
            np.pi / 2).to_edge(LEFT).shift(DOWN + RIGHT)

        t1w_seg = ImageMobject("assets/images/t1w_seg.png").next_to(
            segmentation, RIGHT).shift(.5 * RIGHT)
        t1w_unc = ImageMobject("assets/images/t1w_unc.png").next_to(
            uncertainty, RIGHT).shift(.5 * RIGHT)
        t1w_title = Text("T1w\nHealthy", font="Open Sans",
                         weight=LIGHT).scale(0.4).next_to(t1w_unc, DOWN)

        t2w_seg = ImageMobject("assets/images/t2w_seg.png").next_to(
            t1w_seg, RIGHT).shift(.5 * RIGHT)
        t2w_unc = ImageMobject("assets/images/t2w_unc.png").next_to(
            t1w_unc, RIGHT).shift(.5 * RIGHT)
        t2w_title = Text("T2w\nHealthy", font="Open Sans",
                         weight=LIGHT).scale(0.4).next_to(t2w_unc, DOWN)

        t2w_seg2 = ImageMobject("assets/images/t2w_seg2.png").next_to(
            t2w_seg, RIGHT).shift(.5 * RIGHT)
        t2w_unc2 = ImageMobject("assets/images/t2w_unc2.png").next_to(
            t2w_unc, RIGHT).shift(.5 * RIGHT)
        t2w_title2 = Text("T2w\nSclerosis\nMotion Artifacts",
                          font="Open Sans",
                          weight=LIGHT).scale(0.4).next_to(t2w_unc2, DOWN)

        self.play(FadeIn(segmentation, uncertainty))

        self.play(FadeIn(t1w_seg, t1w_unc, t1w_title))

        self.play(FadeIn(t2w_seg, t2w_unc, t2w_title))

        self.play(FadeIn(t2w_seg2, t2w_unc2, t2w_title2))

        self.wait(4)

        self.next_section("Results.End", PresentationSectionType.SUB_SKIP)
        self.play(
            FadeOut(title, subtitle, segmentation, uncertainty, t1w_seg,
                    t1w_unc, t1w_title, t2w_seg, t2w_unc, t2w_title, t2w_seg2,
                    t2w_unc2, t2w_title2))


class End(BaseHsf):

    def construct(self):
        super().construct()

        title = Text("Thank you for your attention!", font="Open Sans")
        # img = ImageMobject("assets/images/monster.apng")
        self.next_section("End", PresentationSectionType.NORMAL)

        self.play(FadeIn(title))
        self.play(title.animate.scale(0.75).move_to(UP * 3))

        im = imageio.get_reader("assets/images/monster.gif")
        gif = []
        for frame in im:
            gif.append(ImageMobject(frame))

        gif *= 3

        for i, frame in enumerate(gif):
            if i == 0:
                self.play(FadeIn(frame))
            else:
                self.add(frame)
            self.wait(0.04)
            if i != len(gif) - 1:
                self.remove(frame)

        self.wait(2)

        self.next_section("End.End", PresentationSectionType.SUB_SKIP)
        self.play(FadeOut(title, frame))
