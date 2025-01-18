import turtle

def draw_geometric_pattern():
    screen = turtle.Screen()
    screen.bgcolor("black")  # 背景色を黒に設定

    pen = turtle.Turtle()
    pen.speed(0)  # 最大速度
    pen.color("cyan")  # ペンの色を設定
    pen.width(2)  # ペンの幅を設定

    # 幾何学模様を描く
    for angle in range(0, 360, 10):
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        pen.seth(angle)  # 向きを設定
        for _ in range(36):
            pen.forward(100)
            pen.right(170)

    pen.hideturtle()  # ペンを隠す
    screen.mainloop()

draw_geometric_pattern()

