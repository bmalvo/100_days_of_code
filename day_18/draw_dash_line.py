def draw_dash_line(painter):
    for i in range(15):
        painter.forward(10)
        painter.up()
        painter.forward(10)
        painter.down()
