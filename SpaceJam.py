# Luke Classen, 6/5/2024

from direct.showbase.ShowBase import ShowBase
import math, sys, random

class MyApp(ShowBase):

    def __init__(self):

        ShowBase.__init__(self)

        # Create world
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

        # Space Station (space station)
        self.SpaceStation = self.loader.loadModel("./Assets/Space Station/station.glb")
        self.SpaceStation.reparentTo(self.render)
        stationTex = self.loader.loadTexture("./Assets/Space Station/Metal.jpg")
        self.SpaceStation.setTexture(stationTex, 1)
        self.SpaceStation.setPos(75, 500, 100)

        # Player (banana)
        self.player = self.loader.loadModel("./Assets/Spaceships/spaceship.obj")
        self.player.reparentTo(self.render)
        playerTex = self.loader.loadTexture("./Assets/Spaceships/spaceship.jpg")
        self.player.setScale(0.5)
        self.player.setHpr(0, 0, 90)
        self.player.setTexture(playerTex, 1)
        self.player.setPos(75, 500, -100)

        # Path dictionary
        planets = [
            {"model_path": "./Assets/Planets/protoPlanet.x", "texture_path": "./Assets/Planets/Mars.jpg"},
            {"model_path": "./Assets/Planets/protoPlanet.x", "texture_path": "./Assets/Planets/Purple.png"},
            {"model_path": "./Assets/Planets/protoPlanet.x", "texture_path": "./Assets/Planets/Sand.png"},
            {"model_path": "./Assets/Planets/protoPlanet.x", "texture_path": "./Assets/Planets/Tiled.jpg"},
            {"model_path": "./Assets/Planets/protoPlanet.x", "texture_path": "./Assets/Planets/Wicker.jpg"},
            {"model_path": "./Assets/Planets/protoPlanet.x", "texture_path": "./Assets/Planets/Rock.jpg"}
        ]

        # Spawn planets at "random" positions within the player's view
        for i, planet_spec in enumerate(planets):
            planet = self.loader.loadModel(planet_spec["model_path"])
            planet.setTexture(self.loader.loadTexture(planet_spec["texture_path"]), 1)
            planet.setPos(random.randint(-2000, 8000), random.randint(3000, 6000), random.randint(350, 2550)) # Planets occasionally collide
            planet.setScale(350)
            planet.reparentTo(self.render)
            setattr(self, f"Planet{i+1}", planet)


    # Prepare message if server wants to quit.
    def quit(self):
        '''Exit game.'''
        sys.exit()
        
# Instances, then runs program
app = MyApp()
app.run()