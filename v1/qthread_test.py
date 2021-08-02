from pynput import keyboard
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QObject
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from window import Window
from file_handler import File_Handler
import sys
import os

class Worker(QThread) :

    def __init__(self, parent_) : 

        QThread.__init__(self)

        self.key_1_listener = keyboard.Listener(on_press = self.key_1_press, on_release = self.key_1_release)
        self.key_2_listener = keyboard.Listener(on_press = self.key_2_press, on_release = self.key_2_release)
        self.key_3_listener = keyboard.Listener(on_press = self.key_3_press, on_release = self.key_3_release)

        self.parent = parent_

        print(f' SELF.PARENT : {self.parent}')

        self.test_signal_value = pyqtSignal(int)

        self.keys = list(self.parent.file_dictionary.keys())

        self.key_1_pressed = False
        self.key_2_pressed = False

        self.vertical_pointer = 0

        self.horizontal_pointer = 0

    def run(self) :

        self.key_1_listener.start()
        self.key_2_listener.start()
        self.key_3_listener.start()
        self.signal_listener()

    def signal_listener(self) : 

        while True :

            if self.key_1_pressed == True and self.key_2_pressed == True : 

                self.parent.window.show()

            else : 

                self.parent.window.hide()

    def key_1_press(self, key) : 

        if str(key) == self.parent.window.config['key_1'] :

            print('key 1 press')

            self.key_1_pressed = True
            # self.parent.window.show()

    def key_1_release(self, key) :

        if str(key) == self.parent.window.config['key_1'] :

            print('key 1 release')

            self.key_1_pressed = False

    def key_2_press(self, key) : 

        if str(key) == self.parent.window.config['key_2'] : 

            print('key 2 press')

            self.key_2_pressed = True

        print(f'KEY : {str(key)}')


        if str(key) == self.parent.window.config['key_exit'] : 

            print('TRUE')
            # sys.exit()
            os._exit(400)
            self.key_1_listener.stop()
            self.key_2_listener.stop()
            self.key_3_listener.stop()

    def key_2_release(self, key) : 

        if str(key) == self.parent.window.config['key_2'] : 

            print('key 2 release')

            self.key_2_pressed = False

    def key_3_press(self, key) : 

        print(self.vertical_pointer)        

    def key_3_release(self, key) : 

        if str(key) == self.parent.window.config['key_up'] : 

            if self.vertical_pointer < len(self.parent.file_dictionary[self.keys[self.horizontal_pointer]]) - 1 : 

                # try :

                    self.vertical_pointer += 1

                    self.file_name = self.parent.file_dictionary[self.keys[self.horizontal_pointer]][self.vertical_pointer]

                    self.file_name = self.keys[self.horizontal_pointer] + '/' + self.file_name 

                    print(f'UP : {self.file_name}')

                    self.parent.window.update_image(self.file_name)

                # except : 
                
                    # print(self.vertical_pointer)

        if str(key) == self.parent.window.config['key_down'] : 

            if self.vertical_pointer > 0:


                self.vertical_pointer -= 1

                self.file_name = self.parent.file_dictionary[self.keys[self.horizontal_pointer]][self.vertical_pointer]

                self.file_name = self.keys[self.horizontal_pointer] + '/' + self.file_name 

                print(f'DOWN : {self.file_name}')

                self.parent.window.update_image(self.file_name)

        if str(key) == self.parent.window.config['key_right'] :

            # print('LEFT CLICKED')

            if self.horizontal_pointer < len(self.parent.file_dictionary[self.keys[self.horizontal_pointer]]) - 1  :

                self.vertical_pointer = 0

                self.horizontal_pointer += 1

                print(list(self.keys))

                self.file_name = self.parent.file_dictionary[self.keys[self.horizontal_pointer]][self.vertical_pointer]

                print(self.file_name)

                self.file_name = self.keys[self.horizontal_pointer] + '/' + self.file_name 

                self.parent.window.update_image(self.file_name)


        if str(key) == self.parent.window.config['key_left'] :

            # print('LEFT CLICKED')

            if self.horizontal_pointer >= 0 :

                self.vertical_pointer = 0

                self.horizontal_pointer -= 1

                print(list(self.keys))

                self.file_name = self.parent.file_dictionary[self.keys[self.horizontal_pointer]][self.vertical_pointer]

                print(self.file_name)

                self.file_name = self.keys[self.horizontal_pointer] + '/' + self.file_name 

                self.parent.window.update_image(self.file_name)


class Window_Handler(QObject) : 

    def __init__(self):
        super(Window_Handler, self).__init__() 

        # self.setStyleSheet('background-color: rgba(10,0,0,100)')

        self.load_window()

        self.load_file_handler()

        print(f'WINDOW : {self.window}')
        
        self.load_thread()

    
    def load_window(self) : 

        self.window = Window(test_image = 'Images/Image_Dir_1/test_1.png')

    
    def load_file_handler(self) :

        self.file_handler = File_Handler(self.window.config['image_parent_directory'])

        self.file_dictionary = self.file_handler.file_dictionary


    
    def load_thread(self) :

        self.thread = QThread()

        self.thread_worker = Worker(parent_ = self)

        print(f'SELF : {self}')

        self.thread_worker.moveToThread(self.thread)

        self.thread_worker.start()


if __name__ == '__main__' : 

    app = QApplication(sys.argv) 

    win = Window_Handler()
    
    app.exec_()
