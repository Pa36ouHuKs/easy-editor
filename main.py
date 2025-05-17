#создай тут фоторедактор Easy Editor!
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton
import os
from PIL import Image, ImageOps, ImageFilter
from PyQt5.QtGui import QPixmap
from tkinter import Tk #для закрытия окна, нашел только такое
global er
global brail
brail = 0
er = 0
class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.image = None
        self.directory = None
        self.savedir = 'Modified/'
    def loadImage(self, filename):
        self.filename = filename
        self.directory = workdir
        imagePath = os.path.join(self.directory, self.filename)
        self.image = Image.open(imagePath)
    def showImage(self, path):
        pixMapImage = QPixmap(path)
        label_width = image_label.width()
        label_height = image_label.height()
        scaled_pixMap = pixMapImage.scaled(label_width, label_height, Qt.KeepAspectRatio)
        image_label.setPixmap(scaled_pixMap)
        image_label.setVisible(True)
    def saveImage(self):
        path = os.path.join(self.directory, self.savedir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        imagePath = os.path.join(path, self.filename)
        self.image.save(imagePath)
    def do_bw(self):
        if List.selectedItems():
            self.image = ImageOps.grayscale(self.image)
            self.saveImage()
            image_path = os.path.join(self.directory, self.savedir, self.filename)
            self.showImage(image_path)
        else:
            global er
            global brail
            global main_win, button_bw, image_label, button_left, button_right, button_mirror, button_p, button_sharpen
            if er == 0:
                Error_win = QMessageBox()
                Error_win.setText('Может для начала нужно выбрать картинку?')
                Error_win.exec()
                er = 1
            elif er == 1:
                Error_win = QMessageBox()
                Error_win.setText('Эмм, ты промахнулся, напомню, надо выбрать картинку')
                Error_win.exec()
                er = 2
            elif er == 2:
                Error_win = QMessageBox()
                Error_win.setText('Ты издеваешься? Нажми кнопку "Папка"!')
                Error_win.exec()
                er = 3
            elif er == 3:
                Error_win = QMessageBox()
                Error_win.setText('У тебя что то не так? Кнопка. "Папка". НАЖМИ. НА. НЕЕ.')
                Error_win.exec()
                er = 4
            elif er >= 4 and er != 20 and er != 50 and er != 70 and er != 100:
                if brail == 1:
                    Error_win = QMessageBox()
                    Error_win.setText('⠞⠑⠃⠑⠀⠵⠁⠝⠫⠞⠾⠎⠫⠀⠝⠑⠀⠟⠑⠍⠢')
                    Error_win.exec()
                    er += 1
                else:
                    Error_win = QMessageBox()
                    Error_win.setText('Тебе заняться не чем?')
                    Error_win.exec()
                    er += 1
            elif er == 20:
                Error_win = QMessageBox()
                Error_win.setText('У тебя точно нет проблем со зрением?')
                Error_win.exec()
                er += 1
            elif er == 50:
                Error_win = QMessageBox()
                Error_win.setText('Значит есть, да? Ладно, как хочешь. Я поменяю ВЕСЬ интерфейс на Шрифт Брайля. Надеюсь тебе станет легче)')
                Error_win.exec()
                main_win.setWindowTitle('⠑⠁⠎⠽⠀⠑⠙⠊⠞⠕⠗')
                button_p.setText('⠏⠁⠏⠅⠁')
                button_left.setText('⠇⠑⠺⠕')
                button_right.setText('⠏⠗⠁⠺⠕')
                button_mirror.setText('⠵⠑⠗⠅⠁⠇⠕')
                button_sharpen.setText('⠗⠑⠵⠅⠕⠎⠞⠾')
                button_bw.setText('⠟⠀⠃')
                image_label.setText('⠅⠁⠗⠞⠊⠝⠅⠁')
                #АХХАХАХАХАХ, Я ГЕНИЙ
                er += 1
                brail = 1
            elif er == 70:
                Error_win = QMessageBox()
                Error_win.setText('Че как, прикольно точки читать? Ладно ладно, может ты и в правду не замечаешь эту кнопку. Для тебя я ее выделю, а язык верну обратно. Только перестань.')
                Error_win.exec()
                main_win.setWindowTitle('Easy Editor')
                button_p.setText('ВОТ. ЭТА. КНОПКА.')
                button_left.setText('Лево')
                button_right.setText('Право')
                button_mirror.setText('Зеркало')
                button_sharpen.setText('Резкость')
                button_bw.setText('Ч/Б')
                image_label.setText('Картинка')
                er += 1
                brail = 0
            elif er == 100:
                Error_win = QMessageBox()
                Error_win.setText('Ты все еще здесь?! Кто ты такой? Проваливай отсюда, мне здесь такие не нужны.')
                Error_win.exec()
                main_win = Tk()
                main_win.destroy()
            #здесь что то будет
    def do_left(self):
        if List.selectedItems():
            self.image = self.image.rotate(90)
            self.saveImage()
            image_path = os.path.join(self.directory, self.savedir, self.filename)
            self.showImage(image_path)
        else:
            global er
            global brail
            global main_win, button_bw, image_label, button_left, button_right, button_mirror, button_p, button_sharpen
            if er == 0:
                Error_win = QMessageBox()
                Error_win.setText('Может для начала нужно выбрать картинку?')
                Error_win.exec()
                er = 1
            elif er == 1:
                Error_win = QMessageBox()
                Error_win.setText('Эмм, ты промахнулся, напомню, надо выбрать картинку')
                Error_win.exec()
                er = 2
            elif er == 2:
                Error_win = QMessageBox()
                Error_win.setText('Ты издеваешься? Нажми кнопку "Папка"!')
                Error_win.exec()
                er = 3
            elif er == 3:
                Error_win = QMessageBox()
                Error_win.setText('У тебя что то не так? Кнопка. "Папка". НАЖМИ. НА. НЕЕ.')
                Error_win.exec()
                er = 4
            elif er >= 4 and er != 20 and er != 50 and er != 70 and er != 100:
                if brail == 1:
                    Error_win = QMessageBox()
                    Error_win.setText('⠞⠑⠃⠑⠀⠵⠁⠝⠫⠞⠾⠎⠫⠀⠝⠑⠀⠟⠑⠍⠢')
                    Error_win.exec()
                    er += 1
                else:
                    Error_win = QMessageBox()
                    Error_win.setText('Тебе заняться не чем?')
                    Error_win.exec()
                    er += 1
            elif er == 20:
                Error_win = QMessageBox()
                Error_win.setText('У тебя точно нет проблем со зрением?')
                Error_win.exec()
                er += 1
            elif er == 50:
                Error_win = QMessageBox()
                Error_win.setText('Значит есть, да? Ладно, как хочешь. Я поменяю ВЕСЬ интерфейс на Шрифт Брайля. Надеюсь тебе станет легче)')
                Error_win.exec()
                main_win.setWindowTitle('⠑⠁⠎⠽⠀⠑⠙⠊⠞⠕⠗')
                button_p.setText('⠏⠁⠏⠅⠁')
                button_left.setText('⠇⠑⠺⠕')
                button_right.setText('⠏⠗⠁⠺⠕')
                button_mirror.setText('⠵⠑⠗⠅⠁⠇⠕')
                button_sharpen.setText('⠗⠑⠵⠅⠕⠎⠞⠾')
                button_bw.setText('⠟⠀⠃')
                image_label.setText('⠅⠁⠗⠞⠊⠝⠅⠁')
                #АХХАХАХАХАХ, Я ГЕНИЙ
                er += 1
                brail = 1
            elif er == 70:
                Error_win = QMessageBox()
                Error_win.setText('Че как, прикольно точки читать? Ладно ладно, может ты и в правду не замечаешь эту кнопку. Для тебя я ее выделю, а язык верну обратно. Только перестань.')
                Error_win.exec()
                main_win.setWindowTitle('Easy Editor')
                button_p.setText('ВОТ. ЭТА. КНОПКА.')
                button_left.setText('Лево')
                button_right.setText('Право')
                button_mirror.setText('Зеркало')
                button_sharpen.setText('Резкость')
                button_bw.setText('Ч/Б')
                image_label.setText('Картинка')
                er += 1
                brail = 0
            elif er == 100:
                Error_win = QMessageBox()
                Error_win.setText('Ты все еще здесь?! Кто ты такой? Проваливай отсюда, мне здесь такие не нужны.')
                Error_win.exec()
                main_win = Tk()
                main_win.destroy()
    def do_right(self):
        if List.selectedItems():
            self.image = self.image.rotate(270)
            self.saveImage()
            image_path = os.path.join(self.directory, self.savedir, self.filename)
            self.showImage(image_path)
        else:
            global er
            global brail
            global main_win, button_bw, image_label, button_left, button_right, button_mirror, button_p, button_sharpen
            if er == 0:
                Error_win = QMessageBox()
                Error_win.setText('Может для начала нужно выбрать картинку?')
                Error_win.exec()
                er = 1
            elif er == 1:
                Error_win = QMessageBox()
                Error_win.setText('Эмм, ты промахнулся, напомню, надо выбрать картинку')
                Error_win.exec()
                er = 2
            elif er == 2:
                Error_win = QMessageBox()
                Error_win.setText('Ты издеваешься? Нажми кнопку "Папка"!')
                Error_win.exec()
                er = 3
            elif er == 3:
                Error_win = QMessageBox()
                Error_win.setText('У тебя что то не так? Кнопка. "Папка". НАЖМИ. НА. НЕЕ.')
                Error_win.exec()
                er = 4
            elif er >= 4 and er != 20 and er != 50 and er != 70 and er != 100:
                if brail == 1:
                    Error_win = QMessageBox()
                    Error_win.setText('⠞⠑⠃⠑⠀⠵⠁⠝⠫⠞⠾⠎⠫⠀⠝⠑⠀⠟⠑⠍⠢')
                    Error_win.exec()
                    er += 1
                else:
                    Error_win = QMessageBox()
                    Error_win.setText('Тебе заняться не чем?')
                    Error_win.exec()
                    er += 1
            elif er == 20:
                Error_win = QMessageBox()
                Error_win.setText('У тебя точно нет проблем со зрением?')
                Error_win.exec()
                er += 1
            elif er == 50:
                Error_win = QMessageBox()
                Error_win.setText('Значит есть, да? Ладно, как хочешь. Я поменяю ВЕСЬ интерфейс на Шрифт Брайля. Надеюсь тебе станет легче)')
                Error_win.exec()
                main_win.setWindowTitle('⠑⠁⠎⠽⠀⠑⠙⠊⠞⠕⠗')
                button_p.setText('⠏⠁⠏⠅⠁')
                button_left.setText('⠇⠑⠺⠕')
                button_right.setText('⠏⠗⠁⠺⠕')
                button_mirror.setText('⠵⠑⠗⠅⠁⠇⠕')
                button_sharpen.setText('⠗⠑⠵⠅⠕⠎⠞⠾')
                button_bw.setText('⠟⠀⠃')
                image_label.setText('⠅⠁⠗⠞⠊⠝⠅⠁')
                #АХХАХАХАХАХ, Я ГЕНИЙ
                er += 1
                brail = 1
            elif er == 70:
                Error_win = QMessageBox()
                Error_win.setText('Че как, прикольно точки читать? Ладно ладно, может ты и в правду не замечаешь эту кнопку. Для тебя я ее выделю, а язык верну обратно. Только перестань.')
                Error_win.exec()
                main_win.setWindowTitle('Easy Editor')
                button_p.setText('ВОТ. ЭТА. КНОПКА.')
                button_left.setText('Лево')
                button_right.setText('Право')
                button_mirror.setText('Зеркало')
                button_sharpen.setText('Резкость')
                button_bw.setText('Ч/Б')
                image_label.setText('Картинка')
                er += 1
                brail = 0
            elif er == 100:
                Error_win = QMessageBox()
                Error_win.setText('Ты все еще здесь?! Кто ты такой? Проваливай отсюда, мне здесь такие не нужны.')
                Error_win.exec()
                main_win = Tk()
                main_win.destroy()
    def do_mirror(self):
        if List.selectedItems():
            self.image = ImageOps.mirror(self.image)
            self.saveImage()
            image_path = os.path.join(self.directory, self.savedir, self.filename)
            self.showImage(image_path)
        else:
            global er
            global brail
            global main_win, button_bw, image_label, button_left, button_right, button_mirror, button_p, button_sharpen
            if er == 0:
                Error_win = QMessageBox()
                Error_win.setText('Может для начала нужно выбрать картинку?')
                Error_win.exec()
                er = 1
            elif er == 1:
                Error_win = QMessageBox()
                Error_win.setText('Эмм, ты промахнулся, напомню, надо выбрать картинку')
                Error_win.exec()
                er = 2
            elif er == 2:
                Error_win = QMessageBox()
                Error_win.setText('Ты издеваешься? Нажми кнопку "Папка"!')
                Error_win.exec()
                er = 3
            elif er == 3:
                Error_win = QMessageBox()
                Error_win.setText('У тебя что то не так? Кнопка. "Папка". НАЖМИ. НА. НЕЕ.')
                Error_win.exec()
                er = 4
            elif er >= 4 and er != 20 and er != 50 and er != 70 and er != 100:
                if brail == 1:
                    Error_win = QMessageBox()
                    Error_win.setText('⠞⠑⠃⠑⠀⠵⠁⠝⠫⠞⠾⠎⠫⠀⠝⠑⠀⠟⠑⠍⠢')
                    Error_win.exec()
                    er += 1
                else:
                    Error_win = QMessageBox()
                    Error_win.setText('Тебе заняться не чем?')
                    Error_win.exec()
                    er += 1
            elif er == 20:
                Error_win = QMessageBox()
                Error_win.setText('У тебя точно нет проблем со зрением?')
                Error_win.exec()
                er += 1
            elif er == 50:
                Error_win = QMessageBox()
                Error_win.setText('Значит есть, да? Ладно, как хочешь. Я поменяю ВЕСЬ интерфейс на Шрифт Брайля. Надеюсь тебе станет легче)')
                Error_win.exec()
                main_win.setWindowTitle('⠑⠁⠎⠽⠀⠑⠙⠊⠞⠕⠗')
                button_p.setText('⠏⠁⠏⠅⠁')
                button_left.setText('⠇⠑⠺⠕')
                button_right.setText('⠏⠗⠁⠺⠕')
                button_mirror.setText('⠵⠑⠗⠅⠁⠇⠕')
                button_sharpen.setText('⠗⠑⠵⠅⠕⠎⠞⠾')
                button_bw.setText('⠟⠀⠃')
                image_label.setText('⠅⠁⠗⠞⠊⠝⠅⠁')
                #АХХАХАХАХАХ, Я ГЕНИЙ
                er += 1
                brail = 1
            elif er == 70:
                Error_win = QMessageBox()
                Error_win.setText('Че как, прикольно точки читать? Ладно ладно, может ты и в правду не замечаешь эту кнопку. Для тебя я ее выделю, а язык верну обратно. Только перестань.')
                Error_win.exec()
                main_win.setWindowTitle('Easy Editor')
                button_p.setText('ВОТ. ЭТА. КНОПКА.')
                button_left.setText('Лево')
                button_right.setText('Право')
                button_mirror.setText('Зеркало')
                button_sharpen.setText('Резкость')
                button_bw.setText('Ч/Б')
                image_label.setText('Картинка')
                er += 1
                brail = 0
            elif er == 100:
                Error_win = QMessageBox()
                Error_win.setText('Ты все еще здесь?! Кто ты такой? Проваливай отсюда, мне здесь такие не нужны.')
                Error_win.exec()
                main_win = Tk()
                main_win.destroy()
    def do_sharpen(self):
        if List.selectedItems():
            try:
                self.image = self.image.filter(ImageFilter.SHARPEN)
            except:
                global brail
                if brail == 1:
                    Error_win = QMessageBox()
                    Error_win.setText('⠝⠑⠁⠂⠀⠗⠑⠵⠅⠕⠎⠞⠾⠀⠙⠇⠫⠀⠉⠺⠑⠞⠝⠕⠛⠕⠀⠲⠏⠝⠛⠀⠝⠑⠀⠵⠁⠺⠑⠵⠇⠊⠂⠀⠊⠵⠺⠊⠝⠫⠯')
                    Error_win.exec()
                else:
                    Error_win = QMessageBox()
                    Error_win.setText('Неа, резкость для цветного .png не завезли, извиняй')
                    Error_win.exec()
            self.saveImage()
            image_path = os.path.join(self.directory, self.savedir, self.filename)
            self.showImage(image_path)
        else:
            global er
            global main_win, button_bw, image_label, button_left, button_right, button_mirror, button_p, button_sharpen
            if er == 0:
                Error_win = QMessageBox()
                Error_win.setText('Может для начала нужно выбрать картинку?')
                Error_win.exec()
                er = 1
            elif er == 1:
                Error_win = QMessageBox()
                Error_win.setText('Эмм, ты промахнулся, напомню, надо выбрать картинку')
                Error_win.exec()
                er = 2
            elif er == 2:
                Error_win = QMessageBox()
                Error_win.setText('Ты издеваешься? Нажми кнопку "Папка"!')
                Error_win.exec()
                er = 3
            elif er == 3:
                Error_win = QMessageBox()
                Error_win.setText('У тебя что то не так? Кнопка. "Папка". НАЖМИ. НА. НЕЕ.')
                Error_win.exec()
                er = 4
            elif er >= 4 and er != 20 and er != 50 and er != 70 and er != 100:
                if brail == 1:
                    Error_win = QMessageBox()
                    Error_win.setText('⠞⠑⠃⠑⠀⠵⠁⠝⠫⠞⠾⠎⠫⠀⠝⠑⠀⠟⠑⠍⠢')
                    Error_win.exec()
                    er += 1
                else:
                    Error_win = QMessageBox()
                    Error_win.setText('Тебе заняться не чем?')
                    Error_win.exec()
                    er += 1
            elif er == 20:
                Error_win = QMessageBox()
                Error_win.setText('У тебя точно нет проблем со зрением?')
                Error_win.exec()
                er += 1
            elif er == 50:
                Error_win = QMessageBox()
                Error_win.setText('Значит есть, да? Ладно, как хочешь. Я поменяю ВЕСЬ интерфейс на Шрифт Брайля. Надеюсь тебе станет легче)')
                Error_win.exec()
                main_win.setWindowTitle('⠑⠁⠎⠽⠀⠑⠙⠊⠞⠕⠗')
                button_p.setText('⠏⠁⠏⠅⠁')
                button_left.setText('⠇⠑⠺⠕')
                button_right.setText('⠏⠗⠁⠺⠕')
                button_mirror.setText('⠵⠑⠗⠅⠁⠇⠕')
                button_sharpen.setText('⠗⠑⠵⠅⠕⠎⠞⠾')
                button_bw.setText('⠟⠀⠃')
                image_label.setText('⠅⠁⠗⠞⠊⠝⠅⠁')
                #АХХАХАХАХАХ, Я ГЕНИЙ
                er += 1
                brail = 1
            elif er == 70:
                Error_win = QMessageBox()
                Error_win.setText('Че как, прикольно точки читать? Ладно ладно, может ты и в правду не замечаешь эту кнопку. Для тебя я ее выделю, а язык верну обратно. Только перестань.')
                Error_win.exec()
                main_win.setWindowTitle('Easy Editor')
                button_p.setText('ВОТ. ЭТА. КНОПКА.')
                button_left.setText('Лево')
                button_right.setText('Право')
                button_mirror.setText('Зеркало')
                button_sharpen.setText('Резкость')
                button_bw.setText('Ч/Б')
                image_label.setText('Картинка')
                er += 1
                brail = 0
            elif er == 100:
                Error_win = QMessageBox()
                Error_win.setText('Ты все еще здесь?! Кто ты такой? Проваливай отсюда, мне здесь такие не нужны.')
                Error_win.exec()
                main_win = Tk()
                main_win.destroy()
#    def do_blur(self):
#       self.image = self.image.filter(ImageFilter.BLUR)
#        self.saveImage()
#        image_path = os.path.join(self.directory, self.savedir, self.filename)
#        self.showImage(image_path)
#может доделаю... МОЖЕТ

workdir = ''
workImage = ImageProcessor()
def showChosenImage():
    if List.currentRow() >= 0:
        filename = List.currentItem().text()
        workImage.loadImage(filename)
        image_path = os.path.join(workImage.directory, filename)
        workImage.showImage(image_path)
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def filter(files, extensions):
    result = []
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                result.append(filename)
    return result
def showFilenamesList():
    if er == 3:
        Error_win = QMessageBox()
        Error_win.setText('Так то лучше')
        Error_win.exec()
    elif er >= 4 and er != 20 and er != 50 and er != 70 and er != 100:
        Error_win = QMessageBox()
        Error_win.setText('Верно мыслишь')
        Error_win.exec()
    try:
        chooseWorkdir()
        extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        files = os.listdir(workdir)
        files = filter(files, extensions)
        List.clear()
        List.addItems(files)
    except:
        Error_win = QMessageBox()
        Error_win.setIcon(QMessageBox.Question)
        Error_win.setText('Зачем ты тогда нажимал на выбор папки?')
        Error_win.exec()
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Easy Editor')
main_win.resize(700, 500)
button_p = QPushButton('Папка')
button_left = QPushButton('Лево')
button_right = QPushButton('Право')
button_mirror = QPushButton('Зеркало')
button_sharpen = QPushButton('Резкость')
button_bw = QPushButton('Ч/Б')
image_label = QLabel('Картинка')
List = QListWidget()
V_line1 = QVBoxLayout()
V_line2 = QVBoxLayout()
H_line1 = QHBoxLayout()
H_line2 = QHBoxLayout()
V_line1.addWidget(button_p)
V_line1.addWidget(List)
H_line1.addWidget(button_left)
H_line1.addWidget(button_right)
H_line1.addWidget(button_mirror)
H_line1.addWidget(button_sharpen)
H_line1.addWidget(button_bw)
V_line2.addWidget(image_label)
V_line2.addLayout(H_line1)
H_line2.addLayout(V_line1)
H_line2.addLayout(V_line2)
main_win.setLayout(H_line2)

button_p.clicked.connect(showFilenamesList)
List.currentRowChanged.connect(showChosenImage)
button_bw.clicked.connect(workImage.do_bw)
button_left.clicked.connect(workImage.do_left)
button_right.clicked.connect(workImage.do_right)
button_mirror.clicked.connect(workImage.do_mirror)
button_sharpen.clicked.connect(workImage.do_sharpen)
main_win.show()
app.exec_()