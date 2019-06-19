import wpf

from System.Windows import Window

class GUIpy(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'GUIpy.xaml')
