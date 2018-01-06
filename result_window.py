import sys
from PyQt4 import QtGui, QtCore

class ResultWindow(QtGui.QWidget):
	def __init__(self,path,parent=None):
		super(ResultWindow,self).__init__()

		self.setFixedSize(1000,600)
		self.move(200,50)
		self.names_of_state = path
		self.print_info()

		self.label = QtGui.QLabel(self)
		

		self.home(self.names_of_state)

	def home(self,state_name):
		path_string = ''

		for name in state_name:
			path_string += name + ' -> '

		self.label.setText(path_string)
		self.show()


	def print_info(self):
		print(self.names_of_state)


def run(path):
	r_win = QtGui.QApplication(sys.argv)
	r_win_icon = QtGui.QIcon()
	r_win_icon.addFile('icon.png')
	r_win.setWindowIcon(r_win_icon)
	ui = ResultWindow(path)
	sys.exit(r_win.exec_())

#run(['ambala','bhiwani','faridabad','hisar'])