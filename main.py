# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 NormDist.com
#
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation; either version 2.1 of the License,
# or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301


import os
import sys

from PySide2.QtCore import Qt, QUrl
from PySide2.QtGui import QIcon
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu, QAction, QStyle


class CustomWebEngineView(QWebEngineView):
    def contextMenuEvent(self, event):
        # 直接重写并跳过默认的上下文菜单处理
        pass

class WebWindow(QMainWindow):
    def __init__(self, url):
        super().__init__()

        self.setWindowTitle("DeepSeek - 探索未至之境")
        self.setGeometry(0, 0, 960, 654)

        # 添加 Favicon
        file_path = os.path.dirname(__file__)
        icon_path = os.path.join(file_path,"app","assets", "favicon.ico")
        self.setWindowIcon(QIcon(icon_path))

        # 创建浏览器组件
        # self.browser = QWebEngineView()        
        self.browser = CustomWebEngineView()
        self.browser.load(QUrl(url))

        # 布局设置
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.setContentsMargins(0, 0, 0, 0)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.startup_center()

    def closeEvent(self, event):
        """ 重写关闭事件 """
        event.ignore()  # 忽略默认关闭行为
        self.hide()     # 隐藏窗口而不是关闭

    def startup_center(self):
        frame_geometry = self.frameGeometry()
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        center_point = screen_geometry.center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())



class TrayIcon(QSystemTrayIcon):
    def __init__(self, window, icon_path):
        super().__init__()
        self.window = window

        # 创建系统托盘图标
        self.setIcon(QIcon(icon_path))
        self.setToolTip("DeepSeek")

        # 创建右键菜单
        self.menu = QMenu()
        self._create_actions()
        self.setContextMenu(self.menu)

        # 绑定事件
        self.activated.connect(self._toggle_window)

        self.show()

    def _create_actions(self):

        style = QApplication.style()
        show_action = QAction(style.standardIcon(QStyle.SP_DesktopIcon), "显示", self)
        exit_action = QAction("退出", self)

        show_action.triggered.connect(self.window.show())
        exit_action.triggered.connect(QApplication.instance().quit)

        self.menu.addAction(show_action)
        self.menu.addAction(exit_action)


    def _toggle_window(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self.window.isHidden() or self.window.isMinimized():
                # 如果窗口被隐藏、最小化，则显示窗口并设置窗口状态为正常
                self.window.showNormal()
                self.window.raise_()

            self.window.activateWindow()


def main():

    # 启用高DPI缩放
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    # 创建应用程序实例和窗口
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    url = "https://chat.deepseek.com/"
    window = WebWindow(url)
    icon_path = os.path.join(os.path.dirname(__file__), "app", "assets", "favicon.ico")
    tray = TrayIcon(window, icon_path)
    window.show()

    sys.exit(app.exec_())


# 运行主函数
if __name__ == "__main__":
    main()