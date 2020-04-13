#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> myMainWindow.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/11 14:44
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QActionGroup, QLabel, QProgressBar, QSpinBox, QFontComboBox)
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QTextCharFormat, QFont

from ui_mainWindow import Ui_MainWindow


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__buildUI()

        # 设置斜体
        self.ui.actFont_Italic.triggered.connect(self.do_act_font_italic_triggered)
        # 设置粗体
        self.ui.actFont_Bold.triggered.connect(self.do_act_font_bold_triggered)
        # 设置下划线
        self.ui.actFont_Underline.triggered.connect(self.do_act_underline_triggered)

        # 新建文件
        self.ui.actFile_New.triggered.connect(self.do_act_file_new_triggered)
        # 打开文件
        self.ui.actFile_Open.triggered.connect(self.do_act_file_open_triggered)
        # 保存文件
        self.ui.actFile_Save.triggered.connect(self.do_act_file_save_triggered)

    def __buildUI(self):  # 窗体上动态添加组件
        # 创建状态栏上的组件
        self.__LabFile = QLabel(self)  # QLabel组件显示信息
        self.__LabFile.setMinimumWidth(150)
        self.__LabFile.setText("文件名：")
        self.ui.statusBar.addWidget(self.__LabFile)  # 添加到状态栏

        self.__progressBar1 = QProgressBar(self)
        self.__progressBar1.setMaximumWidth(200)
        self.__progressBar1.setMinimum(5)
        self.__progressBar1.setMaximum(50)
        sz = self.ui.plainTextEdit.font().pointSize()  # 字体大小
        self.__progressBar1.setValue(sz)
        self.ui.statusBar.addWidget(self.__progressBar1)  # 添加到状态栏

        self.__LabInfo = QLabel(self)  # QLabel组件显示字体名称
        self.__LabInfo.setText("选择字体名称：")
        self.ui.statusBar.addPermanentWidget(self.__LabInfo)  # 添加到状态栏

    @pyqtSlot(bool)
    def do_act_font_italic_triggered(self, checked):  # 斜体
        fmt = self.ui.plainTextEdit.currentCharFormat()
        fmt.setFontItalic(checked)
        self.ui.plainTextEdit.mergeCurrentCharFormat(fmt)

    @pyqtSlot(bool)
    def do_act_font_bold_triggered(self, checked):  # 粗体
        fmt = self.ui.plainTextEdit.currentCharFormat()
        if checked:
            fmt.setFontWeight(QFont.Bold)
        else:
            fmt.setFontWeight(QFont.Normal)
        self.ui.plainTextEdit.mergeCurrentCharFormat(fmt)

    @pyqtSlot(bool)
    def do_act_underline_triggered(self, checked):  # 下划线
        fmt = self.ui.plainTextEdit.currentCharFormat()
        fmt.setFontUnderline(checked)
        self.ui.plainTextEdit.mergeCurrentCharFormat(fmt)

    def do_act_file_new_triggered(self):  # 新建文件，不实现具体功能
        self.__LabFile.setText(" 新建文件")

    def do_act_file_open_triggered(self):  # 打开文件，不实现具体功能
        self.__LabFile.setText(" 打开的文件")

    def do_act_file_save_triggered(self):  # 保存文件，不实现具体功能
        self.__LabFile.setText(" 文件已保存")


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app，用QApplication类
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
