from manim import *

class TableScene(Scene):
  def construct(self):

    # TODO: add colors?
    table_skeleton = Table(
            [["","",""],["","",""],["","",""]],
            row_labels=[Text("Sen. X", color=BLACK), Text("Sen. Y", color=BLACK), Text("Sen. Z", color=BLACK)],
            col_labels=[Text("Sen. X", color=BLACK), Text("Sen. Y", color=BLACK), Text("Sen. Z", color=BLACK)])
    self.play(Write(table_skeleton))

    self.wait(2)

    table_labels_only = Table(
            [["","",""],["","",""],["","",""]],
            row_labels=[Text("Sen. X"), Text("Sen. Y"), Text("Sen. Z")],
            col_labels=[Text("Sen. X"), Text("Sen. Y"), Text("Sen. Z")])

    self.play(Transform(table_skeleton, table_labels_only))

    self.wait(1)

    table_diag_filled = Table(
            [["100","",""],["","100",""],["","","100"]],
            row_labels=[Text("Sen. X"), Text("Sen. Y"), Text("Sen. Z")],
            col_labels=[Text("Sen. X"), Text("Sen. Y"), Text("Sen. Z")])

    self.play(Transform(table_labels_only, table_diag_filled))

    # TODO: break this up for each relationship
    table_full_data = Table(
            [["100","50","20"],["50","100","10"],["20","10","100"]],
            row_labels=[Text("Sen. X"), Text("Sen. Y"), Text("Sen. Z")],
            col_labels=[Text("Sen. X"), Text("Sen. Y"), Text("Sen. Z")])

    self.wait(1)
    
    self.play(Transform(table_diag_filled, table_full_data))

