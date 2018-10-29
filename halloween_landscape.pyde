x = 0

def setup():
    global moon
    global landscape
    global right
    global left
    global bigfoot
    global devil
    global freddy
    global zombie
    global clown
    global vampire
    global tophat
    global jump
    global imagelist
    size(1366, 768)
    moon = loadImage("half_moon__.png")
    landscape = loadImage("halloween background.png")
    left = loadImage("left.png")
    right = loadImage("right.png")
    bigfoot = loadImage("bigfoot.png")
    devil = loadImage("devil.png")
    freddy = loadImage("freddy.png")
    zombie = loadImage("zombie.png")
    clown = loadImage("clown.png")
    vampire = loadImage("vampire.png")
    tophat = loadImage("tophatguy.png")
    jump = loadImage("jump.png")
    imagelist = [bigfoot, devil, freddy, zombie, clown, vampire, tophat]
    
def draw():
    global x
    global xdict
    m = 0
    xdict = {bigfoot : x+100, devil : x+400, freddy : x+700, zombie : x+1000, clown : x+1300, vampire : x+1600, tophat : x+1900}
    image(landscape, x, 0)
    image(moon, 1200, 25, 150, 150)
    for character in imagelist:
        image(character, xdict[character], 600, character.width/(character.height/200), 200)
    if x != 0:
        image(left, 10, 350, 100, 100)
    if x != -1100:
        image(right, 1256, 350, 100, 100)
    if x + 5 <= 0 and mouseX <= 110:
        x += 5
    if x - 5 >= -1100 and mouseX >= 1256:
        x -= 5
    if mousePressed:
        for character in imagelist:
            if mouseX > xdict[character] and mouseX < xdict[character] + character.width/(character.height/200) and mouseY >= 600:
                textSize(32)
                text("press space", xdict[character], 550)
    if keyPressed:
        if key == " ":
            image(jump, 0, 0, 1366, 768)
    
