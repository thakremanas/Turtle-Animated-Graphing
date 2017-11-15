import turtle

data={}
### Prompt for input ###
title=input("Enter the path to the file (For example: data/huskies2016.txt  or  data/sample_text)  : ")

#Define get_max_value function
def get_max_value(filePath,featureVal):
    """Gets data from the file using getdata(filePath, featureVal) function and returns the maximum value of the observation in integer """
    dataSet = getData(filePath,featureVal)
    maxData = 0
    for a,b in data.items():
        if(int(b) > maxData):
            maxData = int(b)
    return maxData

#define count_observations
def count_observations(filePath,featureVal) :
    """The function gets the data from file and looks of the length of the dataset using len command and returns it"""
    dataSet = getData(filePath,featureVal)
    return len(dataSet)

#define getData
def getData(filePath,featureVal):
   """Reads data from the file line by line and stores in label, feature1 and feauture 2. returns the data after reading entire file"""
    #Open file with the path
   f = open(filePath, 'r')
   while True:
        
        label=f.readline()
        if label=='':
                break;
        feature1 = f.readline()
        feature2 = f.readline() #skipping the 2nd feature
        if(featureVal == "feature 1"):
            data[label]=feature1
        elif(featureVal == "feature 2"):
            data[label]=feature2
   return data

#Function : draw_axes
def draw_axes(turtle,xpos,ypos,height,barWidth,maxVal,xnum):
    """Calls functions draw_x_axis and draw_y_axis. Simply draws the axes """
    turtle.setpos(xpos,ypos)
    draw_y_axis(turtle,height,maxVal)
    #call x axis function
    gapLength = 10
    width = (barWidth+gapLength)*xnum
    draw_x_axis(turtle,width)
    
#Function : draw_y_axes    
def draw_y_axis(turtle,height,maxVal):
    """Draws Y axis and tickers. uses while loop to guide the movement of turtle till the number of blocks is reached """
    blocks = 10 #setting the tickers to 10
    number = float(maxVal/blocks)
    moveByPixel = height/blocks
    i=1
    turtle.left(90)
    while i <= blocks:
        turtle.forward(moveByPixel)
        turtle.write(round(number*i,2),move=False,align="right",font=("Arial", 12, "normal"))
        turtle.right(90)
        turtle.forward(10)
        turtle.backward(10)
        turtle.left(90)
        i=i+1
    turtle.backward(height)

#Function : draw_x_axes
def draw_x_axis(turtle,width):
    """Draws X axis """
    turtle.right(90)
    turtle.forward(width)
    turtle.backward(width)

#Function : draw_rectangle
def draw_rectangle(turtle,height,width,color):
    """Draws a rectangle """
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.end_fill()


#Function : draw_bars
def draw_bars(turtle,gap,xnum,width,ymax,height,data):
    """Calls draw_rectangle function and uses for loop to repeat the action. Also fills color using choose_color function to fill them """
    i=1
    pixel=ymax/height 
    recs=[]#bar height
    labels=[]
    for a,b in data.items():
        x =  (float(b)/pixel)
        turtle.down()
        turtle.fd(gap)
        color = choose_color(i)
        draw_rectangle(turtle,x,width,color)
        turtle.up()
        add_label(turtle,width,50,a)
        #turtle.fd(width)
        i=i+1

#Function : add_label        
def add_label(turtle,width,baseHeight,label):
    """Function simply add labels of established font and using turtle movements """
    turtle.rt(90)
    turtle.fd(baseHeight)
    turtle.lt(90)
    turtle.fd(width/2)
    turtle.write(label, move=False, align="center", font=("Arial", 12, "normal"))
    turtle.fd(width/2)
    turtle.lt(90)
    turtle.fd(baseHeight)
    turtle.rt(90)
    
#Function : choose_color	
def choose_color(selector):
    """Chooses color based on the i value (from line 100) as input for selector """
    #Color pallets choosen online for colors[]
    colors=['#CC9933','#6699CC','#CC3399','#996633','#336699','#0099CC','#FF9999','#CC0066','#99CC00','#CC3399','#009933','#996699','#CCFFFF','#FFCC33','#FF33CC','#336600','#CCCC44','#990033','#FFFF99','#9999CC','#FFCC33','#333333','#9999FF','#993399','#CC99CC','#CC9966','#FF99CC','#CCCC66','#990033','#FFFFFF','#999900','#00CC00','#333399','#993333','#F00000','#999933','#CCCC99','#FF9933','#006699','#CC3366','#0099CC','#9999CC','#999999','#66CC66','#996699','#FF6600','#006600','#CCFF66','#3366CC','#666666','#FF9933','#663300','#663399','#33CC99','#FF9966','#CCFFCC','#FF9900','#99CC99','#999999','#CCCC66','#FFFFFF','#CC6600','#FFFF33','#CC6600','#009966','#339999','#336633','#000000','#CC9900','#66CCCC','#99CC33','#FFCCFF','#CC9966','#996633','#660099','#993333','#660066','#6666CC','#333366','#FFFFCC','#9933CC','#FFFFCC','#003300','#0099FF','#336600','#CC3333','#663366','#CCFFCC','#FFCC00','#009933','#663333','#6666FF','#66CC99','#99CC99','#339966','#000066','#666699','#FF9999','#9999FF','#6666CC','#66CCCC','#663333','#000066','#0099FF','#006600','#99CC00','#99CC33','#FFFF00','#009999','#990066','#CCFF99','#006633','#CCCC00','#003333','#CC9933','#0066CC','#CC9999','#339933','#0000FF',"#search",'#9966CC','#f8f8f8','#996666','#FFFF33','#669966','#CCFF00','#0000FF','#660000','#333366','#006633','#669966','#9933FF','#33CC33','#339999','#CCCCFF','#996666','#FF9900','#996600','#66CC99','#669933','#006699','#333300','#333300','#CC0033','#660066','#336633','#CCCC33','#336699','#CC6666','#F00000','#CCCCFF','#660033','#99CC66','#6699FF','#669933','#FFFF66','#999900','#660099','#66CC66','#CCCCCC','#FF6666','#CCCC33','#009966','#FFCCCC','#FFCCFF','#999933','#36b0f3','#003333','#9966CC','#666633','#F8F8F8','#CCCCCC','#FF33CC','#99CCFF','#0000CC','#993366','#330033','#336666','#666600','#660000','#CC9999','#990066','#99CC66','#99CCCC','#99CCFF"','#993366','#FFFF00','#33CC99','#CC3366','#663300','#FFCC99','#003366','#666633','#CC3333','#669999','#CCFF00','#3399CC','#999966','#669999','#f3f3f3','#339933','#3366CC','#CCCC00','#CCFF99','#666699','#993399','#333399','#9933FF','#66CCFF','#336666','#CC0066','#66CCFF','#FF3399','#FF0033','#663366','#FFFF99','#9933CC','#CC6699','#FFCC99','#0000CC','#FF3399','#FF6666','#330033','#0066CC','#FF9966','#003399','#6699FF','#CC6633','#003399','#999966','#996600','#f9f9f9','#CCCC99','#FFCCCC']
    return colors[selector%235] 
    
	
### Create and Setup the Window ###
featureVal = "feature 1"
xnum = count_observations(title,featureVal)
ymax=get_max_value(title,featureVal)
window = turtle.Screen()
width=50+130*(xnum+1) #(the space between each bar is 30, the width of each bar is 100)
window.setup(900,500,0,0) #specifying window size
window.title(title) #give it the inputted title which shows up on top of window pop up
turtle.speed(5)
turtle.up()
turtle.setpos(-350,-200)
turtle.pendown() 
barWidth = 40
graphHeight = 400
#drawing axes
draw_axes(turtle,-350,-200,graphHeight,barWidth,ymax,xnum)

#drawing bar graph
dataSet = getData(title,featureVal)
draw_bars(turtle,10,xnum,barWidth,ymax,graphHeight,dataSet)

turtle.mainloop()                  



