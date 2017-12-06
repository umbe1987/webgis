from PyQt5 import QtCore, QtWidgets
from ui.mainwindow import MainWindow

if __name__ == "__main__":
    import sys
    
    # prevent "QOpenGLShaderProgram shader program is not linked" error on Linux systems
    # https://forum.qt.io/topic/81328/ubuntu-qopenglshaderprogram-shader-program-is-not-linked/2
    if sys.platform.startswith( 'linux' ) :
        from OpenGL import GL
        
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    
