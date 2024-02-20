# file : test42_ptpaint.py
# desc : 그림판 만들기

import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *
class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self): # 화면 초기화
        #uic.loadUi('./day07/pyPaint.ui', self) # 실행파일 생성시는 경로에 상대경로가 없어야한다.
        uic.loadUi('C:/Sources/basic-python-2024/day07/pyPaint.ui', self)
        #self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowIcon(QIcon('C:/Sources/basic-python-2024/images/iot.png'))
        self.setWindowTitle('Py그림판')
        
        # 캔버스 초기화
        self.brushColor = Qt.black
        self.canvas = QPixmap(self.lb_canvas.width(), self.lb_canvas.height())
        self.canvas.fill(QColor('white'))
        self.lb_canvas.setPixmap(self.canvas)
        #self.btn_black.setStyleSheet('background:black;') # 버튼 백그라운드 색

        self.show()
        self.setCenter()

    def initSignal(self): # 동작 초기화
        self.btn_black.clicked.connect(self.buttonClicked)
        self.btn_red.clicked.connect(self.buttonClicked)
        self.btn_blue.clicked.connect(self.buttonClicked)
        self.btn_clear.clicked.connect(self.buttonClicked)
        # 2024-02-06 이미지 로드 및 저장 버튼 추가
        self.btn_load.clicked.connect(self.buttonClicked)
        self.btn_save.clicked.connect(self.buttonClicked)

    def buttonClicked(self): # 버튼 클릭 함수
        btn_val = self.sender().objectName()

        if btn_val == 'btn_black': # 검은버튼 클릭 시
            btn_val = self.sender().objectName() # self.sender() btn_black
            self.brushColor = Qt.black
        elif btn_val == 'btn_red': # 빨간버튼 클릭 시
            btn_val = self.sender().objectName() # self.sender() btn_red
            self.brushColor = Qt.red
        elif btn_val == 'btn_blue': # 파란버튼 클릭 시
            btn_val = self.sender().objectName() # self.sender() btn_blue
            self.brushColor = Qt.blue
        elif btn_val == 'btn_clear': # 지우기버튼 클릭 시
            btn_val = self.sender().objectName()
            self.canvas.fill(QColor('white'))
            self.lb_canvas.setPixmap(self.canvas)
        elif btn_val == 'btn_load':
            image = QFileDialog.getOpenFileName(None, '이미지로드', '', 'Image file(*.jpg;*.png)')
            imagePath = image[0]
            #print(imagePath)
            pixmap = QPixmap(imagePath).scaledToHeight(381) # 파일 경로에 있는 이미지를 읽어서 pixmap객체에 담기
            self.lb_canvas.setPixmap(pixmap)
            self.lb_canvas.adjustSize() # 이미지를 라벨 크기에 맞추는 작업
        elif btn_val == 'btn_save':
            filePath, _ = QFileDialog.getSaveFileName(self, '이미지저장', '', 'Image file(*.jpg;*.png)')
            if filePath == '': return
            pixmap = self.lb_canvas.pixmap()
            pixmap.save(filePath)

        print(btn_val)

    def mouseMoveEvent(self, e) -> None:
        #print(e.x(), e.y())
        brush = QPainter(self.lb_canvas.pixmap()) # 캔버스에만 그려라
        brush.setPen(QPen(self.brushColor, 5, Qt.SolidLine, Qt.RoundCap))
        brush.drawPoint(e.x(), e.y())
        brush.end()
        self.update()

    def setCenter(self): # 화면 정중앙에 위치
        gm = self.frameGeometry() # 윈앱 자신의 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터의 정중앙 값
        gm.moveCenter(cp)
        self.move(gm.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    instance = WinApp()
    instance.show()
    sys.exit(app.exec_())
