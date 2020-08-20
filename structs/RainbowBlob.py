import random
from threading import Timer


class RainbowBlob:

    def __init__(self,spawnTime,pixelCount):
        self.position = random.randint(30, pixelCount-30)
        self.rainbowColor=0
        self.timeRemaining=60*5
        self.isEatable=False
        self.spawned=False
        self.spawnTime=spawnTime
        self.pixelCount=pixelCount
        self.size=18
        Timer(random.randint(max(spawnTime-10,0),spawnTime+10), self.respawn).start()
    
    def draw(self,colors):
        if self.spawned:
            self.timeRemaining-=1
            
            for i in range(self.size):
                colors[self.position+i][0]=self.rainbowColor
                colors[self.position+i][1]=1
                colors[self.position+i][2]=1
            if self.timeRemaining>0:
                colors[self.position-1][0]=0
                colors[self.position-1][1]=0
                colors[self.position-1][2]=1

                colors[self.position-2][0]=0
                colors[self.position-2][1]=0
                colors[self.position-2][2]=1

                colors[self.position+self.size][0]=0
                colors[self.position+self.size][1]=0
                colors[self.position+self.size][2]=1

                colors[self.position+self.size+1][0]=0
                colors[self.position+self.size+1][1]=0
                colors[self.position+self.size+1][2]=1

            else:
                self.isEatable=True

            self.rainbowColor+=0.02
            self.rainbowColor%=1.0

    def respawn(self):
        self.position = random.randint(30, self.pixelCount-30)
        self.rainbowColor=0
        self.timeRemaining=60*5
        self.isEatable=False
        self.spawned=True
        Timer(random.randint(max(self.spawnTime-10,0),self.spawnTime+10), self.respawn).start()