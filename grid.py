import turtle


count = 0
while (count <= 5):
    turtle.penup()
    turtle.goto(-200,200 - count * 100)
    turtle.pendown()
    turtle.goto(300, 200 - count * 100)
    count = count + 1
count2 = 0
while (count2 <= 5):
    turtle.penup()
    turtle.goto(count2 * 100 - 200, 200)
    turtle.pendown()
    turtle.goto(count2 * 100 - 200, -300)
    count2 = count2 + 1





turtle.exitonclick()

 
   
