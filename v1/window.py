from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QGridLayout
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap
from PIL import Image
from yaml import load, Loader

class Window(QMainWindow) : 

    def __init__(self, parent = None, test_image = None) :

        super(Window, self).__init__()

        self.load_config()

        self.test_image = test_image

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.load_ui()
        
        self.load_image()

        self.config_window()

    def load_ui(self) : 

        self.widget = QWidget(self)

        self.layout = QGridLayout(self.widget)

        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def load_config(self) : 

        with open('config.yaml', 'r') as config_file : 

            self.config = load(config_file, Loader = Loader)

    def config_window(self) : 

        self.setGeometry(self.config['window_position_x'], self.config['window_position_y'], self.image.width, self.image.height)

        self.layout.setContentsMargins(self.config['image_margin'], self.config['image_margin'], self.config['image_margin'], self.config['image_margin'])

    def load_image(self) :

        self.label = QLabel()

        self.qpixmap = QPixmap(self.test_image)

        self.label.setPixmap(self.qpixmap)

        self.image = Image.open(self.test_image)

        self.layout.addWidget(self.label)

    def update_image(self, image) : 

        self.qpixmap = QPixmap(image)

        self.label.setPixmap(self.qpixmap)

        self.image = Image.open(image)

        self.setGeometry(self.config['window_position_x'], self.config['window_position_y'], self.image.width, self.image.height)

if __name__ == '__main__' :

    from PyQt5.QtWidgets import QApplication
    import sys

    pyrefer_app = QApplication(sys.argv)

    pyrefer_win = Window(test_image = 'Images/Image_Dir_1/test_1.png')

    pyrefer_win.show()

    sys.exit(pyrefer_app.exec_())
