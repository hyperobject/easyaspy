Sprites = []
Scripts = []
Blocks = []
class Sprite():
    global Sprites, Scripts
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 90
        self.hidden = False
        self.myScripts = []
        self.name = "Sprite1"
    def run(self):
        for i in self.myScripts:
            i.run()
class Script():
    global Sprites, Scripts, Blocks
    def __init__(self):    
        global Sprites
        self.id = 0
        self.loops = []
        self.myBlocks = []
        self.pos = 0
		self.running = False
        self.owner = 0
        k = 0
        for i in Sprites:
            for j in i.myScripts:
                if j.id == self.id:
                    self.owner = k
                k += 1
    def run(self):
        if self.pos == -1:
            if self.loops[0][2] == len(self.myBlocks):
                self.pos = self.loops[0][1]
            else:
                if self.myBlocks[0].run() == True:
                    self.pos == 0
        if self.pos == 0 and self.myBlocks[0].run() == True:
            self.pos = 1
        self.myBlocks[pos].run()
class Block():
    global Scripts, Blocks
    def __init__(self):
        global Scripts
        self.id = 0
        self.block = 0
        self.inputs = []
        self.complete = False
        self.running = False
        k = 0
        for i in Scripts:
            for j in i.myBlocks:
                if j.id == self.id:
                    self.owner = k
                    k += 1
    def check(self):
        global Scripts
        if self.running == False:
            Scripts[self.owner].pos += 1
            if (Scripts[self.owner].pos + 1) > len(Scripts[self.owner].myBlocks):
                Scripts[self.owner].pos = -1
    def run(self):
        global Sprites, Scripts, answer
        for i in range(len(self.inputs)):
            if type(self.inputs[i]) == type(Sprites[0]):
                self.inputs[i] = self.inputs[i].run()
        if self.block == 0: #say
            string = str(self.inputs[0])
            print(string)
        if self.block == 1: #ask
            string = str(self.inputs[0])
            answer = raw_input(string)
        from math import sqrt
        if self.block == 2: #join
            a = str(self.inputs[0])
            b = str(self.inputs[1])
            return a + b
        if self.block == 3: #mod
            return self.inputs[0] % self.inputs[1]
        if self.block == 4: #letter of
            string = str(self.inputs[1])
            num = (self.inputs[0] - 1) % len(string)
            return string[num]
        if self.block == 5: #length of
            string = str(self.inputs[0])
            return len(string)
        if self.block == 6: #broadcast
            for i in range(len(Scripts)):
			    if Scripts[i].myBlocks[0].block == 7 and Scripts[i].myBlocks[0].inputs[0] == self.inputs[0] and Scripts[i].running == False:
				    Scripts[i].pos = 1
					Scripts[i].running = True
		# block type 7 is a hat, and therefore, will not be defined. Only it's trigger will; it's block type 6.
if __name__ == "__main__":
    print "Block definitions and paralell scripting for EasyAsPy."