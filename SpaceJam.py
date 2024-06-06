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
        '''Load universe, space station, player, then randomly place the planets.'''

        # Universe
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        uniTex = self.loader.loadTexture("./Assets/Universe/Universe.jpg")
        self.Universe.setTexture(uniTex, 1)

        # Space Station
        self.SpaceStation = self.loader.loadModel("./Assets/Space Station/station.glb")
        self.SpaceStation.reparentTo(self.render)
        stationTex = self.loader.loadTexture("./Assets/Space Station/Metal.jpg")
        self.SpaceStation.setTexture(stationTex, 1)
        self.SpaceStation.setPos(75, 500, 100)

        # self.player = self.loader.loadModel.(".")

        # Path dictionary
        planets = [
            {"model_path": "./Assets/Planets/protoPlanet.x", "texture_path": "./Assets/Planets/Mars.jpg"},
            {"model_path": "./Assets/Planets/protoPlanet.x", "texture_path": "./Assets/Planets/Purple.png"},
            {"model_path": "./Assets/Planets/protoPlanet.x", "texture_path": "./Assets/Planets/Sand.png"},
            {"model_path": "./Assets/Planets/protoPlanet.x", "texture_path": "./Assets/Planets/Tiled.jpg"},
            {"model_path": "./Assets/Planets/protoPlanet.x", "texture_path": "./Assets/Planets/Wicker.jpg"},
            {"model_path": "./Assets/Planets/protoPlanet.x", "texture_path": "./Assets/Planets/Rock.jpg"}
        ]

        # Spawn planets at random positions
        for i, planet_spec in enumerate(planets):
            planet = self.loader.loadModel(planet_spec["model_path"])
            planet.setTexture(self.loader.loadTexture(planet_spec["texture_path"]), 1)
            planet.setPos(random.randint(-2000, 8000), random.randint(3000, 6000), random.randint(350, 2550))
            planet.setScale(350)
            planet.reparentTo(self.render)
            setattr(self, f"Planet{i+1}", planet)


    # Prepare message if server wants to quit.
    def quit(self):
        sys.exit()
        
# Instances, then runs program
app = MyApp()
app.run()