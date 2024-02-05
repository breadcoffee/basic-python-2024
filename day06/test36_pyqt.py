# file : test36_pyqt.py
# desc : PyQt5 기본화면 만들기

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget
#print(sysargv) 현재 파이썬의 경로표시

class qtwin_exam(QWidget): # QWidget을 상속받음
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        x = 1920; y = 1080; width = 400; height = 300
        self.setGeometry((x-width)//2, (y-height)//2, width, height) # x, y, width, height
        self.setWindowTitle('Qt5 Hello world!')
        self.text = ''
        self.show()

    def drawText(self, event, paint):
        paint.setPen(QColor(10, 10, 10)) # R G B
        paint.setFont(QFont('NanumGothic', 15))
        paint.drawText((400-120)//2, 300//2, 'HELL WORLD!')
        paint.drawText(event.rect(), Qt.AlignLeft, self.text) # AlignLeft 왼쪽 정렬

    def paintEvent(self, event) -> None: # 재정의(Override)
        paint = QPainter()
        paint.begin(self)
        self.drawText(event, paint)
        paint.end()


loop = QApplication(sys.argv) # 내 소스 위치로 앱을 생성
instance = qtwin_exam() # QWidget을 상속
loop.exec_()