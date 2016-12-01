#coding=utf-8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import numpy as np
 
class Drawer(QWidget):
    GRID_SIZE = 20
    GRID_W = 20
    GRID_H = 20
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()
        self.mat = np.matrix(np.zeros((Drawer.GRID_W, Drawer.GRID_H)))
        self.mouseButton = 0
    def initUI(self):
        self.setGeometry(200, 200, Drawer.GRID_SIZE * Drawer.GRID_W + 300, Drawer.GRID_SIZE * Drawer.GRID_H)
        self.setWindowTitle('Drawer')
        self.label = QLabel(self)
        self.label.setText("Predict: ?")
        self.btnclear = QPushButton(self)
        self.btnclear.setText("clear")
        w = Drawer.GRID_SIZE * Drawer.GRID_W
        self.label.move(w + 10, 10)
        self.btnclear.move(w + 10, 50)
        self.connect(self.btnclear, SIGNAL("clicked()"), self.ClearMat)
        self.show()
    def ClearMat(self):
        self.mat = np.matrix(np.zeros((Drawer.GRID_W, Drawer.GRID_H)))
        self.update()
    def mousePressEvent(self, event):
        p = event.pos()
        self.mouseButton = event.button()
        self.drawp(p.x(), p.y())
    def mouseMoveEvent(self, event): 
        p = event.pos()
        self.drawp(p.x(), p.y())
    def mouseReleaseEvent(self, event):
        #Predict
        self.label.setText("Predict: A")
        pass
    def drawp(self, x, y):
        c = x / self.GRID_SIZE
        r = y / self.GRID_SIZE
        if 0 <= c < self.GRID_W and 0 <= r <= self.GRID_H:
            if self.mouseButton == Qt.LeftButton:
                self.mat[r, c] = 1
            else:
                self.mat[r, c] = 0
            self.update()
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
            

        for r in range(Drawer.GRID_H):
            for c in range(Drawer.GRID_W):
                x = c * Drawer.GRID_SIZE
                y = r * Drawer.GRID_SIZE
                color = Qt.white
                if self.mat[r, c] == 1:
                    color = Qt.black
                qp.setPen(QPen(color, 1, Qt.SolidLine))
                qp.setBrush(QBrush(color, Qt.SolidPattern))
                qp.drawRect(x, y, Drawer.GRID_SIZE, Drawer.GRID_SIZE)

        pen = QPen(Qt.gray, 1 , Qt.SolidLine)
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 2])
        qp.setPen(pen)
        for i in range(Drawer.GRID_W):
            qp.drawLine(i * Drawer.GRID_SIZE, 0, i * Drawer.GRID_SIZE, Drawer.GRID_H * Drawer.GRID_SIZE)
        for i in range(Drawer.GRID_H):
            qp.drawLine(0, i * Drawer.GRID_SIZE, Drawer.GRID_W * Drawer.GRID_SIZE, i * Drawer.GRID_SIZE)




        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Drawer()
    app.exec_()
    
