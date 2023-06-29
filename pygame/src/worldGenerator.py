import random
from ground import Platform
from pygame import sprite

amountOfLevels = 300
removeBlocks = 190
WORLD_HEIGHT = 800
WORLD_WIDTH = 1024
PLATFORM_HEIGHT = 40
PLATFORM_WIDTH = 40

def generateLevel():
    stepper = {
        "wallCount": removeBlocks,
        "padding": 2,
        'x': int(WORLD_WIDTH//PLATFORM_WIDTH//2),
        'y': int(WORLD_HEIGHT//PLATFORM_HEIGHT//2),
    }
    def levelRow():
        return ["#"]* int(WORLD_WIDTH//PLATFORM_WIDTH)

    start_coords = (stepper['x'], stepper['y'])
    level = [levelRow() for _ in range(WORLD_HEIGHT//PLATFORM_HEIGHT)]
    x = -1
    y = -1
    while stepper['wallCount'] >= 0:
        x = stepper['x']
        y = stepper['y']

        if level[y][x] == "#":
            level[y][x] = " "
            stepper['wallCount'] -= 1
        roll = random.randint(1, 4)

        if roll == 1 and x > stepper['padding']:
            stepper['x'] -= 1
        if roll == 2 and x < WORLD_WIDTH//PLATFORM_WIDTH- 1 - stepper['padding']:
            stepper['x'] += 1
        if roll == 3 and y > stepper['padding']:
            stepper['y'] -= 1
        if roll == 4 and y < WORLD_HEIGHT//PLATFORM_HEIGHT - 1 - stepper['padding']:
            stepper['y'] += 1
    end_coords = [x, y]
    
    return [level, start_coords, end_coords]


def getNextMoves(x, y):
    return {
        'left':  [x-1, y], 
        'right': [x+1, y],
        'up':  [x, y-1],
        'down':  [x, y+1]
    }.values()
 
def getShortestPath(level, startCoordinate, endCoordinate):
    searchPaths = [[startCoordinate]]
    visitedCoordinates = [startCoordinate]
    
    while searchPaths != []:
        currentPath = searchPaths.pop(0)
        currentCoordinate = currentPath[-1]
        
        currentX, currentY = currentCoordinate
        
        if currentCoordinate == endCoordinate:
            return currentPath
        
        for nextCoordinate in getNextMoves(currentX, currentY):
            nextX, nextY = nextCoordinate
            
            if nextX < 0 or nextX >= 1024:
                continue
            
            if nextY < 0 or nextY >= 800:
                continue
            
            if nextCoordinate in visitedCoordinates:
                continue
            
            if level[nextY][nextX] == '#':
                continue
            
            searchPaths.append(currentPath + [nextCoordinate])
            visitedCoordinates += [nextCoordinate]
    
    return []

def generateLevels(amount):
    return [generateLevel() for _ in range(amount)]

def evaluateLevels(levels):
    evaluationScores = []
    
    for generatedLevel, startCoordinate, endCoordinate in levels:
        shortestSolution = getShortestPath(
            generatedLevel, 
            startCoordinate, 
            endCoordinate
        )
        
        evaluationScores.append(
            [len(shortestSolution), generatedLevel]
        )
    
    return evaluationScores
 
def generateBestLevel(amountOfLevels):
    levels = generateLevels(amountOfLevels)
    
    evaluationScores = evaluateLevels(levels)
    
    evaluationScores.sort()
    evaluationScores.reverse()
    
    score, bestLevel = evaluationScores.pop(0)
    
    return bestLevel

def initLevel():
    bestLevel = generateBestLevel(amountOfLevels)
    platform_group = sprite.Group()
    for i,row in enumerate(bestLevel):
        for j,wall in enumerate(row):
            if wall == "#":
                platform = Platform(j*PLATFORM_WIDTH, i*PLATFORM_HEIGHT, PLATFORM_HEIGHT, PLATFORM_WIDTH)
                platform_group.add(platform)
    return platform_group, bestLevel