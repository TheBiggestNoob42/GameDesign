from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from direct.showbase.ShowBase import ShowBase

from panda3d.core import TextNode


class TextOnScreen(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.bk_text = "Text Demo"
        self.textObject = OnscreenText(text=self.bk_text, pos=(0.95, -0.95),
                          scale=0.07, fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter, mayChange=1)

        self.b = DirectButton(text=("OK", "click!", "rolling over", "disabled"), text_scale=0.5, scale=0.9,
                         command=self.set_text)

        self.b.reparent_to(self.render2d)

    def set_text(self):
        self.bk_text = "Button Clicked"
        self.textObject.setText(self.bk_text)


TextApp = TextOnScreen()
TextApp.run()
