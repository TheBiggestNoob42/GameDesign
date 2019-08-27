from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import NodePath
from panda3d.core import Camera
from panda3d.core import OrthographicLens
from panda3d.core import DisplayRegion
import direct.directbase.DirectStart
import sys

dr = base.win.makeDisplayRegion()
dr.setSort(20)

myCamera2d = NodePath(Camera('myCam2d'))
lens = OrthographicLens()
lens.setFilmSize(2, 2)
lens.setNearFar(-1000, 1000)
myCamera2d.node().setLens(lens)

myRender2d = NodePath('myRender2d')
myRender2d.setDepthTest(False)
myRender2d.setDepthWrite(False)
myCamera2d.reparentTo(myRender2d)
dr.setCamera(myCamera2d)
