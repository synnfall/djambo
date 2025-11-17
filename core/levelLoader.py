import os
from environment import Environment
from entity.player import Player
from entity.wall import Wall
from entity.exit import Exit

class LevelLoader:
    levels: list

    def __init__(self):
        self.levels = []
        for i in range(Environment.LEVELNUMBER):
            level = self.parseLevel("level"+str(i+1))
            self.levels.append(level)

    def parseLevel(self, levelName: str):
        path = os.path.join(os.path.dirname(__file__), '..', 'levels', levelName)
        path = os.path.abspath(path)
        with open(path, "r") as f:
            lines = [line.rstrip("\n") for line in f]
        return lines

    def loadLevel(self, levelIndex: int, wallSprites):
        level = self.levels[levelIndex]
        res = {
            'Wall': []
        }
        for i in range(len(level)):
            for j in range(len(level[i])):
                entity = level[i][j]
                pos = (j*Environment.RECTSIZE,i*Environment.RECTSIZE)
                match entity:
                    case '#':
                        res['Wall'].append(Wall(pos, wallSprites))
                    case 'P':
                        res['Player'] = Player(pos)
                    case 'E':
                        res['Exit'] = Exit(pos)
        return res