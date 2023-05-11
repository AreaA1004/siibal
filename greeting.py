pip install git+https://github.com/peterbrittain/asciimatics.git
from asciimatics.effects import Print
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen

def demo(screen: Screen):
 x = "HELLO"
 text = Rainbow(screen, FigletText(x, font="basic"))
 screen.play([Scene([ Print(screen, text, (screen.height - text.max_height) // 2, (screen.width - text.max_width) // 2,),])])
if __name__ == "__main__":
 Screen.wrapper(demo)
