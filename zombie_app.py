from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3


class ZombieApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment
        self.scene = self.loader.loadModel("model/environment")
        # Reparent the scene to the render
        self.scene.reparentTo(self.render)

        # Apply stretching and shifting to it
        self.scene.set_scale(0.25, 0.25, 0.25)
        self.scene.set_pos(-8, 100, 0)

        self.imitator = Actor("Imitator/imitator.egg")
        print(self.imitator)

        self.imitator.reparentTo(self.render)


zomb = ZombieApp()
zomb.run()