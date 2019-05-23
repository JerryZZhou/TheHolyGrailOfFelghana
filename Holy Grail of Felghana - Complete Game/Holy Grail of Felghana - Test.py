
#The Holy Grail Inc.
#The Holy Grail of Felghana
#Jerry, Kenny, Joyce, Justin
#Felix will try to collect the sword of light and defeat the generals to collect all 2 keys and defeat Jax.

from gamelib import*

#Variables
game = Game(1200,800,"Holy Grail of Felghana")

bk = Image("level1bk.png",game)
bk.resizeTo(game.width,game.height)

bk2 = Image("level2bk.png",game)
bk2.resizeTo(game.width,game.height)

bk3 = Image("level2bk.png",game)
bk3.resizeTo(game.width,game.height)

bk4 = Image("level4bk.png",game)

startbk = Image("startingbk.jpg",game)
startbk.resizeTo(game.width,game.height)

felixforward = Animation("armorlessfelix walk forward.png",9,game,571/9,68)
#felixforward.resizeBy(10)
felixforward.visible = False
felixforward.moveTo(10,350)

felixdown = Animation("armorlessfelix walk down.png",9,game,571/9,68)
#felixdown.resizeBy(10)
felixdown.visible = False
felixdown.moveTo(10,350)

felixleft = Animation("armorlessfelix walk left.png",9,game,571/9,68)
#felixleft.resizeBy(10)
felixleft.visible = False
felixleft.moveTo(10,350)

felixright = Animation("armorlessfelix walk right.png",9,game,571/9,68)
#felixright.resizeBy(10)
felixright.visible = False
felixright.moveTo(10,350)

felixforwarda = Animation("armorlessfelix attack forward.png",6,game,394/6,61)
#felixforwarda.resizeBy(10)
felixforwarda.visible = False
felixforwarda.moveTo(10,350)

felixdowna = Animation("armorlessfelix attack down.png",6,game,394/6,61)
#felixdowna.resizeBy(10)
felixdowna.visible = False
felixdowna.moveTo(10,350)

felixlefta = Animation("armorlessfelix attack left.png",6,game,394/6,61)
#felixlefta.resizeBy(10)
felixlefta.visible = False
felixlefta.moveTo(10,350)

felixrighta = Animation("armorlessfelix attack right.png",6,game,394/6,61)
#felixrighta.resizeBy(10)
felixrighta.visible = False
felixrighta.moveTo(10,350)

armorfelixforward = Animation("Felix walk forward.png",9,game,571/9,62)
armorfelixforward.resizeBy(-28)
armorfelixforward.visible = False

armorfelixdown = Animation("FELIX walk down.png",9,game,571/9,62)
armorfelixdown.resizeBy(-28)
armorfelixdown.visible = False

armorfelixleft = Animation("FELIX walk left.png",9,game,571/9,62)
armorfelixleft.resizeBy(-28)
armorfelixleft.visible = False

armorfelixright = Animation("FELIX walk right.png",9,game,571/9,62)
armorfelixright.resizeBy(-28)
armorfelixright.visible = False

armorfelixforwarda = Animation("FELIX attack forward.png",6,game,1172/6,124)
armorfelixforwarda.resizeBy(-28)
armorfelixforwarda.visible = False

armorfelixdowna = Animation("FELIX attack down.png",6,game,1172/6,124)
armorfelixdowna.resizeBy(-28)
armorfelixdowna.visible = False

armorfelixlefta = Animation("FELIX attack left.png",6,game,1172/6,124)
armorfelixlefta.resizeBy(-28)
armorfelixlefta.visible = False

armorfelixrighta = Animation("FELIX attack right.png",6,game,1172/6,124)
armorfelixrighta.resizeBy(-28)
armorfelixrighta.visible = False

title = Image("title.png",game)
title.resizeBy(-20)
title.moveTo(600,300)

play = Image("play.png",game)
play.resizeBy(-20)
play.moveTo(600,400)

howto = Image("howto.png",game)
howto.resizeBy(-20)
howto.moveTo(600,500)

howtoplay = Image("howtoplay.jpg",game)
howtoplay.resizeTo(game.width,game.height)
howtoplay.visible = False

sword = Image("Sword of Light2.png",game)
sword.resizeBy(20)
sword.moveTo(600,350)

might = Image("might.png",game)
might.resizeBy(-80)
might.visible = False

objective = Image("Objective.png",game)
objective.moveTo(600,25)
objective.resizeBy(-75)

objective2 = Image("objective 2.png",game)
objective2.moveTo(600,25)
objective2.resizeBy(-75)

objective3 = Image("objective3.png",game)
objective3.moveTo(600,25)
objective3.resizeBy(-75)

objective4 = Image("objective4.png",game)
objective4.moveTo(600,25)
objective4.resizeBy(-75)

congrats = Image("congrats.png",game)
congrats.resizeBy(-20)
congrats.moveTo(600,400)

dwarflord = Animation("lorddwarf.png",4,game,64,360/4)
dwarflord.moveTo(1275,400)
dwarflord.resizeBy(60)

atlas = Image("Atlas.png",game)
atlas.setSpeed(1,180)
atlas.moveTo(600,-100)
atlas.resizeBy(-20)

atlasattack = Animation("AtlasAttack.png",23,game,4250/5,4250/5)
atlasattack.setSpeed(1,180)
atlasattack.moveTo(600,-100)
atlasattack.visible = False
atlasattack.resizeBy(-20)

skey = Image("skey.png",game)
skey.resizeBy(20)
skey.visible = False
skey.moveTo(600,500)

kronos = Animation("WalkKronos.png",15,game,1020/4,840/4)
kronos.resizeBy(20)
kronos.moveTo(1275,400)

kronosattack = Animation("AttackKronos.png",15,game,1635/5,1370/5)
kronosattack.resizeBy(20)
kronosattack.moveTo(1275,400)
kronosattack.visible = False

ckey = Image("ckey.png",game)
ckey.resizeBy(20)
ckey.visible = False
ckey.moveTo(600,500)

jax = Animation("JaxWalk.png",24,game,1000/5,1000/5)
jax.resizeBy(20)
jax.moveTo(1175,400)

jaxattack = Animation("JaxAttack.png",24,game,1000/5,1000/5)
jaxattack.resizeBy(20)
jaxattack.moveTo(1175,400)
jaxattack.visible = False

gameover = Image("gameover.jpg",game)
gameover.resizeTo(game.width,game.height)

levelover = Image("levelover1.png",game)
levelover.resizeTo(game.width,game.height)

island = Image("island.png",game)
island.resizeBy(300)
island.moveTo(600,500)

beam = Image("beam.png",game)
#beam.visible = False
beam.resizeBy(20)
beam.moveTo(1300,900)

speed = randint(2,4)

font = Font(black,12,white,"Times New Roman")
font1 = Font(black,12,yellow,"Times New Roman")

speed = 0

#score
Might = 0
Items = 0

#lists
adwarf = []
bdwarf = []
cdwarf = []
ddwarf = []
edwarf = []
level2 = []
level3 = []

for index in range(5):
    adwarf.append(Animation("adwarf.png",4,game,64,256/4))

for index in range(5):
    bdwarf.append(Animation("bdwarf.png",4,game,64,256/4))

for index in range(5):
    cdwarf.append(Animation("cdwarf.png",4,game,64,256/4))

for index in range(5):
    ddwarf.append(Animation("ddwarf.png",4,game,64,256/4))
        
for index in range(5):
    edwarf.append(Animation("edwarf.png",4,game,64,256/4))

for index in range(20):
    level2.append(Image("level2m.png",game))

for index in range(20):
    level3.append(Image("level3m.png",game))

for index in range(len(level2)):
    y = -randint(200,600)
    x = randint(25,1175)
    level2[index].moveTo(x,y)

for index in range(len(level3)):
    y = -randint(200,600)
    x = randint(25,1175)
    level3[index].moveTo(x,y)

for index in range(len(adwarf)):
    y = randint(0,1200)
    x = randint(1400,1600)
    adwarf[index].moveTo(x,y)

for index in range(len(bdwarf)):
    y = randint(0,1200)
    x = -randint(200,600)
    bdwarf[index].moveTo(x,y)
    
for index in range(len(cdwarf)):
    y = randint(0,1200)
    x = randint(1400,1600)
    cdwarf[index].moveTo(x,y)

for index in range(len(ddwarf)):
    y = randint(0,1200)
    x = -randint(200,600)
    ddwarf[index].moveTo(x,y)
    
for index in range(len(edwarf)):
    edwarf[index].moveTo(x,y)
    y = randint(0,1200)
    x = -randint(200,600)
    

#Start Screen
while not game.over:
    game.processInput()
    startbk.draw()
    title.draw()
    play.draw()
    howto.draw()
    howtoplay.draw()

    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    if mouse.collidedWith(howto,"rectangle") and mouse.LeftClick:
        howtoplay.visible = True

    if mouse.collidedWith(howtoplay,"rectangle") and mouse.RightClick:
        howtoplay.visible = False
        
        
    game.update(30)

game.over = False

#Sword of Light Game Loop (Level 1)
while not game.over:
    game.processInput()
    bk.draw()
    sword.draw()
    felixforward.draw()
    felixdown.draw()
    felixleft.draw()
    felixright.draw()
    #felixright.visible = True
    felixforwarda.draw()
    felixdowna.draw()
    felixlefta.draw()
    felixrighta.draw()
    objective.draw()
    might.draw()
    beam.move()
    #adwarf[index].move()
    #bdwarf[index].move()
    #cdwarf[index].move()
    #ddwarf[index].move()
    #edwarf[index].move()
    #adwarf[index].moveTowards(felixforward,3)
    #bdwarf[index].moveTowards(felixforward,3)
    #cdwarf[index].moveTowards(felixforward,3)
    #ddwarf[index].moveTowards(felixforward,3)
    #edwarf[index].moveTowards(felixforward,3)

 
#Movement
    if keys.Pressed[K_w]:
        felixforward.visible = True
        felixleft.visible = False
        felixright.visible = False
        felixdown.visible = False
        felixforwarda.visible = False
        felixdowna.visible = False
        felixlefta.visible = False
        felixrighta.visible = False
        felixforward.y-=4
        felixdown.y-=4
        felixleft.y-=4
        felixright.y-=4
        felixforwarda.y-=4
        felixdowna.y-=4
        felixlefta.y-=4
        felixrighta.y-=4

        
    if keys.Pressed[K_s]:
        felixforward.visible = False
        felixleft.visible = False
        felixright.visible = False
        felixdown.visible = True
        felixforwarda.visible = False
        felixdowna.visible = False
        felixlefta.visible = False
        felixrighta.visible = False
        felixforward.y+=4
        felixdown.y+=4
        felixleft.y+=4
        felixright.y+=4
        felixforwarda.y+=4
        felixdowna.y+=4
        felixlefta.y+=4
        felixrighta.y+=4
                                                                     
    if keys.Pressed[K_d]:
        felixforward.visible = False
        felixleft.visible = False
        felixright.visible = True
        felixdown.visible = False
        felixforwarda.visible = False
        felixdowna.visible = False
        felixlefta.visible = False
        felixrighta.visible = False
        felixforward.x+=4
        felixdown.x+=4
        felixleft.x+=4
        felixright.x+=4
        felixforwarda.x+=4
        felixdowna.x+=4
        felixlefta.x+=4
        felixrighta.x+=4

    if keys.Pressed[K_a]:
        felixforward.visible = False
        felixleft.visible = True
        felixright.visible = False
        felixdown.visible = False
        felixforwarda.visible = False
        felixdowna.visible = False
        felixlefta.visible = False
        felixrighta.visible = False
        felixforward.x-=4
        felixdown.x-=4
        felixleft.x-=4
        felixright.x-=4
        felixforwarda.x-=4
        felixdowna.x-=4
        felixlefta.x-=4
        felixrighta.x-=4

    if keys.Pressed[K_SPACE] and felixforward.visible:
        felixforwarda.visible = True
        felixforward.visible = False
        #beam.moveTo(felixforward.x,felixforward.y)
        #beam.rotateTowards(mouse)
        #beam.visble = True
        #beam.moveTowards(mouse,7)

    if keys.Pressed[K_SPACE] and felixleft.visible:
        felixlefta.visible = True
        felixleft.visible = False
        #beam.moveTo(felixforward.x,felixforward.y)
        #beam.rotateTowards(mouse)
        #beam.visble = True
        #beam.moveTowards(mouse,7)

    if keys.Pressed[K_SPACE] and felixright.visible:
        felixrighta.visible = True
        felixright.visible = False
        #beam.moveTo(felixforward.x,felixforward.y)
        #beam.rotateTowards(mouse)
        #beam.visble = True
        #beam.moveTowards(mouse,7)

    if keys.Pressed[K_SPACE] and felixdown.visible:
        felixdowna.visible = True
        felixdown.visible = False
        #beam.moveTo(felixforward.x,felixforward.y)
        #beam.rotateTowards(mouse)
        #beam.visble = True
        #beam.moveTowards(mouse,7)

    if keys.Pressed[K_SPACE] and felixforwarda.visible:
        beam.moveTo(felixforward.x,felixforward.y)
        beam.rotateTowards(mouse)
        beam.visble = True
        beam.moveTowards(mouse,20)

    if keys.Pressed[K_SPACE] and felixlefta.visible:
        beam.moveTo(felixforward.x,felixforward.y)
        beam.rotateTowards(mouse)
        beam.visble = True
        beam.moveTowards(mouse,20)

    if keys.Pressed[K_SPACE] and felixrighta.visible:
        beam.moveTo(felixforward.x,felixforward.y)
        beam.rotateTowards(mouse)
        beam.visble = True
        beam.moveTowards(mouse,20)

    if keys.Pressed[K_SPACE] and felixdowna.visible:
        beam.moveTo(felixforward.x,felixforward.y)
        beam.rotateTowards(mouse)
        beam.visble = True
        beam.moveTowards(mouse,20)
    

    for index in range(len(adwarf)):
        if felixforward.collidedWith(sword):
            speed = 4
        if felixleft.collidedWith(sword):
            speed = 4
        if felixright.collidedWith(sword):
            speed = 4
        if felixdown.collidedWith(sword):
            speed = 4
        if felixforwarda.collidedWith(sword):
            speed = 4
        if felixlefta.collidedWith(sword):
            speed = 4
        if felixrighta.collidedWith(sword):
            speed = 4
        if felixdowna.collidedWith(sword):
            speed = 4
    for index in range(len(adwarf)):
        adwarf[index].moveTowards(felixforward,speed)
    
        bdwarf[index].moveTowards(felixforward,speed)
    
        cdwarf[index].moveTowards(felixforward,speed)
    
        ddwarf[index].moveTowards(felixforward,speed)
    
        edwarf[index].moveTowards(felixforward,speed)
            
    for index in range(len(adwarf)):
#adwarf
        if adwarf[index].collidedWith(felixforwarda):
            adwarf[index].visible = False
            Might+=1
            Items+=1
            
        if adwarf[index].collidedWith(felixlefta):
            adwarf[index].visible = False
            Might+=1
            Items+=1
            
        if adwarf[index].collidedWith(felixrighta):
            adwarf[index].visible = False
            Might+=1
            Items+=1
            
        if adwarf[index].collidedWith(felixdowna):
            adwarf[index].visible = False
            Might+=1
            Items+=1
            
#bdwarf
        if bdwarf[index].collidedWith(felixforwarda):
            bdwarf[index].visible = False
            Might+=1
            Items+=1
            
        if bdwarf[index].collidedWith(felixlefta):
            bdwarf[index].visible = False
            Might+=1
            Items+=1

        if bdwarf[index].collidedWith(felixrighta):
            bdwarf[index].visible = False
            Might+=1
            Items+=1
            
        if bdwarf[index].collidedWith(felixdowna):
            bdwarf[index].visible = False
            Might+=1
            Items+=1
            
#cdwarf
        if cdwarf[index].collidedWith(felixforwarda):
            cdwarf[index].visible = False
            Might+=1
            Items+=1

        if cdwarf[index].collidedWith(felixlefta):
            cdwarf[index].visible = False
            Might+=1
            Items+=1

        if cdwarf[index].collidedWith(felixrighta):
            cdwarf[index].visible = False
            Might+=1
            Items+=1

        if cdwarf[index].collidedWith(felixdowna):
            cdwarf[index].visible = False
            Might+=1
            Items+=1
        
#ddwarf
        if ddwarf[index].collidedWith(felixforwarda):
            ddwarf[index].visible = False
            Might+=1
            Items+=1

        if ddwarf[index].collidedWith(felixlefta):
            ddwarf[index].visible = False
            Might+=1
            Items+=1

        if ddwarf[index].collidedWith(felixrighta):
            ddwarf[index].visible = False
            Might+=1
            Items+=1

        if ddwarf[index].collidedWith(felixdowna):
            ddwarf[index].visible = False
            Might+=1
            Items+=1
       
#edwarf
        if edwarf[index].collidedWith(felixforwarda):
            edwarf[index].visible = False
            Might+=1
            Items+=1
    
        if edwarf[index].collidedWith(felixlefta):
            edwarf[index].visible = False
            Might+=1
            Items+=1

        if edwarf[index].collidedWith(felixrighta):
            edwarf[index].visible = False
            Might+=1
            Items+=1

        if edwarf[index].collidedWith(felixdowna):
            edwarf[index].visible = False
            Might+=1
            Items+=1

#gameplay
    if felixforward.collidedWith(sword) and Might<100:
        might.visible = True

    else:
        might.visible = False
        
    if felixright.collidedWith(sword) and Might<100:
        might.visible = True
        
    if felixleft.collidedWith(sword) and Might<100:
        might.visible = True
        
    if felixdown.collidedWith(sword) and Might<100:
        might.visible = True

    if Items>=25:
        dwarflord.moveTowards(felixforward,5)
        
    if dwarflord.collidedWith(felixforwarda):
        dwarflord.health-=10
        felixforward.health-=2

    if dwarflord.collidedWith(felixrighta):
        dwarflord.health-=10
        felixforward.health-=2

    if dwarflord.collidedWith(felixdowna):
        dwarflord.health-=10
        felixforward.health-=2

    if dwarflord.collidedWith(felixlefta):
        dwarflord.health-=10
        felixforward.health-=2

    if dwarflord.collidedWith(felixforward):
        dwarflord.health-=10
        felixforward.health-=2

    if dwarflord.collidedWith(felixright):
        dwarflord.health-=10
        felixforward.health-=2

    if dwarflord.collidedWith(felixdown):
        dwarflord.health-=10
        felixforward.health-=2

    if dwarflord.collidedWith(felixleft):
        dwarflord.health-=10
        felixforward.health-=2

    if dwarflord.health<=0:
        dwarflord.visible = False
        Might = 100
        
    for index in range(len(adwarf)):
        if adwarf[index].health<=0:
            adwarf[index].visble = False
        
        if bdwarf[index].health<=0:
            bdwarf[index].visble = False

        if cdwarf[index].health<=0:
            cdwarf[index].visble = False

        if ddwarf[index].health<=0:
            ddwarf[index].visble = False

        if edwarf[index].health<=0:
            edwarf[index].visble = False
    
        if adwarf[index].collidedWith(felixforward) or adwarf[index].collidedWith(felixright)  or adwarf[index].collidedWith(felixleft) or adwarf[index].collidedWith(felixdown):
            felixforward.health-=1
    
        if bdwarf[index].collidedWith(felixforward) or bdwarf[index].collidedWith(felixright)  or bdwarf[index].collidedWith(felixleft) or bdwarf[index].collidedWith(felixdown):
            felixforward.health-=1

        if cdwarf[index].collidedWith(felixforward) or cdwarf[index].collidedWith(felixright)  or cdwarf[index].collidedWith(felixleft) or cdwarf[index].collidedWith(felixdown):
            felixforward.health-=1

        if ddwarf[index].collidedWith(felixforward) or ddwarf[index].collidedWith(felixright)  or ddwarf[index].collidedWith(felixleft) or ddwarf[index].collidedWith(felixdown):
            felixforward.health-=1

        if edwarf[index].collidedWith(felixforward) or edwarf[index].collidedWith(felixright)  or edwarf[index].collidedWith(felixleft) or edwarf[index].collidedWith(felixdown):
            felixforward.health-=1
            
        if adwarf[index].collidedWith(felixforward) or adwarf[index].collidedWith(felixright)  or adwarf[index].collidedWith(felixleft) or adwarf[index].collidedWith(felixdown):
            felixforward.health-=1
    
        if bdwarf[index].collidedWith(felixforwarda) or bdwarf[index].collidedWith(felixrighta)  or bdwarf[index].collidedWith(felixlefta) or bdwarf[index].collidedWith(felixdowna):
            felixforward.health-=1

        if cdwarf[index].collidedWith(felixforwarda) or cdwarf[index].collidedWith(felixrighta)  or cdwarf[index].collidedWith(felixlefta) or cdwarf[index].collidedWith(felixdowna):
            felixforward.health-=1

        if ddwarf[index].collidedWith(felixforwarda) or ddwarf[index].collidedWith(felixrighta)  or ddwarf[index].collidedWith(felixlefta) or ddwarf[index].collidedWith(felixdowna):
            felixforward.health-=1

        if edwarf[index].collidedWith(felixforwarda) or edwarf[index].collidedWith(felixrighta)  or edwarf[index].collidedWith(felixlefta) or edwarf[index].collidedWith(felixdowna):
            felixforward.health-=1

    game.drawText("Felix's Health :  " + str(felixforward.health),felixforward.x - 75, felixforward.y - 35,font)
    game.drawText("Felix's Might :  " + str(Might),felixforward.x - 75, felixforward.y - 50,font1)
        
    
#game over
    if felixforward.collidedWith(sword) and Might>=100:
        game.over = True

    if felixleft.collidedWith(sword) and Might>=100:
        game.over = True

    if felixright.collidedWith(sword) and Might>=100:
        game.over = True

    if felixdown.collidedWith(sword) and Might>=100:
        game.over = True

    if felixforward.health<0:
        game.over = True

    
    game.update(11)

game.over = False

#Next Level
#while not game.over and felixforward.health > 0:
    #game.processInput()
    #levelover.draw()

    #if mouse.collidedWith(levelover) and mouse.LeftClick:
        #game.over = True

    #game.update(30)
    
#game.over = False
#game.quit()

#Lose
while not game.over and felixforward.health <0:
    gameover.draw()

    game.update(30)

game.quit()

#Level 2
while not game.over and felixforward.health > 0:
    game.processInput()
    bk2.draw()
    armorfelixforward.draw()
    #armorfelixforward.visible = True
    armorfelixdown.draw()
    armorfelixleft.draw()
    armorfelixright.draw()
    armorfelixforwarda.draw()
    armorfelixdowna.draw()
    armorfelixlefta.draw()
    armorfelixrighta.draw()
    atlas.moveTowards(armorfelixforward,2)
    island.draw()
    felixforward.health = 100
    objective2.draw()
    beam.draw()

 
#Movement
    if keys.Pressed[K_w]:
        armorfelixforward.visible = True
        armorfelixleft.visible = False
        armorfelixright.visible = False
        armorfelixdown.visible = False
        armorfelixforwarda.visible = False
        armorfelixdowna.visible = False
        armorfelixlefta.visible = False
        armorfelixrighta.visible = False
        armorfelixforward.y-=3
        armorfelixdown.y-=3
        armorfelixleft.y-=3
        armorfelixright.y-=3
        armorfelixforwarda.y-=3
        armorfelixdowna.y-=3
        armorfelixlefta.y-=3
        armorfelixrighta.y-=3


    if keys.Pressed[K_s]:
        armorfelixforward.visible = False
        armorfelixleft.visible = False
        armorfelixright.visible = False
        armorfelixdown.visible = True
        armorfelixforwarda.visible = False
        armorfelixdowna.visible = False
        armorfelixlefta.visible = False
        armorfelixrighta.visible = False
        armorfelixdown.y+=3
        armorfelixforward.y+=3
        armorfelixright.y+=3
        armorfelixleft.y+=3
        armorfelixdowna.y+=3
        armorfelixforwarda.y+=3
        armorfelixrighta.y+=3
        armorfelixlefta.y+=3
                                                                     
    if keys.Pressed[K_d]:
        armorfelixforward.visible = False
        armorfelixleft.visible = False
        armorfelixright.visible = True
        armorfelixdown.visible = False
        armorfelixforwarda.visible = False
        armorfelixdowna.visible = False
        armorfelixlefta.visible = False
        armorfelixrighta.visible = False
        armorfelixleft.x+=3
        armorfelixforward.x+=3
        armorfelixdown.x+=3
        armorfelixright.x+=3
        armorfelixlefta.x+=3
        armorfelixforwarda.x+=3
        armorfelixdowna.x+=3
        armorfelixrighta.x+=3

    if keys.Pressed[K_a]:
        armorfelixforward.visible = False
        armorfelixleft.visible = True
        armorfelixright.visible = False
        armorfelixdown.visible = False
        armorfelixforwarda.visible = False
        armorfelixdowna.visible = False
        armorfelixlefta.visible = False
        armorfelixrighta.visible = False
        armorfelixright.x-=3
        armorfelixforward.x-=3
        armorfelixdown.x-=3
        armorfelixleft.x-=3
        armorfelixrighta.x-=3
        armorfelixforwarda.x-=3
        armorfelixdowna.x-=3
        armorfelixlefta.x-=3

    if keys.Pressed[K_SPACE] and armorfelixforward.visible:
        armorfelixforwarda.visible = True
        armorfelixforward.visible = False
        beam.moveTo(armorfelixforward.x,armorfelixforward.y)
        beam.rotateTowards(mouse)
        beam.visble = True
        beam.moveTowards(mouse,20)

    if keys.Pressed[K_SPACE] and armorfelixleft.visible:
        armorfelixlefta.visible = True
        armorfelixleft.visible = False
        beam.moveTo(armorfelixforward.x,armorfelixforward.y)
        beam.rotateTowards(mouse)
        beam.visble = True
        beam.moveTowards(mouse,20)


    if keys.Pressed[K_SPACE] and armorfelixright.visible:
        armorfelixrighta.visible = True
        armorfelixright.visible = False
        beam.moveTo(armorfelixforward.x,armorfelixforward.y)
        beam.rotateTowards(mouse)
        beam.visble = True
        beam.moveTowards(mouse,20)


    if keys.Pressed[K_SPACE] and armorfelixdown.visible:
       armorfelixdowna.visible = True
       armorfelixdown.visible = False
       beam.moveTo(armorfelixforward.x,armorfelixforward.y)
       beam.rotateTowards(mouse)
       beam.visble = True
       beam.moveTowards(mouse,20)

    for index in range(len(level2)):
        level2[index].moveTowards(armorfelixforward,6)

    
    for index in range(len(level2)):
        if level2[index].collidedWith(armorfelixforward):
            felixforward.health-=5
        if level2[index].collidedWith(armorfelixright):
            felixforward.health-=5
        if level2[index].collidedWith(armorfelixdown):
            felixforward.health-=5
        if level2[index].collidedWith(armorfelixleft):
            felixforward.health-=5 
        if level2[index].collidedWith(armorfelixforwarda):
            felixforward.health-=5
            level2[index].visible = False
        if level2[index].collidedWith(armorfelixrighta):
            felixforward.health-=5
            level2[index].visible = False
        if level2[index].collidedWith(armorfelixdowna):
            felixforward.health-=5
            level2[index].visible = False
        if level2[index].collidedWith(armorfelixlefta):
            felixforward.health-=5
            level2[index].visible = False
        if level2[index].collidedWith(beam):
            level2[index].visible = False

    if atlasattack.collidedWith(armorfelixforward):
        felixforward.health-=10
        atlas.visible = False
        atlasattack.visible = True

    if atlasattack.collidedWith(armorfelixright):
        felixforward.health-=10
        atlas.visible = False
        atlasattack.visible = True

    if atlasattack.collidedWith(armorfelixdown):
        felixforward.health-=10
        atlas.visible = False
        atlasattack.visible = True

    if atlasattack.collidedWith(armorfelixleft):
        felixforward.health-=10
        atlas.visible = False
        atlasattack.visible = True

    if atlas.collidedWith(armorfelixforwarda):
        atlas.health-=5

    if atlas.collidedWith(armorfelixrighta):
        atlas.health-=5

    if atlas.collidedWith(armorfelixdowna):
        atlas.health-=5

    if atlas.collidedWith(armorfelixlefta):
        atlas.health-=5

    if atlasattack.collidedWith(armorfelixforwarda):
        atlas.health-=5

    if atlasattack.collidedWith(armorfelixrighta):
        atlas.health-=5

    if atlasattack.collidedWith(armorfelixdowna):
        atlas.health-=5

    if atlasattack.collidedWith(armorfelixlefta):
        atlas.health-=5

    if felixforward.health<=0:
        game.over = True

    if atlas.health>=0:
        atlas.visible = False
        skey.visible = True

    if armorfelixforward.collidedWith(skey):
        game.over = False

    if armorfelixright.collidedWith(skey):
        game.over = False

    if armorfelixleft.collidedWith(skey):
        game.over = False

    if armorfelixdown.collidedWith(skey):
        game.over = False

    game.drawText("Felix's Health :  " + str(felixforward.health),armorfelixforward.x - 75, armorfelixforward.y - 35,font)
    game.drawText("Atlas's Health: " + str(atlas.health),atlas.x,atlas.y-150,font)
    
    game.update(11)

game.over = False

while not game.over and felixforward.health < 0:
    gameover.draw()

    game.update(30)

game.quit()

#Level 3
while not game.over and felixforward.health > 0:
    game.processInput()
    bk3.draw()
    armorfelixforward.draw()
    #armorfelixright.visible = True
    armorfelixdown.draw()
    armorfelixleft.draw()
    armorfelixright.draw()
    armorfelixforwarda.draw()
    armorfelixdowna.draw()
    armorfelixlefta.draw()
    armorfelixrighta.draw()
    kronos.draw()
    kronosattack.draw()
    beam.draw()
    objective3.draw()

    if keys.Pressed[K_w]:
        armorfelixforward.visible = True
        armorfelixleft.visible = False
        armorfelixright.visible = False
        armorfelixdown.visible = False
        armorfelixforwarda.visible = False
        armorfelixdowna.visible = False
        armorfelixlefta.visible = False
        armorfelixrighta.visible = False
        armorfelixforward.y-=3
        armorfelixdown.y-=3
        armorfelixleft.y-=3
        armorfelixright.y-=3
        armorfelixforwarda.y-=3
        armorfelixdowna.y-=3
        armorfelixlefta.y-=3
        armorfelixrighta.y-=3


    if keys.Pressed[K_s]:
        armorfelixforward.visible = False
        armorfelixleft.visible = False
        armorfelixright.visible = False
        armorfelixdown.visible = True
        armorfelixforwarda.visible = False
        armorfelixdowna.visible = False
        armorfelixlefta.visible = False
        armorfelixrighta.visible = False
        armorfelixdown.y+=3
        armorfelixforward.y+=3
        armorfelixright.y+=3
        armorfelixleft.y+=3
        armorfelixdowna.y+=3
        armorfelixforwarda.y+=3
        armorfelixrighta.y+=3
        armorfelixlefta.y+=3
                                                                     
    if keys.Pressed[K_d]:
        armorfelixforward.visible = False
        armorfelixleft.visible = False
        armorfelixright.visible = True
        armorfelixdown.visible = False
        armorfelixforwarda.visible = False
        armorfelixdowna.visible = False
        armorfelixlefta.visible = False
        armorfelixrighta.visible = False
        armorfelixleft.x+=3
        armorfelixforward.x+=3
        armorfelixdown.x+=3
        armorfelixright.x+=3
        armorfelixlefta.x+=3
        armorfelixforwarda.x+=3
        armorfelixdowna.x+=3
        armorfelixrighta.x+=3

    if keys.Pressed[K_a]:
        armorfelixforward.visible = False
        armorfelixleft.visible = True
        armorfelixright.visible = False
        armorfelixdown.visible = False
        armorfelixforwarda.visible = False
        armorfelixdowna.visible = False
        armorfelixlefta.visible = False
        armorfelixrighta.visible = False
        armorfelixright.x-=3
        armorfelixforward.x-=3
        armorfelixdown.x-=3
        armorfelixleft.x-=3
        armorfelixrighta.x-=3
        armorfelixforwarda.x-=3
        armorfelixdowna.x-=3
        armorfelixlefta.x-=3

    if keys.Pressed[K_SPACE] and armorfelixforward.visible:
        armorfelixforwarda.visible = True
        armorfelixforward.visible = False
        beam.moveTo(armorfelixforward.x,armorfelixforward.y)
        beam.rotateTowards(mouse)
        beam.visble = True
        beam.moveTowards(mouse,20)

    if keys.Pressed[K_SPACE] and armorfelixleft.visible:
        armorfelixlefta.visible = True
        armorfelixleft.visible = False
        beam.moveTo(armorfelixforward.x,armorfelixforward.y)
        beam.rotateTowards(mouse)
        beam.visble = True
        beam.moveTowards(mouse,20)


    if keys.Pressed[K_SPACE] and armorfelixright.visible:
        armorfelixrighta.visible = True
        armorfelixright.visible = False
        beam.moveTo(armorfelixforward.x,armorfelixforward.y)
        beam.rotateTowards(mouse)
        beam.visble = True
        beam.moveTowards(mouse,20)


    if keys.Pressed[K_SPACE] and armorfelixdown.visible:
       armorfelixdowna.visible = True
       armorfelixdown.visible = False
       beam.moveTo(armorfelixforward.x,armorfelixforward.y)
       beam.rotateTowards(mouse)
       beam.visble = True
       beam.moveTowards(mouse,20)

    for index in range(len(level2)):
        level3[index].moveTowards(armorfelixforward,5)

    for index in range(len(level2)):
        if level3[index].collidedWith(armorfelixforward):
            felixforward.health-=5
        if level3[index].collidedWith(armorfelixright):
            felixforward.health-=5
        if level3[index].collidedWith(armorfelixdown):
            felixforward.health-=5
        if level3[index].collidedWith(armorfelixleft):
            felixforward.health-=5 
        if level3[index].collidedWith(armorfelixforwarda):
            felixforward.health-=5
            level3[index].visible = False
        if level3[index].collidedWith(armorfelixrighta):
            felixforward.health-=5
            level3[index].visible = False
        if level3[index].collidedWith(armorfelixdowna):
            felixforward.health-=5
            level3[index].visible = False
        if level3[index].collidedWith(armorfelixlefta):
            felixforward.health-=5
            level3[index].visible = False
        if level3[index].collidedWith(beam):
            level3[index].visible =5

    if kronosattack.collidedWith(armorfelixforward):
        felixforward.health-=10
        kronos.visible = False
        kronosattack.visible = True

    if kronosattack.collidedWith(armorfelixright):
        felixforward.health-=10
        kronos.visible = False
        atlasattack.visible = True

    if kronosattack.collidedWith(armorfelixdown):
        felixforward.health-=10
        kronos.visible = False
        kronosattack.visible = True

    if kronosattack.collidedWith(armorfelixleft):
        felixforward.health-=10
        kronos.visible = False
        kronosattack.visible = True

    if kronos.collidedWith(armorfelixforwarda):
        kronos.health-=5

    if kronos.collidedWith(armorfelixrighta):
        kronos.health-=5

    if kronos.collidedWith(armorfelixdowna):
        kronos.health-=5

    if kronos.collidedWith(armorfelixlefta):
        kronos.health-=5

    if kronosattack.collidedWith(armorfelixforwarda):
        kronos.health-=5

    if kronosattack.collidedWith(armorfelixrighta):
        kronos.health-=5

    if kronosattack.collidedWith(armorfelixdowna):
        kronos.health-=5

    if kronosattack.collidedWith(armorfelixlefta):
        kronos.health-=5

    if felixforward.health<=0:
        game.over = True

    if kronos.health>=0:
        kronos.visible = False
        ckey.visible = True

    if armorfelixforward.collidedWith(ckey):
        game.over = False

    if armorfelixright.collidedWith(ckey):
        game.over = False

    if armorfelixleft.collidedWith(ckey):
        game.over = False

    if armorfelixdown.collidedWith(ckey):
        game.over = False

    game.drawText("Felix's Health :  " + str(felixforward.health),armorfelixforward.x - 75, armorfelixforward.y - 35,font)
    game.drawText("Kronos's Health: " + str(kronos.health),kronos.x,kronos.y-150,font)

    game.update(11)

while not game.over and felixforward.health <0:
    gameover.draw()

    game.update(30)

game.quit()

#Level 4
while not game.over and felixforward.health > 0:
    game.processInput()
    bk4.draw()
    felixforward.health = 100
    armorfelixforward.draw()
    armorfelixdown.draw()
    armorfelixleft.draw()
    armorfelixright.draw()
    armorfelixforwarda.draw()
    armorfelixdowna.draw()
    armorfelixlefta.draw()
    armorfelixrighta.draw()
    beam.draw()
    jax.health = 200
    jax.draw()
    jaxattack.draw()
    objective4.draw()

    if keys.Pressed[K_w]:
        armorfelixforward.visible = True
        armorfelixleft.visible = False
        armorfelixright.visible = False
        armorfelixdown.visible = False
        armorfelixforwarda.visible = False
        armorfelixdowna.visible = False
        armorfelixlefta.visible = False
        armorfelixrighta.visible = False
        armorfelixforward.y-=3
        armorfelixdown.y-=3
        armorfelixleft.y-=3
        armorfelixright.y-=3
        armorfelixforwarda.y-=3
        armorfelixdowna.y-=3
        armorfelixlefta.y-=3
        armorfelixrighta.y-=3


    if keys.Pressed[K_s]:
        armorfelixforward.visible = False
        armorfelixleft.visible = False
        armorfelixright.visible = False
        armorfelixdown.visible = True
        armorfelixforwarda.visible = False
        armorfelixdowna.visible = False
        armorfelixlefta.visible = False
        armorfelixrighta.visible = False
        armorfelixdown.y+=3
        armorfelixforward.y+=3
        armorfelixright.y+=3
        armorfelixleft.y+=3
        armorfelixdowna.y+=3
        armorfelixforwarda.y+=3
        armorfelixrighta.y+=3
        armorfelixlefta.y+=3
                                                                     
    if keys.Pressed[K_d]:
        armorfelixforward.visible = False
        armorfelixleft.visible = False
        armorfelixright.visible = True
        armorfelixdown.visible = False
        armorfelixforwarda.visible = False
        armorfelixdowna.visible = False
        armorfelixlefta.visible = False
        armorfelixrighta.visible = False
        armorfelixleft.x+=3
        armorfelixforward.x+=3
        armorfelixdown.x+=3
        armorfelixright.x+=3
        armorfelixlefta.x+=3
        armorfelixforwarda.x+=3
        armorfelixdowna.x+=3
        armorfelixrighta.x+=3

    if keys.Pressed[K_a]:
        armorfelixforward.visible = False
        armorfelixleft.visible = True
        armorfelixright.visible = False
        armorfelixdown.visible = False
        armorfelixforwarda.visible = False
        armorfelixdowna.visible = False
        armorfelixlefta.visible = False
        armorfelixrighta.visible = False
        armorfelixright.x-=3
        armorfelixforward.x-=3
        armorfelixdown.x-=3
        armorfelixleft.x-=3
        armorfelixrighta.x-=3
        armorfelixforwarda.x-=3
        armorfelixdowna.x-=3
        armorfelixlefta.x-=3

    if keys.Pressed[K_SPACE] and armorfelixforward.visible:
        armorfelixforwarda.visible = True
        armorfelixforward.visible = False
        beam.moveTo(armorfelixforward.x,armorfelixforward.y)
        beam.rotateTowards(mouse)
        beam.visble = True
        beam.moveTowards(mouse,20)

    if keys.Pressed[K_SPACE] and armorfelixleft.visible:
        armorfelixlefta.visible = True
        armorfelixleft.visible = False
        beam.moveTo(armorfelixforward.x,armorfelixforward.y)
        beam.rotateTowards(mouse)
        beam.visble = True
        beam.moveTowards(mouse,20)


    if keys.Pressed[K_SPACE] and armorfelixright.visible:
        armorfelixrighta.visible = True
        armorfelixright.visible = False
        beam.moveTo(armorfelixforward.x,armorfelixforward.y)
        beam.rotateTowards(mouse)
        beam.visble = True
        beam.moveTowards(mouse,20)


    if keys.Pressed[K_SPACE] and armorfelixdown.visible:
       armorfelixdowna.visible = True
       armorfelixdown.visible = False
       beam.moveTo(armorfelixforward.x,armorfelixforward.y)
       beam.rotateTowards(mouse)
       beam.visble = True
       beam.moveTowards(mouse,20)

    if jaxattack.collidedWith(armorfelixforward):
        felixforward.health-=15
        jax.visible = False
        jaxattack.visible = True

    if jaxattack.collidedWith(armorfelixright):
        felixforward.health-=15
        jax.visible = False
        jaxattack.visible = True

    if jaxattack.collidedWith(armorfelixdown):
        felixforward.health-=15
        jax.visible = False
        jaxattack.visible = True

    if jaxattack.collidedWith(armorfelixleft):
        felixforward.health-=15
        jax.visible = False
        jaxattack.visible = True

    if jax.collidedWith(armorfelixforwarda):
        jax.health-=5

    if jax.collidedWith(armorfelixrighta):
        jax.health-=5

    if jax.collidedWith(armorfelixdowna):
        jax.health-=5

    if jax.collidedWith(armorfelixlefta):
        jax.health-=5

    if kronosattack.collidedWith(armorfelixforwarda):
        jax.health-=5

    if kronosattack.collidedWith(armorfelixrighta):
        jax.health-=5

    if kronosattack.collidedWith(armorfelixdowna):
        jax.health-=5

    if kronosattack.collidedWith(armorfelixlefta):
        jax.health-=5

    if felixforward.health<=0:
        game.over = True

    if jax.health<=0:
        game.over = True

    game.drawText("Felix's Health :  " + str(felixforward.health),armorfelixforward.x - 75, armorfelixforward.y - 35,font)
    game.drawText("Jax's Health: " + str(jax.health),kronos.x,jax.y-150,font)

    game.update(11)

game.over = False

while not game.over and felixforward.health<=0:
    gameover.draw()

    game.update(30)

game.quit()

while not game.over and felixforward.health > 0 and jax.health<=0:
    startbk.draw()
    congrats.draw()

    game.update(30)

game.quit()
    


    
