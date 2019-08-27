import direct.directbase.DirectStart
from direct.task import Task
from direct.actor import Actor
from panda3d.core import NodePath
from math import pi, sin, cos

# Load the first environment model
environ = loader.loadModel("models/environment")
print(type(environ))
environ.reparentTo(render)
environ.setScale(0.25, 0.25, 0.25)
environ.setPos(-8, 42, 0)

# Task to move the camera
def SpinCameraTask(task):
    angledegrees = task.time * 6.0
    angleradians = angledegrees * (pi / 180.0)
    base.camera.setPos(20 * sin(angleradians), 20 * cos(angleradians), 3)
    base.camera.setHpr(angledegrees, 0, 0)
    return Task.cont


taskMgr.add(SpinCameraTask, "SpinCameraTask")

# Run the tutorial
run()