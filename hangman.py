from turtle import *
def startup():
     win=Screen()
     setup(width=.9, height=0.9, startx=None, starty=None)
     win.title("Hangman")
     win.clear()
     hideturtle()
     speed(10)
     pencolor("black")
     penup()
     origin=drawGallows()
     clearStk(incorrect)
     return (win,origin)

def moveTurtle(face,units):
     pendown()
     setheading(face)
     forward(units)
     penup()
     return

def drawGallows():
     moveTurtle(right,2*unit)
     goto(pos()[0]//2,pos()[1])
     moveTurtle(up,4*unit)
     moveTurtle(right,2*unit)
     moveTurtle(down,0.4*unit)
     return pos()

def drwHead(origin):
     goto(origin[0]-0.2*unit,origin[1]-0.2*unit)
     pendown()
     circle(0.2*unit)
     penup()
     return pos()

def drwTorso(origin):
     goto(origin[0]+0.2*unit,origin[1]-0.2*unit)
     moveTurtle(down,unit)
     return pos()

def drwLArm(origin):
     goto(origin[0],origin[1]+0.6*unit)
     moveTurtle(left,0.4*unit)
     goto(origin)
     return origin

def drwRArm(origin):
     goto(origin[0],origin[1]+0.6*unit)
     moveTurtle(right,0.4*unit)
     goto(origin)
     return origin

def drwLLeg(origin):
     goto(origin[0],origin[1]+0.1*unit)
     moveTurtle(leftTilt,0.6*unit)
     goto(origin)
     return origin

def drwRLeg(origin):
     goto(origin[0],origin[1]+0.1*unit)
     moveTurtle(rightTilt,0.6*unit)
     goto(origin)
     return origin
#Global data
up=90
down=270
leftTilt=225
left=180
rightTilt=315
right=0
unit=50
def makeStk():
    return ['stack',[1,2,3]]
def elements(x):
    return x[1]
def push(stk,el):
    return elements(stk).append(el)
def clearStk(x):
    del x[1][:]
def fullStk(x):
    return len (x[1])==6

def getwords():
    lst=[]
    lst=lst+[input("enter a word  ")]
    lst=lst+[input("enter a word  ")]
    lst=lst+[input("enter a word  ")]
    return lst
def maskletters(mask,word):
    for i in word:
         penup()
         write (mask,move=True,align="left", font=("ariel",30,"normal"))
         goto(pos()+(5,0))
def showcorrect(char,word):
    
    for i in word:
        if char==i:
             penup()
             write (char,move=True,align="left", font=("ariel",30,"normal"))
             goto(pos()+(5,0))
        elif i!=char:
             penup()
             write ("_",move=True,align="left", font=("ariel",30,"normal"))
             goto(pos()+(5,0))


def getGuess():
     d=textinput("Hangman","Enter a letter")
     if len(d)==1 and d.islower():
          return d
     else:
          return getGuess()

def goodguess(let,word):
    if word=='':
        return 0
    elif let==word[0]:
        return 1+goodguess(let,word[1:])
    else:
       return goodguess(let,word[1:])

def displayWord(char,word,func):
     
     return func(char,word)


incorrect=makeStk()



def play():
     guesslst=[]
     guesses=getwords()
     startup()
     galpos=pos()
     goto(-150,-100)
     displayWord("_",guesses[0],maskletters)
     writepos=(-150,-100)
     while len(incorrect[1])<6:
          guess=getGuess()
          num=goodguess(guess,guesses[0])
          if num<1:
               incorrect[1]+=[guess]
               step=len(incorrect[1])
               drawbody[step](galpos)
               galpos=pos()
               guesslst=guesslst+[guess]
          for x in guesslst:
               for y in guesses[0]:
                    if x==y:
                         write("YOU HAVE WON",move=True,aligh='left',font=('ariel',40,"italic"))
          for i in guesses[0]:
               if guess==i:
                    goto(writepos)
                    displayWord(i,guesses[0],showcorrect)
          

         
drawbody={1:drwHead,2:drwTorso,3:drwLArm,4:drwRArm,5:drwLLeg,6:drwRLeg}

