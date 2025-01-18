import turtle

# ウィンドウの設定
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("亀プログラム")

# 亀の作成
kame = turtle.Turtle()
kame.shape("turtle")
kame.color("green")
kame.speed(2)

# 四角形を描く
for i in range(1,100):
    kame.forward(100*i)  # 100ピクセル前進
    kame.left(90)      # 左に90度回転

# 円を描く
kame.penup()           # ペンを持ち上げる（描画しない）
kame.goto(150, 0)      # 新しい位置に移動
kame.pendown()         # ペンを下ろす（描画する）
kame.circle(50)        # 半径50の円を描く

# プログラムを終了するまでウィンドウを開いたままにする
screen.mainloop()

