from manim import *

class TableScene(Scene):
  def construct(self):
    # construct table template
    table_skeleton = Table(
            [["","",""],["","",""],["","",""]],
            row_labels=[Text("Sen. X"), Text("Sen. Y"), Text("Sen. Z")],
            col_labels=[Text("Sen. X"), Text("Sen. Y"), Text("Sen. Z")])
    self.play(Write(table_skeleton))
    self.wait(10)

    # write diagonal of 100s across table (Sen. votes with themselves)
    first_hundred = Text('100')
    sec_hundred = Text('100')
    third_hundred = Text('100')

    first_hundred.shift([-1.5, 0.6, 0])
    sec_hundred.shift([1.5, -0.6, 0])
    third_hundred.shift([4.5, -1.8, 0])

    self.play(Write(first_hundred), Write(sec_hundred), Write(third_hundred))
    
    self.wait(10)

    # fill in Sen. X - Sen. Y data
    first_fifty = Text('50')
    sec_fifty = Text('50')

    first_fifty.shift([1.5, 0.6,0])
    sec_fifty.shift([-1.5, -0.6, 0])

    self.play(Write(first_fifty), Write(sec_fifty))

    self.wait(10)

    # fill in Sen. Y - Sen. Z data
    first_ten = Text('10')
    sec_ten = Text('10')

    first_ten.shift([1.5, -1.8, 0])
    sec_ten.shift([4.5, -0.6, 0])

    self.play(Write(first_ten), Write(sec_ten))

    self.wait(10)

    # fill in Sen. X - Sen. Z data
    first_twenty = Text('20')
    sec_twenty = Text('20')

    first_twenty.shift([-1.5, -1.8, 0])
    sec_twenty.shift([4.5, 0.6, 0])

    self.play(Write(first_twenty), Write(sec_twenty))

    self.wait(10)

class GraphScene(Scene):
  def construct(self):
    vertices = ['X', 'Y', 'Z']
    edges = []
    g = Graph(vertices, edges, labels=True)
    self.play(Create(g))
    self.wait(10)
    self.play(g.animate.add_edges(('X', 'Y'), edge_config={ 'stroke_width': 50 }))
    self.wait(10)
    self.play(g.animate.remove_edges(('X', 'Y')))
    self.wait(10)
    self.play(g.animate.add_edges(('X', 'Y'), edge_config={ 'stroke_width': 25}))
    self.wait(10)
    self.play(g.animate.add_edges(('Y', 'Z'), edge_config={ 'stroke_width': 10}), g.animate.add_edges(('Z', 'X'), edge_config={ 'stroke_width': 17}))
    self.wait(10)
    self.play(g['X'].animate.set_fill_color(BLUE), g['Y'].animate.set_fill_color(BLUE), g['Z'].animate.set_fill_color(RED))
    self.wait(30)