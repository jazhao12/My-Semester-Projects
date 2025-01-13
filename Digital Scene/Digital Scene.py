#James Zhao
#Oct 1
#Period 7
#Digital Scene


#This program will draw a scene from Spongebob!
#Coded by James Zhao, Matthew Yang, and Sadie Wood.


#Initialize
import turtle
import random
james=turtle.Turtle()
james.speed(0)
matt=turtle.Turtle()
matt.speed(0)
sadie=turtle.Turtle()
sadie.speed(0)

#Functions
#Simplfied turtle penup, goto, pendown sequence
#The 'james' turtle will go to (x,y) without drawing a line
#x = integer
#y = integer
#Coded by James
def turtlegoto(x,y):
    james.pu()
    james.goto(x,y)
    james.pd()

#Simplified General Turtle Line Drawing
#The 'james' turtle with face 'orientation' and go forward 'distance'
#orientation = integer
#distance = integer
def betterForward(orientation,distance):
    james.seth(orientation)
    james.fd(distance)

#Simplified Line Drawing for the Orange Pineapple
#The 'james' turtle will go to (x,y) and face 'orientation' and go forward 'distance'
#x = integer
#y = integer
#orientation = integer
#distance = integer
#Coded by James
def drawPineLine(x,y,orientation,distance):
    turtlegoto(x,y)
    betterForward(orientation,distance)

#Draws the base outline for the Orange Pineapple
#Coded by James
def spongeHouse():
    turtlegoto(200,0)
    james.color('#ff6600')
    james.begin_fill()
    betterForward(0,100)
    james.seth(70)
    james.circle(150,50)
    betterForward(180,80)
    james.seth(240)
    james.circle(150,50)
    james.end_fill()
    james.color('#000000')
    drawPineLine(240,125,210,50)
    drawPineLine(270,125,225,115)
    drawPineLine(295,110,227,145)
    drawPineLine(305,80,230,105)
    drawPineLine(310,50,240,58)
    drawPineLine(260,125,330,46)
    drawPineLine(230,125,315,113)
    drawPineLine(205,110,313,143)
    drawPineLine(195,80,310,104)
    drawPineLine(190,50,300,58)

#Draws one leaf of the pineapple
#size = integer
#orientation = integer
#Coded by James
def spongeLeaf(size,orientation):
    james.color('#99cc00')
    james.begin_fill()
    james.seth(90 - orientation)
    james.circle(-size,70)
    james.rt(105)
    james.circle(-size,70)
    james.end_fill()

#Draws the leaves of the pineapple
#x = integer
#y = integer
#Coded by James
def spongeRoof(x,y):
    turtlegoto(x,y)
    rotation=20
    for i in range(-60,15,15):
        spongeLeaf(100,i)
        betterForward(rotation,5)
        rotation -= 5
    james.seth(90)
    james.begin_fill()
    james.circle(40,180)
    betterForward(0,80)
    james.end_fill()

#Draws a window of the pineapple
#x = integer
#y = integer
#Coded by James
def spongeWindow(x,y):
    james.color('#1a75ff')
    turtlegoto(x,y)
    james.begin_fill()
    james.circle(15)
    james.end_fill()
    turtlegoto(x,y+5)
    james.color('#0066cc')
    james.width(4)
    james.circle(10)

#Draws the door of the pineapple
#Coded by James
def spongeDoor():
    james.color('#1a75ff')
    james.width(2)
    turtlegoto(270,0)
    james.begin_fill()
    betterForward(90,40)
    james.circle(20,180)
    james.fd(40)
    betterForward(0,40)
    james.end_fill()
    james.color('#0066cc')
    james.bk(5)
    betterForward(90,40)
    james.circle(15,180)
    james.fd(40)
    turtlegoto(240,5)
    betterForward(0,20)
    betterForward(90,30)
    james.circle(10,180)
    james.fd(30)
    turtlegoto(243,30)
    james.circle(7)
    turtlegoto(245,30)
    james.circle(5)
    turtlegoto(250,30)
    james.dot(5)
    
#Draws the pineapple side-chimney
#x = integer
#y = integer
#Coded by James
def spongeChimney(x,y):
    james.color('#1a75ff')
    turtlegoto(x,y)
    james.begin_fill()
    betterForward(0,random.randint(12,15))
    betterForward(110,4)
    betterForward(0,8)
    betterForward(110,8)
    betterForward(0,4)
    betterForward(120,20)
    betterForward(0,25)
    betterForward(240,20)
    betterForward(0,4)
    betterForward(270,10)
    james.circle(-7,90)
    james.fd(10)
    betterForward(90,2)
    betterForward(180,random.randint(15,18))
    james.end_fill()
    james.color('#0066cc')
    turtlegoto(x+12,y)
    betterForward(270,5)
    turtlegoto(x+18,y+12)
    betterForward(0,10)

#Draws the entire Spongebob House
#Coded by James
def spongeFullHouse():
    spongeChimney(300,95)
    spongeHouse()
    spongeRoof(215,120)
    spongeWindow(220,60)
    spongeWindow(292,30)
    spongeDoor()

#builds the base of patrick's house (a rock)
#Coded by Matthew
def buildRock():
    matt.penup()
    matt.goto(-200, 0)
    matt.pendown()
    matt.begin_fill()
    matt.color("brown")
    matt.left(90)
    matt.circle(70,180)
    matt.end_fill()

#builds the weathervane located on top of the rock
#Coded by Matthew
def buildWeatherVane():
    matt.penup()
    matt.goto(-270,70)
    matt.color("#b5bf41")
    matt.pendown()
    matt.backward(20)
    matt.goto(-290,90)
    matt.right(210)
    matt.forward(10)
    matt.right(180)
    matt.forward(10)
    matt.left(60)
    matt.forward(10)
    matt.penup()
    matt.goto(-270,90)
    matt.pendown()
    matt.left(60)
    matt.forward(20)
    matt.left(90)
    matt.forward(10)
    matt.backward(20)
    matt.forward(10)
    matt.right(90)
    matt.forward(5)
    matt.left(90)
    matt.forward(10)
    matt.backward(20)

#builds patrick's house (rock and weather vane)
#Coded by Matthew
def buildPatrickHouse():
    buildRock()
    buildWeatherVane()

#Draws the "ears" on the side of the house
#color = a string hex code
#x = integer
#y = integer
#Coded by Sadie Wood
def drawEars(color, x,y):
    sadie.color(color)
    sadie.penup()
    sadie.goto(x,y)
    sadie.pendown()
    sadie.begin_fill()
    for i in range(2):
        sadie.right(90)
        sadie.forward(80)
        sadie.right(90)
        sadie.forward(170)
    sadie.end_fill()

#draws the big trapezoid that makes up squidward's house
#color = a string hex code
#x = integer
#y = integer
#Coded by Sadie Wood
def drawBigTrapezoid(color, x,y):
    sadie.penup()
    sadie.goto(x,y)
    sadie.pendown()
    sadie.color(color)
    sadie.pencolor("black")
    sadie.pensize(2)
    sadie.begin_fill()
    sadie.left(80)
    sadie.forward(250)
    sadie.right(80)
    sadie.forward(90)
    sadie.right(80)
    sadie.forward(250)
    sadie.right(100)
    sadie.forward(178)
    sadie.end_fill()

#Draws the "nose" and "eyebrow" on the house
#color = a string hex code
#x = integer
#y = integer
#Coded by Sadie Wood
def drawBrowsNose(color, x,y):
    sadie.penup()
    sadie.goto(x,y)
    sadie.pendown()
    sadie.color(color)
    sadie.pensize(2)
    sadie.pencolor("black")
    sadie.begin_fill()
    sadie.right(90)
    sadie.forward(30)
    sadie.right(90)
    sadie.forward(80)
    sadie.right(90)
    sadie.forward(30)
    sadie.right(90)
    sadie.forward(45)
    sadie.left(80)
    sadie.forward(75)
    sadie.left(100)
    sadie.forward(40)
    sadie.left(100)
    sadie.forward(75)
    sadie.left(80)
    sadie.forward(50)
    sadie.end_fill()

#Draws one eye of the squidward house
#Coded by Sadie Wood
def drawOneEye():
    sadie.dot(30, "#0975e0")
    sadie.dot(15, "#128cde")

#Draws both windows/ eyes of the house
#Coded by Sadie Wood
def drawEyes():
    sadie.penup()
    sadie.goto(-33,140)
    sadie.pendown()
    drawOneEye()
    sadie.penup()
    sadie.goto(32,140)
    sadie.pendown()
    drawOneEye()

#Draws door/ mouth of the house
#color = a string hex code
#Coded by Sadie Wood
def drawDoor(color):
    sadie.right(90)
    sadie.penup()
    sadie.goto(-21,0)
    sadie.pendown()
    sadie.color(color)
    sadie.pencolor("black")
    sadie.begin_fill()
    sadie.forward(45)
    sadie.circle(-24,180)
    sadie.forward(45)
    sadie.right(90)
    sadie.forward(48)
    sadie.end_fill()

#Combines all elements of the face into one function
#Coded by Sadie Wood    
def drawFace():
    drawBrowsNose("#22476b", -41,160)
    drawEyes()
    drawDoor("#ad6e00")

#Combines all functions and draws all of squidwards house
#Coded by Sadie Wood
def drawSquidHouse():
    drawEars("#22476b", 85,175)
    drawBigTrapezoid("#375f87", -90,0)
    drawFace()

#Draws stars for the sky
#x = integer
#y = integer
#Coded by Sadie and Matthew
def buildStars(x,y):
    sadie.color("#ffd11a")
    for i in range(10):
        x=random.randint(-500,500)
        y=random.randint(0,500)
        for index in range(5):
            sadie.penup()
            sadie.goto(x,y)
            sadie.pendown()
            sadie.left(72)
            sadie.forward(50)
            sadie.right(144)
            sadie.forward(50)
            sadie.backward(50)

#Draws the background with stars
#color = a hexadecimal string with a hash tag symbol prefix symbolizing hex color
#Coded by James
def drawBackground():
    james.color('#00c5ff')
    turtlegoto(-600,30)
    james.begin_fill()
    betterForward(0,1200)
    betterForward(90,600)
    betterForward(180,1200)
    betterForward(270,600)
    james.end_fill()
    buildStars(random.randint(-500,500),random.randint(0,500))
    james.color('#f6dcbd')
    turtlegoto(-600,30)
    james.begin_fill()
    betterForward(0,1200)
    betterForward(270,600)
    betterForward(180,1200)
    betterForward(90,600)
    james.end_fill()

#Draws the pathways
#Coded by James
def drawPathways():
    james.color('#7f8274')
    turtlegoto(-600,-100)
    james.begin_fill()
    betterForward(355,1200)
    betterForward(270,600)
    betterForward(180,1200)
    betterForward(90,600)
    james.end_fill()
    turtlegoto(230,0)
    james.begin_fill()
    betterForward(0,40)
    betterForward(280,300)
    betterForward(180,180)
    james.end_fill()
    turtlegoto(-220,0)
    james.begin_fill()
    betterForward(180,100)
    betterForward(190,700)
    betterForward(0,350)
    james.end_fill()
    turtlegoto(-20,0)
    james.begin_fill()
    betterForward(0,45)
    betterForward(260,300)
    betterForward(180,250)
    james.end_fill()

#Draws the entire drawing
#Coded by James
def drawScene():
    drawBackground()
    drawPathways()
    spongeFullHouse()
    drawSquidHouse()
    buildPatrickHouse()

#Main
drawScene() 
