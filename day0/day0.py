from turtle import *


#we want to paint a house


#step 1: draw a square
speed(30)
width(7)      
color('red')
forward(200)
left(90)
forward(200)

left(90)
forward(200)
left(90)
forward(200)
#end of square
 
#drawing a door

left(90)
forward(70)
color("blue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60) 
right(90)

forward(120) #height of the door
end_fill()
 
penup()
goto(200,200)
pendown()
color("orange")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
exitonclick()


