import turtle

# إعداد المظهر الأولي للنافذة والقلم
window = turtle.Screen()
window.bgcolor("white")
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")
pen.fillcolor("red")

# رسم شكل القلب
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()

# إخفاء القلم بعد الانتهاء
pen.hideturtle()

# إغلاق النافذة عند النقر عليها
window.exitonclick()
