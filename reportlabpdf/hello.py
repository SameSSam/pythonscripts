from math import radians
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import letter, A4 

# myCanvas = Canvas("myfile.pdf", pagesize=letter)
# width,height = letter 

def hello(c):
    from reportlab.lib.units import inch 
    c.translate(inch,inch)
    c.setFont("Helvetica",14)
    c.setStrokeColorRGB(0.2,0.5,0.3)
    c.setFillColorRGB(1,0,1)
    c.line(0,0,0,1.7*inch)
    c.line(0,0,1*inch,0)
    c.rect(0.2*inch,0.2*inch,1*inch,1.5*inch,fill=1)
    c.rotate(90)
    c.setFillColorRGB(0,0,0.77)
    c.drawString(0.3*inch, -2*inch,"Hello World")

def coords(canvas):
    from reportlab.lib.units import inch 
    from reportlab.lib.colors import pink,black, red,blue,green 

    c = canvas 
    c.setStrokeColor(pink)
    c.grid([inch,2*inch,3*inch,4*inch],[0.5*inch,inch,1.5*inch,2*inch,2.5*inch])
    c.setStrokeColor(black)
    c.setFont('Times-Roman', 20)
    c.drawString(0,0,"(0,0) the origin")
    c.drawString(2.5*inch,inch,"(2.5,1) in inches")
    c.drawString(4*inch,2.5*inch,"(4,2.5)")
    c.setFillColor(red)
    c.rect(0,2*inch,0.2*inch,0.3*inch,fill=1)
    c.setFillColor(green)
    c.circle(4.5*inch,0.4*inch,0.2*inch,fill=1)

def translate(canvas):
    from reportlab.lib.units import cm
    canvas.translate(2.3*cm,0.3*cm)
    coords(canvas)

def scale(canvas):
    canvas.scale(0.75,0.5)
    coords(canvas)

def scaletranslate(canvas):
    from reportlab.lib.units import inch 

    canvas.setFont('Courier-BoldOblique',12)
    canvas.saveState()

    canvas.scale(0.3,0.5)
    canvas.translate(2.4*inch,1.5*inch)
    canvas.drawString(0,2.7*inch,"Scale then translate")
    coords(canvas)

    canvas.restoreState()
    canvas.translate(2.4*inch,1.5*inch)
    canvas.scale(0.3,0.5)
    canvas.drawString(0,2.7*inch,"translate then scale")
    coords(canvas)

def colorsRGB(canvas):
    from reportlab.lib import colors 
    from reportlab.lib.units import inch 

    black = colors.black 
    y=x=0;dy=inch*3/4.0;dx=inch*5.5/5;w=h=dy/2;rdx=(dx-w)/2
    rdy=h/5.0;texty=h+2*rdy 
    canvas.setFont("Helvetica",10)
    for [namedcolor,name] in (
        [colors.lavenderblush,"lavenderblush"],
        [colors.lawngreen,"lawngreen"],
        [colors.lemonchiffon,"lemonchiffon"],
        [colors.lightblue,"lightblue"],
        [colors.lightcoral,"lightcoral"]):
        canvas.setFillColor(namedcolor)
        canvas.rect(x+rdx,y+rdy,w,h,fill=1)
        canvas.setFillColor(black)
        canvas.drawCentredString(x+rdx/2,y+texty,name)
        x = x+dx
    y=y+dy;x=0
    for rgb in [(1,0,0),(0,1,0),(0,0,1),(0.5,0.3,0.1),(0.4,0.5,0.3)]:
        r,g,b=rgb
        canvas.setFillColorRGB(r,g,b)
        canvas.rect(x+rdx,y+rdy,w,h,fill=1)
        canvas.setFillColor(black)
        canvas.drawCentredString(x+rdx,y+texty,"r%s g%s b%s"%rgb)
        x= x + dx
    y = y+dy;x=0
    for gray in (0.0,0.25,0.50,0.75,1.0):
        canvas.setFillGray(gray) 
        canvas.rect(x+rdx,y+rdy,w,h,fill=1)
        canvas.setFillColor(black)
        canvas.drawCentredString(x+dx/2,y+texty,"gray: %s"%gray)
        x = x + dx 

def alpha(canvas):
    from reportlab.graphics.shapes import Rect
    from reportlab.lib.colors import Color, black, blue, red 

    red50transparent = Color(100,0,0,alpha=0.5)
    c = canvas
    c.setFillColor(black)
    c.setFont('Helvetica',14)
    c.drawString(25,180,"Solid")
    c.rect(25,25,100,100,fill=True,stroke=False)
    c.setFillColor(red)
    c.rect(100,75,100,100,fill=True,stroke=False)
    c.setFillColor(black)
    c.drawString(225,180,'Tranparent')
    c.setFillColor(blue)
    c.rect(225,25,100,100,fill=True,stroke=False)
    c.setFillColor(red50transparent)
    c.rect(300,75,100,100,fill=True,stroke=False)

def spumoni(canvas):
    from reportlab.lib.units import inch 
    from reportlab.lib.colors import pink,green,brown,white

    x=0;dx=0.4*inch
    for i in range(4):
        for color in (pink,green,brown):
            canvas.setFillColor(color)
            canvas.rect(x,0,dx,3*inch,stroke=0,fill=1)
            x = x + dx
    canvas.setFillColor(white)
    canvas.setFont("Helvetica",85)
    canvas.drawCentredString(2.75*inch,1.3*inch,"SPUMPNI")

def spumoni2(canvas):
    from reportlab.lib.units import inch
    from reportlab.lib.colors import pink,green,brown,white,black

    #draw the previous drawing
    spumoni(canvas)

    #now put an ice cream cone on the top of it:
    #first draw a triange (ice cream cone)
    p= canvas.beginPath()
    xcenter = 2.75*inch 
    radius = 0.45*inch 
    p.moveTo(xcenter-radius,1.5*inch)
    p.lineTo(xcenter+radius,1.5*inch)
    p.lineTo(xcenter,0)
    canvas.setFillColor(brown)
    canvas.setStrokeColor(black)
    canvas.drawPath(p,fill=1)
    #draw some circles (scoops)
    y = 1.5*inch 
    for color in (pink,green,brown):
        canvas.setFillColor(color)
        canvas.circle(xcenter,y,radius,fill=1)
        y = y + radius 

def textsize(canvas):
    from reportlab.lib.units import inch 
    from reportlab.lib.colors import magenta,red
    canvas.setFont("Times-Roman",20)
    canvas.setFillColor(red)
    canvas.drawCentredString(2.75*inch,2.5*inch,"Font size examples")
    canvas.setFillColor(magenta)
    size = 7
    y = 2.3*inch 
    x = 1.3*inch 
    
    for line in lyrics:
        canvas.setFont("Helvetica",size)
        canvas.drawRightString(x,y,"%s points:" %size)
        canvas.drawString(x,y,line)
        y= y-size*1.2 
        size = size + 1.5
    
def fonts(canvas):
    from reportlab.lib.units import inch 
    text = "Now is th time for all good men to ..."
    x = 1.8* inch 
    y = 2.7* inch 
    for font in canvas.getAvailableFonts():
        canvas.setFont(font,10)
        canvas.drawString(x,y,text)
        canvas.setFont("Helvetica",10)
        canvas.drawRightString(x-10,y,font+":")
        y = y - 13

def cursormoves1(canvas):
    from reportlab.lib.units import inch
    textobject = canvas.beginText()
    textobject.setTextOrigin(inch,2.5*inch)
    textobject.setFont("Helvetica-Oblique",16)
    for line in lyrics:
        textobject.textLine(line)
    textobject.setFillGray(0.4)
    textobject.textLines(
        """
        With many apologies to the Beach Boys 
        and anyone else who finds this objectionable
        """
    )
    canvas.drawText(textobject)

def cursormoves2(canvas):
    from reportlab.lib.units import inch
    textobject = canvas.beginText()
    textobject.setTextOrigin(inch,6*inch)
    textobject.setFont("Helvetica-Oblique",16)
    for line in lyrics:
        textobject.textOut(line)
        textobject.moveCursor(20,30)
    textobject.setFillColorRGB(0.4,0,1)
    textobject.textLines(
        """
        With many apologies to the Beach Boys 
        and anyone else who finds this objectionable
        """
    )
    canvas.drawText(textobject)

def charspace(canvas):
    from reportlab.lib.units import inch
    textobject = canvas.beginText()
    textobject.setTextOrigin(inch,6*inch)
    textobject.setFont("Helvetica-Oblique",16)
    charspace=0
    for line in lyrics:
        textobject.setCharSpace(charspace)
        textobject.textLine("%s:   %s" %(charspace,line))
        charspace = charspace+0.5 
    textobject.setFillGray(0.4)
    textobject.textLines(
        """
        With many apologies to the Beach Boys 
        and anyone else who finds this objectionable
        """
    )
    canvas.drawText(textobject)

def wordspace(canvas):
    from reportlab.lib.units import inch
    textobject = canvas.beginText()
    textobject.setTextOrigin(inch,6*inch)
    textobject.setFont("Helvetica-Oblique",16)
    wordspace=0
    for line in lyrics:
        textobject.setWordSpace(wordspace)
        textobject.textLine("%s:   %s" %(wordspace,line))
        wordspace = wordspace+2.5 
    textobject.setFillColorCMYK(0.4,0,0.4,0.2)
    textobject.textLines(
        """
        With many apologies to the Beach Boys 
        and anyone else who finds this objectionable
        """
    )
    canvas.drawText(textobject)

def horizontalscale(canvas):
    from reportlab.lib.units import inch
    textobject = canvas.beginText()
    textobject.setTextOrigin(3,2.5*inch)
    textobject.setFont("Helvetica-Oblique",16)
    horizontalscale=80
    for line in lyrics:
        textobject.setHorizScale(horizontalscale)
        textobject.textLine("%s:   %s" %(horizontalscale,line))
        horizontalscale = horizontalscale+10 
    textobject.setFillColorCMYK(0.0,0.4,0.4,0.2)
    textobject.textLines(
        """
        With many apologies to the Beach Boys 
        and anyone else who finds this objectionable
        """
    )
    canvas.drawText(textobject)

def leading(canvas):
    from reportlab.lib.units import inch
    textobject = canvas.beginText()
    textobject.setTextOrigin(3,2.5*inch)
    textobject.setFont("Helvetica-Oblique",16)
    leading=8
    for line in lyrics:
        textobject.setLeading(leading)
        textobject.textLine("%s:   %s" %(leading,line))
        leading = leading+2.5
    textobject.setFillColorCMYK(0.8,0,0,0.3)
    textobject.textLines(
        """
        With many apologies to the Beach Boys 
        and anyone else who finds this objectionable
        """
    )
    canvas.drawText(textobject)

def star(canvas,title="Title Here",aka="Coomment Here",xcenter=None,ycenter=None,nvertices=5):
    from math import pi,cos,sin
    from reportlab.lib.units import inch 

    radius = inch/3.0
    if xcenter is None: xcenter=2.75*inch
    if ycenter is None: ycenter=1.5*inch
    canvas.drawCentredString(xcenter,ycenter+1.3*radius,title)
    canvas.drawCentredString(xcenter,ycenter-1.4*radius,aka)

    p = canvas.beginPath()
    p.moveTo(xcenter,ycenter+radius)
    angle = (2*pi)*2/5.0 
    startangle = pi/2.0 
    for vertex in range(nvertices-1):
        nextangle = angle*(vertex+1) + startangle 
        x = xcenter + radius*cos(nextangle)
        y = ycenter + radius*sin(nextangle)
        p.lineTo(x,y) 
    if nvertices == 5:
        p.close()
    canvas.drawPath(p)


#Line join setting

def joins(canvas):
    from reportlab.lib.units import inch 
    #make lines big 
    canvas.setLineWidth(5)
    star(canvas,"Default: mitered join","0:pointed",xcenter = 1*inch)
    canvas.setLineJoin(1)
    star(canvas,"Round Join","1:rounded")
    canvas.setLineJoin(2)
    star(canvas,"Bevelled join","2:square",xcenter=4.5*inch)

#line cap
def caps(canvas):
    from reportlab.lib.units import inch
    #make lines big
    canvas.setLineWidth(5)
    star(canvas,"Default","no projection",xcenter=1*inch,nvertices=4)
    canvas.setLineCap(1)
    star(canvas,"Round Cap","1:ends in half circle",nvertices=4)
    canvas.setLineCap(2)
    star(canvas,"Square cap","2:projects out half a width",xcenter=4.5*inch,nvertices=4)

#dashes borkoen lines
def dashes(canvas):
    from reportlab.lib.units import inch 
    #make lines big
    canvas.setDash(6,3)
    star(canvas,"Simple Dashes","6 points on, 3 off",xcenter=1*inch)
    canvas.setDash(1,2)
    star(canvas,"Dots","One on,two off")
    canvas.setDash([1,1,3,3,1,4,4,1],0)
    star(canvas,"Cpmplex Pattern","[1,1,3,3,1,4,4,1]",xcenter=4.5*inch)
#create complex figures with path object
def penciltip(canvas,debug=1):
    from reportlab.lib.colors import tan,black,green 
    from reportlab.lib.units import inch 
    u = inch/10.0
    canvas.setLineWidth(4)
    if debug: 
        canvas.scale(2.8,2.8) #make it bigg
        canvas.setLineWidth(1) #small lines 
    canvas.setStrokeColor(black)
    canvas.setFillColor(tan)
    p = canvas.beginPath()
    p.moveTo(10*u,0)
    p.lineTo(0,5*u)
    p.lineTo(10*u,10*u)
    p.curveTo(11.5*u,10*u,11.5*u,7.5*u,10*u,7.5*u)
    p.curveTo(12*u,7.5*u,11*u,2.5*u,9.7*u,2.5*u)
    p.curveTo(10.5*u,2.5*u,11*u,0,10*u,0)
    canvas.drawPath(p,stroke=1,fill=1)
    canvas.setFillColor(black)
    p=canvas.beginPath()
    p.moveTo(0,5*u)
    p.lineTo(4*u,3*u)
    p.lineTo(5*u,4.5*u)
    p.lineTo(3*u,6.5*u)
    canvas.drawPath(p,stroke=1,fill=1)
    if debug:
        canvas.setStrokeColor(green)
        canvas.grid([0,5*u,10*u,15*u],[0,5*u,10*u])


#Rectangles,circles,ellipses
def pencil(canvas,text="No.2"):
    from reportlab.lib.colors import yellow,red,black,white 
    from reportlab.lib.units import inch 

    u = inch/10.0
    canvas.setStrokeColor(black)
    canvas.setLineWidth(4)
    #draw erasor 
    canvas.setFillColor(red)
    canvas.circle(30*u,5*u,5*u,stroke=1,fill=1)
    #draw all else but the tip(mainly rectangles with different fills)
    canvas.setFillColor(yellow)
    canvas.rect(10*u,0,20*u,10*u,stroke=1,fill=1)
    canvas.setFillColor(black)
    canvas.rect(23*u,0,8*u,10*u,fill=1)
    canvas.roundRect(14*u,3.5*u,8*u,3*u,1.5*u,stroke=1,fill=1)
    canvas.setFillColor(white)
    canvas.rect(25*u,u,1.2*u,8*u,fill=1,stroke=0)
    canvas.rect(27.5*u,u,1.2*u,8*u,fill=1,stroke=0)
    canvas.setFont("Times-Roman",3*u)
    canvas.drawCentredString(18*u,4*u,text)
    #now draw the tip
    penciltip(canvas,debug=0)
    #draw broken lines across the body
    canvas.setDash([10,5,16,10],0)
    canvas.line(11*u,2.5*u,22*u,2.5*u)
    canvas.line(22*u,7.5*u,12*u,7.5*u)

#bezier 
def bezier(canvas):
    from reportlab.lib.colors import yellow,green,red,black 
    from reportlab.lib.units import inch 
    i = inch
    d= i/4 
    #define the bezier curve control points
    x1,y1,x2,y2,x3,y3,x4,y4=d,1.5*i,1.5*i,d,3*i,d,5.5*i-d,3*i-d
    #draw a figure encolosing the control points 
    canvas.setFillColor(yellow)
    p = canvas.beginPath()
    p.moveTo(x1,y1)
    for (x,y) in [(x2,y2),(x3,y3),(x4,y4)]:
        p.lineTo(x,y)
    canvas.drawPath(p,fill=1,stroke=0)
    #draw the tangent lines
    canvas.setLineWidth(inch*0.1)
    canvas.setStrokeColor(green)
    canvas.line(x1,y1,x2,y2)
    canvas.setStrokeColor(red)
    canvas.line(x3,y3,x4,y4)
    #finally draw the curve
    canvas.setStrokeColor(black)
    canvas.bezier(x1,y1,x2,y2,x3,y3,x4,y4)
    
#smoothly joining bezier curve sequences 
def bezier2(canvas):
    from reportlab.lib.units import inch 
    from reportlab.lib.colors import yellow,green,red,black 
    #make a sequence of control points
    xd,yd=5.5*inch/2, 3*inch/2 
    xc,yc=xd,yd 
    dxdy = [(0,0.33),(0.33,0.33),(0.75,1),(0.875,0.875),(0.875,0.875),(1,0.75),(0.33,0.33),(0.33,0)]
    pointlist=[]  #???????????????
    for xoffset in (1,-1):
        yoffset = xoffset
        for (dx,dy) in dxdy:  #????????????8????????????,????????????16????????????
            px = xc + xd*xoffset*dx
            py = yc + yd*yoffset*dy
            pointlist.append((px,py))
        yoffset = -xoffset
        for (dy,dx) in dxdy: #????????????8???????????????????????????16????????????(x,y??????????????????)
            px = xc+xd*xoffset*dx
            py = yc+yd*yoffset*dy
            pointlist.append((px,py))
    #draw tangent lines and curves 
    canvas.setLineWidth(inch*0.1)
    while pointlist:
        #??????????????????????????????????????????????????????
        [(x1,y1),(x2,y2),(x3,y3),(x4,y4)] = pointlist[:4]
        del pointlist[:4]
        canvas.setLineWidth(inch*0.1)
        canvas.setStrokeColor(green)
        canvas.line(x1,y1,x2,y2)  #?????????????????????
        canvas.setStrokeColor(red)
        canvas.line(x3,y3,x4,y4)  #??????????????????
        #finally draw the curve,????????????
        canvas.setStrokeColor(black)
        canvas.bezier(x1,y1,x2,y2,x3,y3,x4,y4)

def arcs(canvas):
    from reportlab.lib.units import inch 
    canvas.setLineWidth(4)
    canvas.setStrokeColorRGB(0.8,1,0.6)
    #draw rectangles enclosing the arcs
    canvas.rect(inch,inch,1.5*inch,inch)
    canvas.rect(3*inch,inch,inch,1.5*inch)
    canvas.setStrokeColorRGB(0,0.2,0.4)
    canvas.setFillColorRGB(1,0.6,0.8)
    p = canvas.beginPath()
    p.moveTo(0.2*inch,0.2*inch)
    p.arcTo(inch,inch,2.5*inch,2*inch,startAng=-30,extent=135)
    p.arc(3*inch,inch,4*inch,2.5*inch,startAng=-60,extent=300)
    canvas.drawPath(p,fill=1,stroke=1)

def variousshapes(canvas):
    from reportlab.lib.units import inch 
    inch = int(inch)
    canvas.setStrokeGray(0.5)
    canvas.grid(range(0,int(11*inch/2),int(inch/2)),range(0,int(7*inch/2),int(inch/2)))
    canvas.setLineWidth(4)
    canvas.setStrokeColorRGB(0,0.2,0.7)
    canvas.setFillColorRGB(1,0.6,0.8)
    p = canvas.beginPath()
    p.rect(0.5*inch,0.5*inch,0.5*inch,2*inch)
    p.circle(2.75*inch,1.5*inch,0.3*inch)
    p.ellipse(3.5*inch,0.5*inch,1.2*inch,2*inch)
    canvas.drawPath(p,fill=1,stroke=1)

def closingfigures(canvas):
    from reportlab.lib.units import inch 
    h = inch/3.0;k=inch/2.0
    canvas.setStrokeColorRGB(0.2,0.3,0.5)
    canvas.setFillColorRGB(0.8,0.6,0.2)
    canvas.setLineWidth(4)
    p = canvas.beginPath()
    for i in (1,2,3,4):
        for j in (1,2):
            xc,yc = inch*i,inch*j
            p.moveTo(xc,yc)
            p.arcTo(xc-h,yc-k,xc+h,yc+k,startAng=0,extent=60*i)
            #close only the first one, not the second one 
            if j==1:
                p.close()
    canvas.drawPath(p,fill=1,stroke=1)


def hand(canvas,debug=1,fill=0):
    (startx,starty) = (0,0)
    curves = [
    ( 0, 2), ( 0, 4), ( 0, 8), # back of hand
    ( 5, 8), ( 7,10), ( 7,14),
    (10,14), (10,13), ( 7.5, 8), # thumb
    (13, 8), (14, 8), (17, 8),
    (19, 8), (19, 6), (17, 6),
    (15, 6), (13, 6), (11, 6), # index, pointing
    (12, 6), (13, 6), (14, 6),
    (16, 6), (16, 4), (14, 4),
    (13, 4), (12, 4), (11, 4), # middle
    (11.5, 4), (12, 4), (13, 4),
    (15, 4), (15, 2), (13, 2),
    (12.5, 2), (11.5, 2), (11, 2), # ring
    (11.5, 2), (12, 2), (12.5, 2),
    (14, 2), (14, 0), (12.5, 0),
    (10, 0), (8, 0), (6, 0), # pinky, then close
    ]
    from reportlab.lib.units import inch 
    if debug:canvas.setLineWidth(6)
    u = inch*0.2
    p = canvas.beginPath()
    p.moveTo(startx,starty)
    ccopy = list(curves)
    while ccopy:
        [(x1,y1),(x2,y2),(x3,y3)] = ccopy[:3]
        del ccopy[:3]
        p.curveTo(x1*u,y1*u,x2*u,y2*u,x3*u,y3*u)
    p.close()
    canvas.drawPath(p,fill=fill)
    if debug:
        from reportlab.lib.colors import red,green
        (lastx,lasty) = (startx,starty)
        ccopy = list(curves)
        while ccopy:
            [(x1,y1),(x2,y2),(x3,y3)] = ccopy[:3]
            del ccopy[:3]
            canvas.setStrokeColor(red)
            canvas.line(lastx*u,lasty*u,x1*u,y1*u)
            canvas.setStrokeColor(green)
            canvas.line(x2*u,y2*u,x3*u,y3*u)
            (lastx,lasty) = (x3,y3)

def hand2(canvas):
    canvas.translate(20,10)
    canvas.setLineWidth(3)
    canvas.setFillColorRGB(0.1,0.3,0.9)
    canvas.setStrokeGray(0.5)
    hand(canvas,debug=0,fill=1)



#below starts the main program:
c = canvas.Canvas('hello.pdf')
lyrics = [
    "well she hit Net Solutions", "and she registered her own .com site now",
    "and filled it up with yahoo profile pics", "she snarfed in one night now",
    "and she made 50 million when Hugh Hefner", "bought up the rights now",
    "and she'll have fun fun fun", "til her Daddy takes the keyboard away",
]
hand2(c)
c.showPage()
c.save()