from manim import *
import numpy as np

class introaula5(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        #mycolor = ManimColor('#000000') #preto
        #mycolor = ManimColor('#080C04')
        mycolor = ManimColor('#151F0A')
        #mycolor = ManimColor('#FFFF00') # amarelo
        self.camera.background_color = mycolor




        # configuracao de cores, titulos e logo
        gradiente_vv = ["#00FF00" , "#5CD0B3", "#83C167"]
        
        img = ImageMobject('logo02')
        img.scale(0.3)  
        img.shift(3.3*DOWN + 5.9*RIGHT)  
        self.add(img) 

        turma = MarkupText("Equações Diferenciais", font = "lato", weight=BOLD).scale(0.4).move_to(5.4*LEFT+3.5*UP)
        turma.set_color_by_gradient(gradiente_vv)

        materia = MarkupText("Estudo das Equações Diferenciais Autônomas", font = "lato", weight=BOLD).scale(0.4).move_to(4.3*RIGHT+3.5*UP)
        materia.set_color_by_gradient(gradiente_vv)
        self.play(Write(turma), Write(materia), run_time = 0.3)
        self.wait(2)

        texto01 = MarkupText("Voltamos a uma Equação Diferencial do tipo...", font = "lato", weight=BOLD).scale(0.9).move_to(0*RIGHT+1.5*UP)
        self.play(Write(texto01))
        self.wait(4)
        self.play(FadeOut(texto01))


        axes = Axes(
            x_range = [-7,7,1], #come, fim, passo
            y_range = [-4,4,1],
            x_length = 14, #tamanho, espaco do eixo x
            y_length = 8, #tamanho, espaco do eixo y
            axis_config = {'color': WHITE, 'tip_shape': StealthTip, 'include_ticks': False}, #cor do eixo e tracinhos sem (fasle)
            tips = True
        )
        gradiente_vv = ["#00FF00" , "#5CD0B3", "#83C167"]
        
        # Labels do eixos
        labels = axes.get_axis_labels(x_label = 'x', y_label = 'y')

        curve01 = axes.plot(lambda x: (1/16)*x**4-x**2+4, x_range = (-4,4)).set_color_by_gradient(RED, ORANGE)


        pt01 = Dot(point=axes.c2p(2, 1, 0), color=TEAL, radius = 0.03)
        
        ponto01 = MathTex(r'(2,1)').set_color_by_gradient(BLUE, TEAL).scale(1.1)
        ponto01.next_to(pt01, RIGHT+DOWN)

        

        lines_1 = axes.get_lines_to_point([2,1,0], color = GREEN_A)
        x0label = MathTex(r'y_0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([0,1,0], 1.3*LEFT)
        y0label = MathTex(r'x_0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([2,0,0], 1.3*DOWN)

        
        # criando pontos
        point_1 = np.array([0,1,0])
        dot_1 = Dot(point_1, color = WHITE)
        label_1 = Text('(0,1)', font_size = 30).next_to(dot_1, LEFT+0.3*DOWN)

        point_2 = np.array([0,2,0])
        dot_2 = Dot(point_2, color = WHITE)
        label_2 = Text('(0,2)', font_size = 30).next_to(dot_2, LEFT+0.3*DOWN)

        point_3 = np.array([0,3,0])
        dot_3 = Dot(point_3, color = WHITE)
        label_3 = Text('(0,3)', font_size = 30).next_to(dot_3, LEFT+0.3*DOWN)

        point_4 = np.array([0,-1,0])
        dot_4 = Dot(point_4, color = WHITE)
        label_4 = Text('(0,-1)', font_size = 30).next_to(dot_4, LEFT+0.3*DOWN)


        self.wait(2)

        #criar um PVI geral e dizer que a equacao determina uma familia mas o PVI determina uma unica solucao 
        #criando o PVI geral
        funcPVIgeral01_label = MathTex(r'\frac{dy}{dx}=F(x,y)}').set_color_by_gradient(BLUE, TEAL).scale(1.5)
        funcPVIgeral01_label.shift(3*LEFT+1*UP)
        funcPVIgeral02_label = MathTex(r'y(x_{0})=y_{0}').set_color_by_gradient(BLUE, TEAL).scale(1.5)
        funcPVIgeral02_label.shift(3*LEFT+1*DOWN)


        
        
        PVItext = MarkupText("P.V.I.:", font = "lato", weight=BOLD).scale(1.3).move_to(3*LEFT+2.8*UP)


        self.play(Write(PVItext), Write(funcPVIgeral01_label), Write(funcPVIgeral02_label))

        arrow01 = Arrow([-0.6,1,0],[0.8,1,0], color = TEAL)
        arrow02 = Arrow([-0.6,-1,0],[0.8,-1,0], color = TEAL)

        PVItext01 = MarkupText("define uma família de soluções", font = "lato", weight=BOLD).scale(0.5).move_to(3.5*RIGHT+1*UP)
        PVItext02 = MarkupText("define uma única solução", font = "lato", weight=BOLD).scale(0.5).move_to(3.5*RIGHT+1*DOWN)
        
        PVItext03 = MarkupText("define o campo de direção das soluções", color = GOLD, font = "lato", weight=BOLD).scale(0.5).move_to(3.7*RIGHT+1*UP)
        PVItext04 = MarkupText("define uma única solução", font = "lato", weight=BOLD).scale(0.5).move_to(3.5*RIGHT+1*DOWN)
        

        self.wait(4)
        self.play(Create(arrow01), Write(PVItext01))
        self.wait(3)
        self.play(Create(arrow02), Write(PVItext02))
        self.wait(6)

        self.play(FadeOut(arrow01), FadeOut(arrow02), FadeOut(PVItext01), FadeOut(PVItext02), FadeOut(PVItext))
        self.wait(3)

        self.play(funcPVIgeral01_label.animate.shift(2.5*RIGHT))
        self.play(funcPVIgeral02_label.animate.shift(2.5*RIGHT))

        funcPVIauto_label = MathTex(r'\frac{dy}{dx}=f(y)}').set_color_by_gradient(BLUE, TEAL).scale(1.5)
        funcPVIauto_label.shift(0.5*LEFT+1*UP)

        self.play(ReplacementTransform(funcPVIgeral01_label, funcPVIauto_label))

        self.wait(5)

        self.play(funcPVIauto_label.animate.shift(5.1*LEFT+1.8*UP).scale(0.5))
        self.play(funcPVIgeral02_label.animate.shift(5.1*LEFT+2.9*UP).scale(0.5))
        self.wait(2)


        funcPVIauto02 = MathTex(r'\frac{dy}{dx}=f(y)}').set_color_by_gradient(BLUE, TEAL).scale(1.5)
        funcPVIauto02.shift(0.0*LEFT+1*UP)

        funcPVIauto03 = MathTex(r'y^{\prime}=f(y)}').set_color_by_gradient(BLUE, TEAL).scale(1.5)
        funcPVIauto03.shift(0.0*LEFT+1*UP)

        self.play(Write(funcPVIauto02), run_time = 2)
        self.wait(3)

        self.play(ReplacementTransform(funcPVIauto02, funcPVIauto03))
        self.wait(3)

        #criando exemplo 
        exPVIauto04 = MathTex(r'y^{\prime}=2y-y^{2}}').set_color_by_gradient(BLUE, TEAL).scale(1.2)
        exPVIauto04.shift(0.0*LEFT+2.5*DOWN)
        exPVIauto05 = MathTex(r'y^{\prime}=2y-y^{2}}').set_color_by_gradient(BLUE, TEAL).scale(1.2)
        exPVIauto05.shift(0.0*LEFT+2.5*DOWN)
        exPVIauto04text = MarkupText("Exemplo:", font = "lato", weight=BOLD).scale(0.5).move_to(0.0*RIGHT+1.5*DOWN)

        self.play(Write(exPVIauto04), Write(exPVIauto04text))
        self.wait(3)

        self.play(ReplacementTransform(exPVIauto04,exPVIauto05))

        self.wait(3)

        self.play(funcPVIauto03.animate.move_to([4,1.9,0]).scale(1.0))
        self.play(exPVIauto04text.animate.move_to([4,1.2,0]).scale(0.9))
        self.play(exPVIauto05.animate.move_to([4,0.7,0]).scale(0.9))
        


        #criando eixo auxiliar menor
        axes2 = Axes(
            x_range = [-3.5,3.5,1], #come, fim, passo
            y_range = [-2,2,1],
            x_length = 7, #tamanho, espaco do eixo x
            y_length = 4, #tamanho, espaco do eixo y
            axis_config = {'color': WHITE, 'tip_shape': StealthTip, 'include_ticks': False}, #cor do eixo e tracinhos sem (fasle)
            tips = True
        )
        # Labels do eixos
        leixo01 = MathTex(r'y^{\prime}}').set_color_by_gradient(WHITE, GRAY).scale(0.7)
        leixo01.move_to([3.9,-0.4,0])
        leixo02 = MathTex(r'y').set_color_by_gradient(WHITE, GRAY).scale(0.7)
        leixo02.move_to([6.5,-2.3,0])

        dotaxes2 = [3.5,-2.0,0]
        axes2.move_to(dotaxes2)
        axes2.scale(0.9)
        

        rectaxes2 = RoundedRectangle(corner_radius=0.2, fill_color = GREEN, fill_opacity = 0.1, stroke_color = BLUE_B, height=4.0, width=7).move_to(dotaxes2)
        rectaxes2.scale(0.9)
        self.play(Create(axes2), Create(rectaxes2), Create(leixo01), Create(leixo02))
        self.wait(2)

        #criando funcao do exemplo para a edo autonoma 
        curveauto01 = axes2.plot(lambda x: -x**2+2*x, x_range = (-0.7,2.6)).set_color_by_gradient(RED, ORANGE)
        self.play(Create(curveauto01), run_time = 3)
        self.wait(3)

        #criando sinais da derivada 
        sinais01 = MathTex(r'+').set_color_by_gradient(RED, YELLOW).scale(0.8)
        sinais01.shift([4.3,-1.5,0])
        sinais02 = MathTex(r'-').set_color_by_gradient(BLUE, TEAL).scale(0.8)
        sinais02.shift([2.8,-2.5,0])
        sinais03 = MathTex(r'-').set_color_by_gradient(BLUE, TEAL).scale(0.8)
        sinais03.shift([5.9,-2.5,0])

        self.play(Write(sinais02))
        self.play(Write(sinais01))
        self.play(Write(sinais03))

        self.wait(4)

        # colocando os pontos 
        dot01axes2 = Dot(axes2.coords_to_point(2,0), color = WHITE).set_z_index(1)
        dot01text = MathTex(r'2').scale(0.7).next_to(dot01axes2, RIGHT+UP, buff = 0.02)

        dot02axes2 = Dot(axes2.coords_to_point(0,0), color = WHITE).set_z_index(1)
        dot02text = MathTex(r'0').scale(0.7).next_to(dot02axes2, LEFT+UP, buff = 0.02)


        self.play(Create(dot01axes2), Write(dot01text))
        self.play(Create(dot02axes2), Write(dot02text))

        self.wait(3)

        # apagar os dados do canto superior esquerdo 
        self.play(Unwrite(funcPVIgeral01_label), Unwrite(funcPVIauto_label))
        # Unwrite(funcPVIgeral02_label)
        self.wait(2)
        #levar para lá (canto sup esq) o exemplo
        self.play(funcPVIauto03.animate.move_to([-5.1,2.6,0]).scale(0.6))
        self.wait(3)

        # apagar o central 
        # fazer a solucao yˆ2-y=0 e y(y-1)=0 e y=0, y=1 solucoes de equilibrio 
        sol01 = MathTex(r'2y-y^{2}=0').set_color_by_gradient(WHITE, GRAY).scale(0.7)
        sol01.move_to([1.5,-2.7,0])
        sol02 = MathTex(r'(2-y)y=0').set_color_by_gradient(WHITE, GRAY).scale(0.7)
        sol02.move_to([1.5,-2.7,0])
        sol03 = MathTex(r'y=0,').set_color_by_gradient(WHITE, GRAY).scale(0.7)
        sol03.move_to([1.0,-3.1,0])
        sol04 = MathTex(r'y=2').set_color_by_gradient(WHITE, GRAY).scale(0.7)
        sol04.move_to([2.0,-3.1,0])

        

        self.play(Write(sol01))
        self.wait(2)
        self.play(ReplacementTransform(sol01, sol02))
        self.wait(2)
        self.play(Write(sol03))
        self.wait(1)
        self.play(Write(sol04))
        self.wait(1)

        
        #### col;ocar eixos e comecar a avaliar a edo autonoma

        self.wait(3)
        self.play(Create(axes), Write(labels))
        self.wait(2)

        ## colocar as linhas dashed em y=0 e y=1 e movendo o exemplo pra cima
        self.play(exPVIauto04text.animate.move_to([4,3,0]).scale(0.9))
        self.play(exPVIauto05.animate.move_to([4,2.5,0]).scale(0.9))


        linha01 = axes.plot(lambda x: 0, x_range = [-7, 7], color = WHITE)
        linha01_dashed = DashedVMobject(linha01,num_dashes=40,equal_lengths=True).set_color_by_gradient(GRAY, BLACK)

        linha02 = axes.plot(lambda x: 2, x_range = [-7, 7], color = WHITE)
        linha02_dashed = DashedVMobject(linha02,num_dashes=40,equal_lengths=True).set_color_by_gradient(GRAY, BLACK)

        self.play(Create(linha01_dashed))
        self.wait(2)
        self.play(Create(linha02_dashed))
        self.wait(3)

        # colocando os pontos 

        dot001axes = Dot(axes.coords_to_point(0,2), color = WHITE).set_z_index(1)
        dot001text = MathTex(r'2').scale(0.7).next_to(dot001axes, LEFT+UP, buff = 0.02)

        dot002axes = Dot(axes.coords_to_point(0,0), color = WHITE).set_z_index(1)
        dot002text = MathTex(r'0').scale(0.7).next_to(dot002axes, LEFT+UP, buff = 0.02)

        self.play(Create(dot001axes), Write(dot001text))
        self.play(Create(dot002axes), Write(dot002text))


        #colocar o campo de direcoes para esse caso 
        # criando um campo a partir da funcao 
        # pelo que entendi pos[0] = x e pos[1] = y
        func = lambda pos: 1 * RIGHT + (2-pos[1])*pos[1] * UP
        vector_field = ArrowVectorField(func, opacity= 0.3)
        eq_campo1 = MathTex(r'\frac{dy}{dx}=(2-y)y', font_size = 50)
        eq_campo1.shift(3*DOWN+4*RIGHT)
        vector_field.set_color_by_gradient(PURPLE, BLUE)

        #self.play(Create(vector_field), run_time = 3)

        func2 = lambda pos: (1 * RIGHT + (2-pos[1])*pos[1] * UP)
        #self.add(StreamLines(func))
        caminhos = StreamLines(func2)
        caminhos.set_color_by_gradient(gradiente_vv)
        caminhos.set_z_index(-1)
        #caminhos.set_opacity(0.3)

        #self.play(Create(caminhos), run_time = 3)
        self.play(FadeIn(caminhos), run_time = 5)
        #self.play(caminhos.create(), run_time = 3)

        func3 = lambda pos: (1 * RIGHT + (2-pos[1])*pos[1] * UP)
        stream_lines = StreamLines(
            func3,
            color = YELLOW,
            x_range = [-7, 7, 1],
            y_range = [-4, 4, 1],
            stroke_width = 1,
            virtual_time = 1,  # use shorter lines
            max_anchors_per_line = 5,  # better performance with fewer anchors
        ).set_color_by_gradient(gradiente_vv)
        stream_lines.set_opacity(0.3)


        #self.play(stream_lines.create(), run_time = 2)  # uses virtual_time as run_time
        self.wait()





        #colocar a solucoes para deferentes pontos iniciais 
        
        
        # y0 = 1.0
        curva01 = axes.plot(lambda x: (2*np.exp(2*x))/(np.exp(2)+np.exp(2*x)), x_range = (-7,7)).set_color_by_gradient(RED, ORANGE)
        self.play(Create(curva01), run_time = 3)
        self.wait(2)

        
        
        x0t = ValueTracker(1)


        pt001 = Dot(point=axes.c2p(1, 1, 0), color=TEAL, radius = 0.02)
        pt001.add_updater(
            lambda mob: mob.become(Dot(point=axes.c2p(x0t.get_value(), (2*np.exp(2*x0t.get_value()))/(np.exp(2)+np.exp(2*x0t.get_value())), 0), color=TEAL, radius = 0.02))
        )

        lines_01 = axes.get_lines_to_point([1,1,0], color = GREEN_A)
        lines_01.add_updater(
            lambda mob: mob.become(axes.get_lines_to_point([x0t.get_value(), (2*np.exp(2*x0t.get_value()))/(np.exp(2)+np.exp(2*x0t.get_value())), 0], color = GREEN_A))
        )

        x00label = MathTex(r'y_0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([0,1,0], 1.3*LEFT)
        x00label.add_updater(
            lambda mob: mob.become(MathTex(r'y_0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([0, (2*np.exp(2*x0t.get_value()))/(np.exp(2)+np.exp(2*x0t.get_value())),0], 1.3*LEFT))
        )

        y00label = MathTex(r'x_0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([1,0,0], 1.3*DOWN)
        y00label.add_updater(
            lambda mob: mob.become(MathTex(r'x_0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([x0t.get_value(),0,0], 1.3*DOWN))
        )

        self.play(Write(x00label), Write(y00label), Create(lines_01), Create(pt001))
        self.wait(3)
        self.play(x0t.animate.set_value(1.8), run_time = 2, rate_func = smooth)
        self.wait(1)
        self.play(x0t.animate.set_value(4.0), run_time = 2, rate_func = smooth)
        self.wait(3)

        #aproximara camera em 7 segundos
        dot_cam = [4, (2*np.exp(2*4))/(np.exp(2)+np.exp(2*4)), 0]
        self.play(self.camera.frame.animate.scale(0.04).move_to(dot_cam), run_time = 7, rate_func = smooth)
        self.wait()

        self.wait(5)
        self.play(Restore(self.camera.frame), run_time = 2)



        self.play(x0t.animate.set_value(-4.8), run_time = 2, rate_func = smooth)
        self.wait(1)
        self.play(x0t.animate.set_value(-2.8), run_time = 2, rate_func = smooth)
        self.wait(1)
        self.play(x0t.animate.set_value(6.8), run_time = 4, rate_func = smooth)
        self.wait(2)
        self.play(x0t.animate.set_value(1), run_time = 4, rate_func = smooth)

        self.wait(4)
        self.play(FadeOut(x00label), FadeOut(y00label), FadeOut(lines_01), FadeOut(pt001), FadeOut(curva01))

        self.wait(2)


        # y0 = 2.5

        curva02 = axes.plot(lambda x: (2*np.exp(2*x))/(-0.2+np.exp(2*x)), x_range = (-0.5,7)).set_color_by_gradient(RED, ORANGE)
        self.play(Create(curva02), run_time = 3)
        self.wait(2)

        
        
        x1t = ValueTracker(1)


        pt002 = Dot(point=axes.c2p(1, (2*np.exp(2))/(-0.2+np.exp(2)), 0), color=TEAL, radius = 0.09)
        pt002.add_updater(
            lambda mob: mob.become(Dot(point=axes.c2p(x1t.get_value(), (2*np.exp(2*x1t.get_value()))/(-0.2+np.exp(2*x1t.get_value())), 0), color=TEAL, radius = 0.09))
        )

        lines_02 = axes.get_lines_to_point([1,1,0], color = GREEN_A)
        lines_02.add_updater(
            lambda mob: mob.become(axes.get_lines_to_point([x1t.get_value(), (2*np.exp(2*x1t.get_value()))/(-0.2+np.exp(2*x1t.get_value())), 0], color = GREEN_A))
        )

        x01label = MathTex(r'y_0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([0,(2*np.exp(2))/(-0.2+np.exp(2)),0], 1.3*LEFT)
        x01label.add_updater(
            lambda mob: mob.become(MathTex(r'y_0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([0, (2*np.exp(2*x1t.get_value()))/(-0.2+np.exp(2*x1t.get_value())),0], 1.3*LEFT))
        )

        y01label = MathTex(r'x_0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([1,0,0], 1.3*DOWN)
        y01label.add_updater(
            lambda mob: mob.become(MathTex(r'x_0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([x1t.get_value(),0,0], 1.3*DOWN))
        )

        self.play(Write(x01label), Write(y01label), Create(lines_02), Create(pt002))
        self.wait(3)
        self.play(x1t.animate.set_value(1.8), run_time = 2, rate_func = smooth)
        self.wait(1)
        self.play(x1t.animate.set_value(2.8), run_time = 2, rate_func = smooth)
        self.wait(1)
        self.play(x1t.animate.set_value(-0.3), run_time = 2, rate_func = smooth)
        self.wait(1)
        self.play(x1t.animate.set_value(6.8), run_time = 4, rate_func = smooth)
        self.wait(2)
        self.play(x1t.animate.set_value(1), run_time = 4, rate_func = smooth)

        self.wait(4)
        self.play(FadeOut(x01label), FadeOut(y01label), FadeOut(lines_02), FadeOut(pt002), FadeOut(curva02))

        self.wait(2)

        # y0 = -0.5
        curva03 = axes.plot(lambda x: (2*np.exp(2*x))/(-5+np.exp(2*x)), x_range = (-7,0.7)).set_color_by_gradient(RED, ORANGE)
        self.play(Create(curva03), run_time = 3)
        self.wait(2)

        
        
        x2t = ValueTracker(0)


        pt003 = Dot(point=axes.c2p(0, -0.5, 0), color=TEAL, radius = 0.09)
        pt003.add_updater(
            lambda mob: mob.become(Dot(point=axes.c2p(x2t.get_value(), (2*np.exp(2*x2t.get_value()))/(-5+np.exp(2*x2t.get_value())), 0), color=TEAL, radius = 0.09))
        )

        lines_03 = axes.get_lines_to_point([0,-0.5,0], color = GREEN_A)
        lines_03.add_updater(
            lambda mob: mob.become(axes.get_lines_to_point([x2t.get_value(), (2*np.exp(2*x2t.get_value()))/(-5+np.exp(2*x2t.get_value())), 0], color = GREEN_A))
        )

        x02label = MathTex(r'y_0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([0,(2*np.exp(2))/(-5+np.exp(2)),0], 1.3*LEFT)
        x02label.add_updater(
            lambda mob: mob.become(MathTex(r'y_0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([0, (2*np.exp(2*x2t.get_value()))/(-5+np.exp(2*x2t.get_value())),0], 1.3*LEFT))
        )

        y02label = MathTex(r'x_0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([1,0,0], 1.3*UP)
        y02label.add_updater(
            lambda mob: mob.become(MathTex(r'x_0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([x2t.get_value(),0,0], 1.3*DOWN))
        )

        self.play(Write(x02label), Write(y02label), Create(lines_03), Create(pt003))
        self.wait(3)
        self.play(x2t.animate.set_value(-6.0), run_time = 2, rate_func = smooth)
        self.wait(1)
        self.play(x2t.animate.set_value(-3.8), run_time = 2, rate_func = smooth)
        self.wait(1)
        self.play(x2t.animate.set_value(-1.3), run_time = 2, rate_func = smooth)
        self.wait(1)
        self.play(x2t.animate.set_value(0.4), run_time = 4, rate_func = smooth)
        self.wait(2)
        self.play(x2t.animate.set_value(-1), run_time = 4, rate_func = smooth)

        self.wait(4)
        self.play(FadeOut(x02label), FadeOut(y02label), FadeOut(lines_03), FadeOut(pt003), FadeOut(curva03))

        self.wait(2)

        ## colocar nomes ATRATOR e REPELIDOR 

        atrator = MarkupText("atrator", font = "lato", weight=BOLD).scale(0.8).move_to(2.5*LEFT+1.1*UP)
        pt_atr = MathTex(r'y = 2').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([-2.2,1.6,0], 1.3*LEFT)
       
        self.play(Write(atrator), Write(pt_atr))
        self.wait(2)

        repelidor = MarkupText("repelidor", font = "lato", weight=BOLD).scale(0.8).move_to(2.0*LEFT+1.0*DOWN)
        pt_rep = MathTex(r'y = 0').set_color_by_gradient(BLUE, TEAL).scale(0.8).next_to([-2.0,-0.5,0], 0.6*LEFT)

        self.play(Write(repelidor), Write(pt_rep))
        self.wait(2)

        
        
        ''''

        #inserir zoomIN da camera
        dot_1 = [2,1,0]
        self.play(self.camera.frame.animate.scale(0.2).move_to(dot_1), run_time = 2.5, rate_func = smooth)
        '''
      

        #self.play(self.camera.frame.animate.scale(0.1).move_to(dot_1), run_time = 2.5, rate_func = smooth)

        
        '''
        self.play(self.camera.frame.animate.scale(0.05).move_to(dot_1), run_time = 2.5, rate_func = smooth)
        self.wait(2)
        self.play(ReplacementTransform(circ03, circ04))
        self.wait(2)
        '''

        self.wait(2)
        self.play(Restore(self.camera.frame))

