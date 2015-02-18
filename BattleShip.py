from Tkinter import *

def mousePressed(event):
    #Buttons for the main menu.
    if canvas.data.menuState == True:
        if (event.x <= 325) and (event.x >= 175):
            if (event.y <= 170) and (event.y >= 125):
                canvas.data.menuState = not canvas.data.menuState
                canvas.data.instrucState = not canvas.data.instrucState
                canvas.data.fillOne = "white"
                canvas.data.fillTwo = "white"
                canvas.data.fillThree = "white"
        if (event.x <= 325) and (event.x >= 175):
            if (event.y <= 245) and (event.y >= 200):
                canvas.data.menuState = not canvas.data.menuState
                canvas.data.gameState = not canvas.data.gameState
                canvas.data.fillOne = "white"
                canvas.data.fillTwo = "white"
                canvas.data.fillThree = "white"

    #Buttons for the instructions page.            
    if canvas.data.instrucState == True:
        if (event.x <= 240) and (event.x >= 80):
            if (event.y <= 430) and (event.y >= 390):
                canvas.data.instrucState = not canvas.data.instrucState
                canvas.data.menuState = not canvas.data.menuState
                canvas.data.fillOne = "white"
                canvas.data.fillTwo = "white"
                canvas.data.fillThree = "white"
        if (event.x <= 420) and (event.x >= 260):
            if (event.y <= 430) and (event.y >= 390):
                canvas.data.instrucState = not canvas.data.instrucState
                canvas.data.gameState = not canvas.data.gameState
                canvas.data.fillOne = "white"
                canvas.data.fillTwo = "white"
                canvas.data.fillThree = "white"

    if canvas.data.gameState == True:
        #Exit button
        if (event.x <= 495) and (event.x >= 450):
            if (event.y <= 30) and (event.y >= 10):
                canvas.data.gameState = not canvas.data.gameState
                canvas.data.menuState = not canvas.data.menuState
                restartGame()
                canvas.data.fillOne = "white"
                canvas.data.fillTwo = "white"
                canvas.data.fillThree = "white"
    
        #Player 1 Done button
        if canvas.data.turn == 0 or canvas.data.turn == 3:
            if (event.x <= 383) and (event.x >= 325):
                if (event.y <= 460) and (event.y >= 440):
                    canvas.data.clickCounter = 0
                    if canvas.data.turn == 0:
                        canvas.data.turn = 2
                    else: canvas.data.turn = 1
                    canvas.data.fillOne = "white"
                    canvas.data.fillTwo = "white"
                    canvas.data.fillThree = "white"

        #Player 1 Start button
        if canvas.data.turn == 5:
            if (event.x <= 383) and (event.x >= 325):
                if (event.y <= 460) and (event.y >= 440):
                    canvas.data.turn = 3
                    canvas.data.fillOne = "white"
                    canvas.data.fillTwo = "white"
                    canvas.data.fillThree = "white"        
                    
        #Player 2 Start button
        if canvas.data.turn == 1:
            if (event.x <= 383) and (event.x >= 325):
                if (event.y <= 160) and (event.y >= 140):
                    canvas.data.turn = 4
                    canvas.data.fillOne = "white"
                    canvas.data.fillTwo = "white"
                    canvas.data.fillThree = "white"
            return
                    
        #Player 2 Done Button
        if canvas.data.turn == 2 or canvas.data.turn == 4:
            if (event.x <= 383) and (event.x >= 325):
                if (event.y <= 160) and (event.y >= 140):
                    canvas.data.turn = 5
                    canvas.data.clickCounter = 0
                    canvas.data.fillOne = "white"
                    canvas.data.fillTwo = "white"
                    canvas.data.fillThree = "white"

        if canvas.data.clickCounter < 100:                    
            if canvas.data.turn == 3:
                if ((event.x <= 285) and (event.x >= 35) and (event.y <= 285) and (event.y >=35)):
                    canvas.data.clickCounter += 1
                    offset0 = (canvas.data.margin + 10 * canvas.data.colWidth + 25)
                    offset1 = (canvas.data.margin + 10 * canvas.data.rowHeight + 25)
                    if (canvas.data.enemyGrid[(event.y-offset1)/25][(event.x-offset0)/25] > 0):
                        canvas.data.playerHit += 1
                        canvas.data.enemyGrid1[(event.y-offset1)/25][(event.x-offset0)/25] += 1
                    else:
                        canvas.data.playerMiss += 1
                        canvas.data.enemyGrid1[(event.y-offset1)/25][(event.x-offset0)/25] -= 1

            if canvas.data.turn == 4:
                if ((event.x <= 285) and (event.x >= 35) and (event.y <= 595) and (event.y >=345)):
                    canvas.data.clickCounter += 1
                    offset0 = (canvas.data.margin + 10 * canvas.data.colWidth + 25)
                    offset1 = (canvas.data.margin + 10 * canvas.data.rowHeight + 25) + 310
                    if (canvas.data.playerGrid[(event.y-offset1)/25][(event.x-offset0)/25] > 0):
                        canvas.data.enemyHit += 1
                        canvas.data.playerGrid1[(event.y-offset1)/25][(event.x-offset0)/25] += 1
                    else:
                        canvas.data.enemyMiss += 1
                        canvas.data.playerGrid1[(event.y-offset1)/25][(event.x-offset0)/25] -= 1
        else: print "You have already made your turn!"
                

    redrawAll()

def mouseMotion(event):
    if canvas.data.menuState == True:
        if (event.x < 325) and (event.x > 175):
            if (event.y < 170) and (event.y > 125):
                canvas.data.fillOne = canvas.data.buttonFill
            else: canvas.data.fillOne = "white"
        else: canvas.data.fillOne = "white"
        if (event.x < 325) and (event.x > 175):
            if (event.y < 245) and (event.y > 200):
                canvas.data.fillTwo = canvas.data.buttonFill
            else: canvas.data.fillTwo = "white"
        else: canvas.data.fillTwo = "white"

    if canvas.data.instrucState == True:
        if (event.x < 240) and (event.x > 80):
            if (event.y < 430) and (event.y > 390):
                canvas.data.fillOne = canvas.data.buttonFill
            else: canvas.data.fillOne = "white"
        else: canvas.data.fillOne = "white"
        if (event.x < 420) and (event.x > 260):
            if (event.y < 430) and (event.y > 390):
                canvas.data.fillTwo = canvas.data.buttonFill
            else: canvas.data.fillTwo = "white"
        else: canvas.data.fillTwo = "white"

    if canvas.data.gameState == True:
        if (event.x < 495) and (event.x > 450):
            if (event.y < 30) and (event.y > 10):
                canvas.data.fillOne = canvas.data.buttonFill
            else: canvas.data.fillOne = "white"
        else: canvas.data.fillOne = "white"
        if (event.x < 383) and (event.x > 325):
            if (event.y < 160) and (event.y > 140):
                canvas.data.fillTwo = canvas.data.buttonFill
            else: canvas.data.fillTwo = "white"
        else: canvas.data.fillTwo = "white"
        if (event.x < 383) and (event.x > 325):
            if (event.y < 460) and (event.y > 440):
                canvas.data.fillThree = canvas.data.buttonFill
            else: canvas.data.fillThree = "white"
        else: canvas.data.fillThree = "white"
    
    redrawAll()

def leftMousePressed(event):
    if canvas.data.turn == 0:
        if (canvas.data.currentShip1 == 1):
            canvas.data.carrierPosition1 = (event.x, event.y)
        elif (canvas.data.currentShip1 == 2):
            canvas.data.destroyerPosition1 = (event.x, event.y)
        elif (canvas.data.currentShip1 == 3):
            canvas.data.submarinePosition1 = (event.x, event.y)
        elif (canvas.data.currentShip1 == 4):
            canvas.data.patrolPosition1 = (event.x, event.y)
    if canvas.data.turn == 2:
        if (canvas.data.currentShip2 == 1):
            canvas.data.carrierPosition2 = (event.x, event.y)
        elif (canvas.data.currentShip2 == 2):
            canvas.data.destroyerPosition2 = (event.x, event.y)
        elif (canvas.data.currentShip2 == 3):
            canvas.data.submarinePosition2 = (event.x, event.y)
        elif (canvas.data.currentShip2 == 4):
            canvas.data.patrolPosition2 = (event.x, event.y)
    redrawAll()

def leftMouseMoved(event):
    if canvas.data.turn == 0:
        if (canvas.data.currentShip1 == 1):
            canvas.data.carrierPosition1 = (event.x, event.y)
        elif (canvas.data.currentShip1 == 2):
            canvas.data.destroyerPosition1 = (event.x, event.y)
        elif (canvas.data.currentShip1 == 3):
            canvas.data.submarinePosition1 = (event.x, event.y)
        elif (canvas.data.currentShip1 == 4):
            canvas.data.patrolPosition1 = (event.x, event.y)
    if canvas.data.turn == 2:
        if (canvas.data.currentShip2 == 1):
            canvas.data.carrierPosition2 = (event.x, event.y)
        elif (canvas.data.currentShip2 == 2):
            canvas.data.destroyerPosition2 = (event.x, event.y)
        elif (canvas.data.currentShip2 == 3):
            canvas.data.submarinePosition2 = (event.x, event.y)
        elif (canvas.data.currentShip2 == 4):
            canvas.data.patrolPosition2 = (event.x, event.y)
    redrawAll()

def leftMouseReleased(event):
    x = event.x
    y = event.y
    if canvas.data.gameState == True:
        for row in range(canvas.data.rows):
            for col in range(canvas.data.cols + 1):
                #Player 1 Ship placement
                if canvas.data.turn == 0:
                
                    x0 = canvas.data.margin + (col+1) * canvas.data.colWidth + 25
                    x1 = x0 + canvas.data.colWidth
                    y0 = canvas.data.margin + (row) * canvas.data.rowHeight + 25 + 310
                    y1 = y0 + canvas.data.rowHeight
                    offset0 = (canvas.data.margin + 10 * canvas.data.colWidth + 25)
                    offset1 = (canvas.data.margin + 10 * canvas.data.rowHeight + 25) + 310
                    
                    if canvas.data.currentShip1 == 1:
                        if canvas.data.rotatedOne1 == False:
                            if ((x < 40) or (x > 285)) or ((y > 550) or (y < 385)):
                                canvas.data.carrierPosition1 = (350,555)
                            elif ((x0 - (x)) < 25) and ((y0 - (y)) < 10):
                                canvas.data.carrierPosition1 = (x0 - 12.5, y0)
                                canvas.data.playerGrid[(((y-45)-offset1)/25)][(x-offset0)/25] += 1
                                canvas.data.playerGrid[(((y-45)-offset1)/25)+1][(x-offset0)/25] += 1
                                canvas.data.playerGrid[(((y-45)-offset1)/25)+2][(x-offset0)/25] += 1
                                canvas.data.playerGrid[(((y-45)-offset1)/25)+3][(x-offset0)/25] += 1
                        else:
                            if ((x < 75) or (x > 245)) or ((y > 595) or (y < 350)):
                                canvas.data.carrierPosition1 = (400,600)
                            elif ((x0 - (x)) < 10) and ((y0 - (y)) < 5):
                                canvas.data.carrierPosition1 = (x0, y0+12.5)
                                canvas.data.playerGrid[((y-offset1)/25)][((x-45)-offset0)/25] += 1
                                canvas.data.playerGrid[((y-offset1)/25)][(((x-45)-offset0)/25)+1] += 1
                                canvas.data.playerGrid[((y-offset1)/25)][(((x-45)-offset0)/25)+2] += 1
                                canvas.data.playerGrid[((y-offset1)/25)][(((x-45)-offset0)/25)+3] += 1
                        
                    if canvas.data.currentShip1 == 2:
                        if canvas.data.rotatedTwo1 == False:
                            if ((x < 40) or (x > 285)) or ((y > 575) or (y < 375)):
                                canvas.data.destroyerPosition1 = (385,555)
                            elif ((x0 - (x)) < 25) and ((y0 - (y)) < 25):
                                canvas.data.destroyerPosition1 = (x0 - 12.5, y0-15)
                                canvas.data.playerGrid[(((y-37)-offset1)/25)][(x-offset0)/25] += 1
                                canvas.data.playerGrid[(((y-37)-offset1)/25)+1][(x-offset0)/25] += 1
                                canvas.data.playerGrid[(((y-37)-offset1)/25)+2][(x-offset0)/25] += 1
                        else:
                            if ((x < 60) or (x > 260)) or ((y > 595) or (y < 350)):
                                canvas.data.destroyerPosition1 = (350,555)
                            elif ((x0 - (x)) < 25) and ((y0 - (y)) < 5):
                                canvas.data.destroyerPosition1 = (x0-15, y0+12.5)
                                canvas.data.playerGrid[(((y)-offset1)/25)][((x-37)-offset0)/25] += 1
                                canvas.data.playerGrid[(((y)-offset1)/25)][(((x-37)-offset0)/25)+1] += 1
                                canvas.data.playerGrid[(((y)-offset1)/25)][(((x-37)-offset0)/25)+2] += 1

                    if canvas.data.currentShip1 == 3:
                        if canvas.data.rotatedThree1 == False:
                            if ((x < 40) or (x > 285)) or ((y > 600) or (y < 360)):
                                canvas.data.submarinePosition1 = (420,555)
                            elif ((x0 - (x)) < 25) and ((y0 - (y)) < 15):
                                canvas.data.submarinePosition1 = (x0-12.5, y0)
                                canvas.data.playerGrid[(((y-20)-offset1)/25)][(x-offset0)/25] += 1
                                canvas.data.playerGrid[(((y-20)-offset1)/25)+1][(x-offset0)/25] += 1
                        else:
                            if ((x < 45) or (x > 270)) or ((y > 595) or (y < 350)):
                                canvas.data.submarinePosition1 = (420,555)
                            elif ((x0 - (x)) < 15) and ((y0 - (y)) < 5):
                                canvas.data.submarinePosition1 = (x0, y0+12.5)
                                canvas.data.playerGrid[((y-offset1)/25)][((x-20)-offset0)/25] += 1
                                canvas.data.playerGrid[((y-offset1)/25)][(((x-20)-offset0)/25)+1] += 1

                    if canvas.data.currentShip1 == 4:
                        if canvas.data.rotatedFour1 == False:
                            if ((x < 40) or (x > 285)) or ((y > 600) or (y < 360)):
                                canvas.data.patrolPosition1 = (450,555)
                            elif ((x0 - (x)) < 25) and ((y0 - (y)) < 15):
                                canvas.data.patrolPosition1 = (x0-12.5, y0)
                                canvas.data.playerGrid[(((y-20)-offset1)/25)][(x-offset0)/25] += 1
                                canvas.data.playerGrid[(((y-20)-offset1)/25)+1][(x-offset0)/25] += 1
                        else:
                            if ((x < 45) or (x > 270)) or ((y > 595) or (y < 350)):
                                canvas.data.patrolPosition1 = (435,555)
                            elif ((x0 - (x)) < 15) and ((y0 - (y)) < 5):
                                canvas.data.patrolPosition1 = (x0, y0+12.5)
                                canvas.data.playerGrid[((y-offset1)/25)][((x-20)-offset0)/25] += 1
                                canvas.data.playerGrid[((y-offset1)/25)][(((x-20)-offset0)/25) + 1] += 1


                #Player 2 Ship placement
                if canvas.data.turn == 2:
                
                    x0 = canvas.data.margin + (col+1) * canvas.data.colWidth + 25
                    x1 = x0 + canvas.data.colWidth
                    y0 = canvas.data.margin + (row) * canvas.data.rowHeight + 25
                    y1 = y0 + canvas.data.rowHeight
                    offset0 = (canvas.data.margin + 10 * canvas.data.colWidth + 25)
                    offset1 = (canvas.data.margin + 10 * canvas.data.rowHeight + 25)
                    
                    if canvas.data.currentShip2 == 1:
                        if canvas.data.rotatedOne2 == False:
                            if ((x < 40) or (x > 285)) or ((y > 240) or (y < 75)):
                                canvas.data.carrierPosition2 = (350,245)
                            elif ((x0 - (x)) < 25) and ((y0 - (y)) < 10):
                                canvas.data.carrierPosition2 = (x0 - 12.5, y0)
                                canvas.data.enemyGrid[(((y-45)-offset1)/25)][(x-offset0)/25] += 1
                                canvas.data.enemyGrid[(((y-45)-offset1)/25) + 1][(x-offset0)/25] += 1
                                canvas.data.enemyGrid[(((y-45)-offset1)/25) + 2][(x-offset0)/25] += 1
                                canvas.data.enemyGrid[(((y-45)-offset1)/25) + 3][(x-offset0)/25] += 1
                        else:
                            if ((x < 75) or (x > 245)) or ((y > 285) or (y < 40)):
                                canvas.data.carrierPosition2 = (400,290)
                            elif ((x0 - (x)) < 10) and ((y0 - (y)) < 5):
                                canvas.data.carrierPosition2 = (x0, y0+12.5)
                                canvas.data.enemyGrid[((y-offset1)/25)][((x-45)-offset0)/25] += 1
                                canvas.data.enemyGrid[((y-offset1)/25)][(((x-45)-offset0)/25)+1] += 1
                                canvas.data.enemyGrid[((y-offset1)/25)][(((x-45)-offset0)/25)+2] += 1
                                canvas.data.enemyGrid[((y-offset1)/25)][(((x-45)-offset0)/25)+3] += 1

                                
                    if canvas.data.currentShip2 == 2:
                        if canvas.data.rotatedTwo2 == False:
                            if ((x < 40) or (x > 285)) or ((y > 265) or (y < 65)):
                                canvas.data.destroyerPosition2 = (385,245)
                            elif ((x0 - (x)) < 25) and ((y0 - (y)) < 25):
                                canvas.data.destroyerPosition2 = (x0 - 12.5, y0-15)
                                canvas.data.enemyGrid[(((y-37)-offset1)/25)][(x-offset0)/25] += 1
                                canvas.data.enemyGrid[(((y-37)-offset1)/25)+1][(x-offset0)/25] += 1
                                canvas.data.enemyGrid[(((y-37)-offset1)/25)+2][(x-offset0)/25] += 1

                        else:
                            if ((x < 60) or (x > 260)) or ((y > 285) or (y < 40)):
                                canvas.data.destroyerPosition2 = (350,245)
                            elif ((x0 - (x)) < 25) and ((y0 - (y)) < 5):
                                canvas.data.destroyerPosition2 = (x0-15, y0+12.5)
                                canvas.data.enemyGrid[(((y)-offset1)/25)][((x-37)-offset0)/25+1] += 1
                                canvas.data.enemyGrid[(((y)-offset1)/25)][(((x-37)-offset0)/25)] += 1
                                canvas.data.enemyGrid[(((y)-offset1)/25)][(((x-37)-offset0)/25)+2] += 1

                    if canvas.data.currentShip2 == 3:
                        if canvas.data.rotatedThree2 == False:
                            if ((x < 40) or (x > 285)) or ((y > 290) or (y < 40)):
                                canvas.data.submarinePosition2 = (420,245)
                            elif ((x0 - (x)) < 25) and ((y0 - (y)) < 15):
                                canvas.data.submarinePosition2 = (x0-12.5, y0)
                                canvas.data.enemyGrid[(((y-20)-offset1)/25)][(x-offset0)/25] += 1
                                canvas.data.enemyGrid[(((y-20)-offset1)/25)+1][(x-offset0)/25] += 1
                        else:
                            if ((x < 45) or (x > 270)) or ((y > 285) or (y < 40)):
                                canvas.data.submarinePosition2 = (420,245)
                            elif ((x0 - (x)) < 15) and ((y0 - (y)) < 5):
                                canvas.data.submarinePosition2 = (x0, y0+12.5)
                                canvas.data.enemyGrid[((y-offset1)/25)][((x-20)-offset0)/25] += 1
                                canvas.data.enemyGrid[((y-offset1)/25)][(((x-20)-offset0)/25)+1] += 1

                    if canvas.data.currentShip2 == 4:
                        if canvas.data.rotatedFour2 == False:
                            if ((x < 40) or (x > 285)) or ((y > 290) or (y < 50)):
                                canvas.data.patrolPosition2 = (450,245)
                            elif ((x0 - (x)) < 25) and ((y0 - (y)) < 15):
                                canvas.data.patrolPosition2 = (x0-12.5, y0)
                                canvas.data.enemyGrid[(((y-20)-offset1)/25)][(x-offset0)/25] += 1
                                canvas.data.enemyGrid[(((y-20)-offset1)/25)+1][(x-offset0)/25] += 1
                        else:
                            if ((x < 45) or (x > 270)) or ((y > 285) or (y < 40)):
                                canvas.data.patrolPosition2 = (435,245)
                            elif ((x0 - (x)) < 15) and ((y0 - (y)) < 5):
                                canvas.data.patrolPosition2 = (x0, y0+12.5)
                                canvas.data.enemyGrid[((y-offset1)/25)][((x-20)-offset0)/25] += 1
                                canvas.data.enemyGrid[((y-offset1)/25)][(((x-20)-offset0)/25)+1] += 1

    redrawAll()



def keyPressed(event):
    if event.char == "p":
        resetShips()
    if (event.char == "r"):
        rotateShip()
    if canvas.data.turn == 0:
        if (event.char == "1"):
            canvas.data.currentShip1 = 1
        if (event.char == "2"):
            canvas.data.currentShip1 = 2
        if (event.char == "3"):
            canvas.data.currentShip1 = 3
        if (event.char == "4"):
            canvas.data.currentShip1 = 4
        if (event.char == "0"):
            canvas.data.currentShip1 = 0
    if canvas.data.turn == 2:
        if (event.char == "1"):
            canvas.data.currentShip2 = 1
        if (event.char == "2"):
            canvas.data.currentShip2 = 2
        if (event.char == "3"):
            canvas.data.currentShip2 = 3
        if (event.char == "4"):
            canvas.data.currentShip2 = 4
        if (event.char == "0"):
            canvas.data.currentShip2 = 0
    redrawAll()

def resetShips():
    if canvas.data.turn == 0:
        canvas.data.playerGrid = [[0,0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0,0]]
        if canvas.data.rotatedOne1 == False:
            canvas.data.carrierPosition1 = (350,555)
        else: canvas.data.carrierPosition1 = (400,600)
        
        canvas.data.destroyerPosition1 = (385,555)
        canvas.data.submarinePosition1 = (420,555)
        canvas.data.patrolPosition1 = (450,555)
    if canvas.data.turn == 2:
        canvas.data.enemyGrid = [[0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0]]
        if canvas.data.rotatedOne2 == False:
            canvas.data.carrierPosition2 = (350,253)
        else: canvas.data.carrierPosition2 = (400,290)
        canvas.data.destroyerPosition2 = (385,253)
        canvas.data.submarinePosition2 = (420,253)
        canvas.data.patrolPosition2 = (450,253)
    redrawAll()

def restartGame():
    init()

def rotateShip():
    #####################################
    #Rotation function part for Player 1#
    #####################################
    if canvas.data.turn == 0:
        if canvas.data.currentShip1 == 1:
            canvas.data.rotatedOne1 = not canvas.data.rotatedOne1
            if canvas.data.rotatedOne1 == True:
                aircraftCarrier1 = PhotoImage(file="aircraftcarrier2.gif")
                canvas.data.aircraftCarrier1 = aircraftCarrier1
            else:
                aircraftCarrier1 = PhotoImage(file="aircraftcarrier.gif")
                canvas.data.aircraftCarrier1 = aircraftCarrier1
        if canvas.data.currentShip1 == 2:
            canvas.data.rotatedTwo1 = not canvas.data.rotatedTwo1
            if canvas.data.rotatedTwo1 == True:
                destroyer1 = PhotoImage(file="destroyer2.gif")
                canvas.data.destroyer1 = destroyer1
            else:
                destroyer1 = PhotoImage(file="destroyer.gif")
                canvas.data.destroyer1 = destroyer1
        if canvas.data.currentShip1 == 3:
            canvas.data.rotatedThree1 = not canvas.data.rotatedThree1
            if canvas.data.rotatedThree1 == True:
                submarine1 = PhotoImage(file="submarine2.gif")
                canvas.data.submarine1 = submarine1
            else:
                submarine1 = PhotoImage(file="submarine.gif")
                canvas.data.submarine1 = submarine1
        if canvas.data.currentShip1 == 4:
            canvas.data.rotatedFour1 = not canvas.data.rotatedFour1
            if canvas.data.rotatedFour1 == True:
                patrolboat1 = PhotoImage(file="patrolboat2.gif")
                canvas.data.patrolboat1 = patrolboat1
            else:
                patrolboat1 = PhotoImage(file="patrolboat.gif")
                canvas.data.patrolboat1 = patrolboat1
            
    #####################################
    #Rotation function part for Player 2#
    #####################################
    if canvas.data.turn == 2:
        if canvas.data.currentShip2 == 1:
            canvas.data.rotatedOne2 = not canvas.data.rotatedOne2
            if canvas.data.rotatedOne2 == True:
                aircraftCarrier2 = PhotoImage(file="aircraftcarrier2.gif")
                canvas.data.aircraftCarrier2 = aircraftCarrier2
            else:
                aircraftCarrier2 = PhotoImage(file="aircraftcarrier.gif")
                canvas.data.aircraftCarrier2 = aircraftCarrier2
        if canvas.data.currentShip2 == 2:
            canvas.data.rotatedTwo2 = not canvas.data.rotatedTwo2
            if canvas.data.rotatedTwo2 == True:
                destroyer2 = PhotoImage(file="destroyer2.gif")
                canvas.data.destroyer2 = destroyer2
            else:
                destroyer2 = PhotoImage(file="destroyer.gif")
                canvas.data.destroyer2 = destroyer2
        if canvas.data.currentShip2 == 3:
            canvas.data.rotatedThree2 = not canvas.data.rotatedThree2
            if canvas.data.rotatedThree2 == True:
                submarine2 = PhotoImage(file="submarine2.gif")
                canvas.data.submarine2 = submarine2
            else:
                submarine2 = PhotoImage(file="submarine.gif")
                canvas.data.submarine2 = submarine2
        if canvas.data.currentShip2 == 4:
            canvas.data.rotatedFour2 = not canvas.data.rotatedFour2
            if canvas.data.rotatedFour2 == True:
                patrolboat2 = PhotoImage(file="patrolboat2.gif")
                canvas.data.patrolboat2 = patrolboat2
            else:
                patrolboat2 = PhotoImage(file="patrolboat.gif")
                canvas.data.patrolboat2 = patrolboat2

def timerFired():
    if canvas.data.playerHit > 10:
        canvas.data.turn = 6
    if canvas.data.enemyHit > 10:
        canvas.data.turn = 7
    redrawAll()
    delay = 250 # milliseconds
    canvas.after(delay, timerFired) # pause, then call timerFired again

#I took this drawGrid function from my code from my bitmap editor for a previous HW
def drawGrid(row,col):
    x0 = canvas.data.margin + col * canvas.data.colWidth + 25
    x1 = x0 + canvas.data.colWidth
    y0 = canvas.data.margin + row * canvas.data.rowHeight + 25
    y1 = y0 + canvas.data.rowHeight
    canvas.create_rectangle(x0,y0,x1,y1,fill="RoyalBlue1")
    canvas.create_rectangle(x0,y0+310,x1,y1+310,fill="RoyalBlue1")

def drawPegs(row,col):
    x0 = canvas.data.margin + col * canvas.data.colWidth + 25
    x1 = x0 + canvas.data.colWidth
    y0 = canvas.data.margin + row * canvas.data.rowHeight + 25
    y1 = y0 + canvas.data.rowHeight
    if (canvas.data.enemyGrid1[row][col] > 0):
        canvas.create_oval(x0+5,y0+5,x1-5,y1-5,fill="red", width=2)
    elif (canvas.data.enemyGrid1[row][col] < 0 ):
        canvas.create_oval(x0+5,y0+5,x1-5,y1-5,fill="white", width=2)

    if (canvas.data.playerGrid1[row][col] > 0 ):
        canvas.create_oval(x0+5,y0+315,x1-5,y1+305,fill="red", width=2)
    elif (canvas.data.playerGrid1[row][col] < 0 ):
        canvas.create_oval(x0+5,y0+315,x1-5,y1+305,fill="white", width=2)


def redrawAll():
    canvas.delete(ALL)
    #Creates the menu for the game.
    if canvas.data.menuState == True:
        logo = PhotoImage(file="logo.gif")
        canvas.data.logo = logo
        canvas.create_image(250,315,image=logo)
        canvas.create_text(250,65,text="BATTLESHIP",font="Courier 42 bold",fill="white")
        canvas.create_text(350,570,text="Created by: Omar Jatoi",font="courier 20",fill="white")
        fillOne = canvas.data.fillOne
        fillTwo = canvas.data.fillTwo
        canvas.create_rectangle(175,125,325,170)
        canvas.create_text(250,150,text="INSTRUCTIONS",font="courier 18",fill=fillOne)
        canvas.create_rectangle(175,200,325,245)
        canvas.create_text(250,225,text="PLAY GAME",font="courier 18",fill=fillTwo)

    #Creates the instructions page.
    if canvas.data.instrucState == True:
        logo = PhotoImage(file="logo.gif")
        canvas.data.logo = logo
        canvas.create_image(250,315,image=logo)
        listOne = "1. Select ship by pressing\n   1, 2, 3, or 4.\n   Click and drag to place. \n   Press "r" to rotate ship."      
        listTwo = "2. Click DONE and wait for \n   other player to place ships."
        listThree = "3. Once ships have been placed \n   press DONE. Player 1 will now \n   press START to begin turn."
        listFour = "4. Click on the enemy grid\n   to guess enemy ship\n   locations. First player\n   to sink all ships wins!"
        canvas.create_text(250,50,text="INSTRUCTIONS",font="courier 36 bold",fill="white")
        canvas.create_text(50,160,text=listOne,font="courier 16",anchor=SW,fill="white")
        canvas.create_text(50,210,text=listTwo,font="courier 16",anchor=SW,fill="white")
        canvas.create_text(50,275,text=listThree,font="courier 16",anchor=SW,fill="white")
        canvas.create_text(50,355,text=listFour,font="courier 16",anchor=SW,fill="white")
        fillOne = canvas.data.fillOne
        fillTwo = canvas.data.fillTwo
        canvas.create_rectangle(80,390,240,430)
        canvas.create_rectangle(260,390,420,430)
        canvas.create_text(160,410,text="MAIN MENU",font="courier 18",fill=fillOne)
        canvas.create_text(340,410,text="PLAY GAME",font="courier 18",fill=fillTwo)
                           

    #This part does the all the drawing for the game.
    if canvas.data.gameState == True:
        logo = PhotoImage(file="logo.gif")
        canvas.data.logo = logo
        canvas.create_image(250,315,image=logo)
        
        #Creates the exit box on the top right of the screen
        fillOne = canvas.data.fillOne
        canvas.create_rectangle(450,10,495,30)
        canvas.create_text(473,20,text="EXIT",font="courier",fill=fillOne)

        canvas.create_text(350,50,text="Player 2",font="courier 18",anchor=SW)
        canvas.create_text(350,350,text="Player 1",font="courier 18",anchor=SW)
        
        #Calls the drawGrid function to create the player and enemy grids.
        for row in range(canvas.data.rows):
            for col in range(canvas.data.cols):
                drawGrid(row,col)

        #Labels the rows of the player and enemy grid        
        canvas.create_text(25,50,text="a",font="courier 16",fill="white")
        canvas.create_text(25,75,text="b",font="courier 16",fill="white")
        canvas.create_text(25,100,text="c",font="courier 16",fill="white")
        canvas.create_text(25,125,text="d",font="courier 16",fill="white")
        canvas.create_text(25,150,text="e",font="courier 16",fill="white")
        canvas.create_text(25,175,text="f",font="courier 16",fill="white")
        canvas.create_text(25,200,text="g",font="courier 16",fill="white")
        canvas.create_text(25,225,text="h",font="courier 16",fill="white")
        canvas.create_text(25,250,text="i",font="courier 16",fill="white")
        canvas.create_text(25,275,text="j",font="courier 16",fill="white")  
        canvas.create_text(25,358,text="a",font="courier 16",fill="white")
        canvas.create_text(25,383,text="b",font="courier 16",fill="white")
        canvas.create_text(25,408,text="c",font="courier 16",fill="white")
        canvas.create_text(25,433,text="d",font="courier 16",fill="white")
        canvas.create_text(25,458,text="e",font="courier 16",fill="white")
        canvas.create_text(25,483,text="f",font="courier 16",fill="white")
        canvas.create_text(25,508,text="g",font="courier 16",fill="white")
        canvas.create_text(25,533,text="h",font="courier 16",fill="white")
        canvas.create_text(25,558,text="i",font="courier 16",fill="white")
        canvas.create_text(25,583,text="j",font="courier 16",fill="white")

        #Labels the columns of player and enemy grid
        canvas.create_text(50,25,text="1",font="courier 16",fill="white")
        canvas.create_text(75,25,text="2",font="courier 16",fill="white")
        canvas.create_text(100,25,text="3",font="courier 16",fill="white")
        canvas.create_text(125,25,text="4",font="courier 16",fill="white")
        canvas.create_text(150,25,text="5",font="courier 16",fill="white")
        canvas.create_text(175,25,text="6",font="courier 16",fill="white")
        canvas.create_text(200,25,text="7",font="courier 16",fill="white")
        canvas.create_text(225,25,text="8",font="courier 16",fill="white")
        canvas.create_text(250,25,text="9",font="courier 16",fill="white")
        canvas.create_text(275,25,text="10",font="courier 16",fill="white")
        canvas.create_text(50,335,text="1",font="courier 16",fill="white")
        canvas.create_text(75,335,text="2",font="courier 16",fill="white")
        canvas.create_text(100,335,text="3",font="courier 16",fill="white")
        canvas.create_text(125,335,text="4",font="courier 16",fill="white")
        canvas.create_text(150,335,text="5",font="courier 16",fill="white")
        canvas.create_text(175,335,text="6",font="courier 16",fill="white")
        canvas.create_text(200,335,text="7",font="courier 16",fill="white")
        canvas.create_text(225,335,text="8",font="courier 16",fill="white")
        canvas.create_text(250,335,text="9",font="courier 16",fill="white")
        canvas.create_text(275,335,text="10",font="courier 16",fill="white")
        
        #Uses a red dot to show who's turn it is.
        if (canvas.data.turn == 0) or (canvas.data.turn == 3):
            canvas.create_oval(320,330,345,355,fill="red",width=2)
        if (canvas.data.turn == 2) or (canvas.data.turn == 4):
            canvas.create_oval(320,30,345,55,fill="red",width=2)

        #Displays the counters for hits and misses
        enemyMissCount = "Misses: " + str(canvas.data.enemyMiss)
        enemyHitCount = "Hits: " + str(canvas.data.enemyHit)
        canvas.create_text(350,80,text=enemyMissCount,font="courier",anchor=SW)
        canvas.create_text(350,100,text=enemyHitCount,font="courier",anchor=SW)
        playerMissCount = "Misses: " + str(canvas.data.playerMiss)
        playerHitCount = "Hits: " + str(canvas.data.playerHit)
        canvas.create_text(350,380,text=playerMissCount,font="courier",anchor=SW)
        canvas.create_text(350,400,text=playerHitCount,font="courier",anchor=SW)

        #Shows the box with ships to place on the grid.
        #Once all the ships have been placed the box is removed.
        #Also loads the images of the ships to the box initially.
        if canvas.data.turn == 0:
            x0 = 405
            y0 = 485
            x1 = 325
            y1 = 500
            x2 = 485
            y2 = 615
        if canvas.data.turn == 2:
            x0 = 405
            y0 = 180
            x1 = 325
            y1 = 195
            x2 = 485
            y2 = 310
        if canvas.data.turn == 0 or canvas.data.turn == 2:
            canvas.create_text(x0,y0,text="Ships",font="courier 18")
            canvas.create_rectangle(x1,y1,x2,y2)
            
        if (canvas.data.turn == 0) or (canvas.data.turn == 3):
            (cx,cy) = canvas.data.carrierPosition1
            aircraftCarrier1 = canvas.data.aircraftCarrier1
            canvas.create_image(cx,cy,image=aircraftCarrier1)
            
            (cx,cy) = canvas.data.destroyerPosition1
            destroyer1 = canvas.data.destroyer1
            canvas.create_image(cx,cy,image=destroyer1)
            
            (cx,cy) = canvas.data.submarinePosition1
            submarine1 = canvas.data.submarine1
            canvas.create_image(cx,cy,image=submarine1)
            
            (cx,cy) = canvas.data.patrolPosition1
            patrolboat1 = canvas.data.patrolboat1
            canvas.create_image(cx,cy,image=patrolboat1)

        if (canvas.data.turn == 2) or (canvas.data.turn == 4):
            (cx,cy) = canvas.data.carrierPosition2
            aircraftCarrier2 = canvas.data.aircraftCarrier2
            canvas.create_image(cx,cy,image=aircraftCarrier2)
            
            (cx,cy) = canvas.data.destroyerPosition2
            destroyer2 = canvas.data.destroyer2
            canvas.create_image(cx,cy,image=destroyer2)
            
            (cx,cy) = canvas.data.submarinePosition2
            submarine2 = canvas.data.submarine2
            canvas.create_image(cx,cy,image=submarine2)
            
            (cx,cy) = canvas.data.patrolPosition2
            patrolboat2 = canvas.data.patrolboat2
            canvas.create_image(cx,cy,image=patrolboat2)
            
        if (canvas.data.turn == 0) or (canvas.data.turn == 3):
            fillThree = canvas.data.fillThree
            canvas.create_rectangle(325,440,383,460)
            canvas.create_text(355,450,text="DONE",font="courier 18",fill=fillThree)
        if (canvas.data.turn == 5):
            fillThree = canvas.data.fillThree
            canvas.create_rectangle(325,440,383,460)
            canvas.create_text(355,450,text="START",font="courier 18",fill=fillThree)            
        if (canvas.data.turn == 1):
            fillTwo = canvas.data.fillTwo
            canvas.create_rectangle(325,140,383,160)
            canvas.create_text(354,150,text="START",font="courier 18",fill=fillTwo)
        if (canvas.data.turn == 2) or (canvas.data.turn == 4):
            fillTwo = canvas.data.fillTwo
            canvas.create_rectangle(325,140,383,160)
            canvas.create_text(354,150,text="DONE",font="courier 18",fill=fillTwo)

        #Draws the red or white pegs depending on if it's a hit or a miss.
        for row in range(canvas.data.rows):
            for col in range(canvas.data.cols):
                drawPegs(row,col)

        #If either one of the players wins, displays which player won.
        if canvas.data.turn == 6:
            canvas.create_rectangle(100,250,400,350,fill="white")
            canvas.create_text(250,300,text="Player 1 wins!",font="courier 26")
        if canvas.data.turn == 7:
            canvas.create_rectangle(100,250,400,350,fill="white")
            canvas.create_text(250,300,text="Player 2 wins!",font="courier 26")


def init():
    ####################
    #Player 1 Variables#
    ####################
    canvas.data.playerHit = 0
    canvas.data.playerMiss = 0
    canvas.data.rotatedOne1 = False #Aircraft carrier rotated? True or False
    canvas.data.rotatedTwo1 = False #Destroyer rotated?
    canvas.data.rotatedThree1 = False #Submarine rotated?
    canvas.data.rotatedFour1 = False #Patrol Boat rotated?
    canvas.data.currentShip1 = 0 #1 for carrier, 2 for destroyer, 3 for submarine, 4 for patrol boat
    aircraftCarrier1 = PhotoImage(file="aircraftcarrier.gif")
    canvas.data.aircraftCarrier1 = aircraftCarrier1
    canvas.data.carrierPosition1 = (350,555)
    destroyer1 = PhotoImage(file="destroyer.gif")
    canvas.data.destroyer1 = destroyer1
    canvas.data.destroyerPosition1 = (385,555) 
    submarine1 = PhotoImage(file="submarine.gif")
    canvas.data.submarine1 = submarine1
    canvas.data.submarinePosition1 = (420,555)
    patrolboat1 = PhotoImage(file="patrolboat.gif")
    canvas.data.patrolboat1 = patrolboat1
    canvas.data.patrolPosition1 = (450,555)
    canvas.data.playerGrid = [[0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0]]
    canvas.data.playerGrid1 = [[0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0]]

    ####################
    #Player 2 Variables#
    ####################
    canvas.data.enemyHit = 0
    canvas.data.enemyMiss = 0
    canvas.data.rotatedOne2 = False #Aircraft carrier rotated? True or False
    canvas.data.rotatedTwo2 = False #Destroyer rotated?
    canvas.data.rotatedThree2 = False #Submarine rotated?
    canvas.data.rotatedFour2 = False #Patrol Boat rotated?
    canvas.data.currentShip2 = 0 #1 for carrier, 2 for destroyer, 3 for submarine, 4 for patrol boat 
    aircraftCarrier2 = PhotoImage(file="aircraftcarrier.gif")
    canvas.data.aircraftCarrier2 = aircraftCarrier2
    canvas.data.carrierPosition2 = (350,253)    
    destroyer2 = PhotoImage(file="destroyer.gif")
    canvas.data.destroyer2 = destroyer2
    canvas.data.destroyerPosition2 = (385,253)    
    submarine2 = PhotoImage(file="submarine.gif")
    canvas.data.submarine2 = submarine2
    canvas.data.submarinePosition2 = (420,253)    
    patrolboat2 = PhotoImage(file="patrolboat.gif")
    canvas.data.patrolboat2 = patrolboat2
    canvas.data.patrolPosition2 = (450,253)
    canvas.data.enemyGrid = [[0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0]]
    canvas.data.enemyGrid1 = [[0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0]]

    ##################
    #Global Variables#
    ##################
    canvas.data.clickCounter = 0
    canvas.data.currentCoordX = 0
    canvas.data.currentCoordY = 0
    canvas.data.menuState = True
    canvas.data.instrucState = False
    canvas.data.gameState = False   
    canvas.data.turn = 0
    #0 = Player 1 place ships
    #1 = Both screens hidden, player 2 has to press start
    #2 = Player 2 places ships
    #3 = Player 1 turn
    #4 = Player 2 turn
    #Once game has started it switches between 1, 3, 4, and 5 till someone wins.
    #5 = Both screens hidden, player 1 has to press start
    #6 = Player 1 wins
    #7 = Player 2 wins
    canvas.data.buttonFill = "blue"
    canvas.data.fillOne = "white"
    canvas.data.fillTwo = "white"
    canvas.data.fillThree = "white"
    canvas.data.rows = 10
    canvas.data.cols = 10
    canvas.data.colWidth = 25
    canvas.data.rowHeight = 25
    canvas.data.margin = 10
    pass

########### copy-paste below here ###########

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    canvas = Canvas(root, width=500, height=630)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init()
    # set up events
    if (canvas.data.gameState == True):
        root.bind("<Button-1>", leftMousePressed)
    else: root.bind("<Button-1>",mousePressed)
    canvas.bind("<Motion>", mouseMotion)
    canvas.bind("<B1-Motion>", leftMouseMoved)
    root.bind("<B1-ButtonRelease>", leftMouseReleased)
    root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
