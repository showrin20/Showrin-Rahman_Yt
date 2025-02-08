from turtle import *
col=["red","green","blue","purple"]
for i in range(4):
  color(col[i%4])
  forward(100)
  left(90)
  circle(50)
done()





from turtle import *
speed(0)
Screen().bgcolor("black")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(100):
    pencolor(colors[i % 6])
    forward(i * 2)
    left(59)
done()



from turtle import *
speed(0)
Screen().bgcolor("black")
colors = ["red", "blue", "green", "yellow"]
for i in range(100):
    pencolor(colors[i % 4])
    forward(i * 5)
    left(90)
done()




from turtle import *
speed(0)
Screen().bgcolor("black")
colors = ["cyan", "magenta", "yellow", "white"]
for i in range(36):
    pencolor(colors[i % 4])
    circle(50)
    left(10)
done()




from turtle import *
speed(0)
Screen().bgcolor("black")
color("gold")
for i in range(50):
    forward(i * 10)
    right(144)

done()



from turtle import *

speed(0)
Screen().bgcolor("black")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(72):
    pencolor(colors[i % 6])
    for _ in range(6):
        forward(i * 2)
        left(60)
    left(5)

done()





