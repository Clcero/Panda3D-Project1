# Luke Classen, 6/5/2024

# Create 3D scenes
from direct.showbase.ShowBase import ShowBase
import math, sys, random

# Derived from ShowBase to be Panda-related
class MyApp(ShowBase):

    # Declare constructor
    def __init__(self):

        # Run ShowBase stuff
        ShowBase.__init__(self)
        self.SetupScene()

        # Start setting key bindings.
        self.accept('escape', self.quit)

    def SetupScene(self):
        '''Load universe and planet'''
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        
        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(random.randint(100, 150), random.randint(3000, 5000), random.randint(50, 75)) 
        self.Planet1.setScale(350)

        tex = self.loader.loadTexture("./Assets/Universe/Universe.jpg")
        tex2 = self.loader.loadTexture("./Assets/Universe/Universe.jpg")
        self.Universe.setTexture(tex, 1)
        self.Planet1.setTexture(tex2, 1)
        

    # Prepare message if server wants to quit.
    def quit(self):
        sys.exit()
        
# Instances, then runs program
app = MyApp()
app.run()