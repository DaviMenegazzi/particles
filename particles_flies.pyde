import random

def setup():
    size(1200, 500)
    
n = 100 #Quantidade de bolinhas na tela
l =  [] #Lista da posição x e y das bolinhas

#Velocidade das bolinhas no eixo x
v = 20

for i in range(n):
    
    #As posições são dispostas aleatoriamente
    posx = random.randint(0, 1200) 
    posy = random.randint(0, 500) 
    
    #Adiciona pra lista
    l.append({"posx": posx, "posy": posy})
    
def draw():
    background(0)
    smooth()
    global posx, posy, n, v
    
    for i in range(n):
        random_posx = l[i]["posx"]
        random_posy = l[i]["posy"]
        
        b = Balls(random_posx, random_posy)
        b.stayInCanvas()
        b.build()
        
        
        #valor da distancia pras bolinhas se conectarem
        d = 200
        
        l[i]["posx"] = l[i]["posx"] + (v * random.randint(-1, 1)) * cos(v)
        l[i]["posy"] = l[i]["posy"] + (v * random.randint(-1, 1)) * cos(v)
        
        if dist(l[i]["posx"], l[i]["posy"], l[i * -1]["posx"], l[i * -1]["posy"]) < d: #se a distancia entre as bolinhas forem menor que o valor da variavel d
            stroke(255)
            line(l[i]["posx"], l[i]["posy"], l[i * -1]["posx"], l[i * -1]["posy"])
    
    
class Balls:
    def __init__(self, posx, posy):
        self.posx        = posx
        self.posy        = posy
        self.sizBall     = random.randint(0, 9)
        
    def build(self):
        ellipse(self.posx, self.posy, self.sizBall, self.sizBall)
        
    def stayInCanvas(self):
        self.posx = constrain(self.posx, 0, width)
        self.posy = constrain(self.posy, 0, height)
        
def mousePressed():
    loop()
        
