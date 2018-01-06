import sys,os
from PyQt4 import QtGui, QtCore
import highway_data
from result_window import run

class MainWindow(QtGui.QMainWindow):

    def __init__(self,parent=None):
        super(MainWindow,self).__init__()

        self.setWindowTitle('YourWay')
        
        #DATA----------------------------------------------------------------
        self.state = ['Ambala', 'Bhiwani', 'Charkhi Dadri', 'Faridabad', 'Fatehabad', 'Gurugram', 'Hisar', 'Jhajjar', 'Jind', 'Kaithal', 'Karnal', 'Narnaul', 'Nuh', 'Palwal', 'Panchkula', 'Panipat', 'Rewari', 'Rohtak', 'Sirsa', 'Sonipat', 'Thanesar', 'Yamuna Nagar']
        self.state_key = {'f': 'Gurugram', 'n': 'Palwal', 'i': 'Jind', 'l': 'Narnaul', 'e': 'Fatehabad', 'c': 'Charkhi Dadri', 't': 'Sonipat', 'b': 'Bhiwani', 'a': 'Ambala', 'g': 'Hisar', 'q': 'Rewari', 'o': 'Panchkula', 'v': 'Yamuna Nagar', 's': 'Sirsa', 'd': 'Faridabad', 'm': 'Nuh', 'p': 'Panipat', 'h': 'Jhajjar', 'r': 'Rohtak', 'u': 'Thanesar', 'j': 'Kaithal', 'k': 'Karnal'}
        self.path = None # Complete Route from source to destination

        # Backend Variables -------------------------------------------------
        self.sourcePath = None
        self.destinationPath = None
        self.viaTransport = None
        self.source_code = None
        self.destination_code = None

        #self.name_states = None
        #self.path_string = None

        #---------------------------------------------------------------------
        
        self.setFixedSize(1000, 600)
        self.move(200,50)

        #Initialization ---------------------------------------For User Window
        self.source_frame = QtGui.QFrame(self)
        self.destination_frame = QtGui.QFrame(self)
        self.transport_frame = QtGui.QFrame(self)
        self.letgo_frame = QtGui.QFrame(self)

        self.source_label = QtGui.QLabel(self.source_frame)
        self.destination_label = QtGui.QLabel(self.destination_frame)
        self.transport_label = QtGui.QLabel(self.transport_frame)
        self.status_label = QtGui.QLabel(self.letgo_frame)

        self.source_comboBox = QtGui.QComboBox(self.source_frame)
        self.destination_comboBox = QtGui.QComboBox(self.destination_frame)
        self.transport_comboBox = QtGui.QComboBox(self.transport_frame)
        
        self.go_button = QtGui.QPushButton(self.letgo_frame)
        
        #		Result Window ---
        self.label_path = QtGui.QLabel(self)

        #--------------------------------------------------------------------

        self.UserWindow()
        self.show()
    
    def UserWindow(self):
        self.source_frame.setGeometry(QtCore.QRect(10, 10, 980, 131))
        self.source_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.source_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.destination_frame.setGeometry(QtCore.QRect(10, 150, 980, 131))
        self.destination_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.destination_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.transport_frame.setGeometry(QtCore.QRect(10, 290, 980, 131))
        self.transport_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.transport_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.letgo_frame.setGeometry(QtCore.QRect(10, 430, 980, 118))
        self.letgo_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.letgo_frame.setFrameShadow(QtGui.QFrame.Raised)
        
        self.source_label.setText("Where you are now ?")
        self.source_label.setGeometry(QtCore.QRect(0, 0, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Kinnari")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.source_label.setFont(font)
        self.source_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.destination_label.setGeometry(QtCore.QRect(0, 0, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Kinnari")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.destination_label.setFont(font)
        self.destination_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.transport_label.setGeometry(QtCore.QRect(0, 0, 521, 61))
        font = QtGui.QFont()
        font.setFamily("Kinnari")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.transport_label.setFont(font)
        self.transport_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.status_label.setGeometry(QtCore.QRect(0, 0, 641, 61))
        font = QtGui.QFont()
        font.setFamily("Kinnari")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.status_label.setFont(font)
        self.status_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        
        self.source_comboBox.setGeometry(QtCore.QRect(750, 70, 181, 51))
        self.source_comboBox.addItem('-- Select --')
        self.source_comboBox.addItem('Ambala')
        self.source_comboBox.addItem('Bhiwani')
        self.source_comboBox.addItem('Charkhi Dadri')
        self.source_comboBox.addItem('Faridabad')
        self.source_comboBox.addItem('Fatehabad')
        self.source_comboBox.addItem('Gurugram')
        self.source_comboBox.addItem('Hisar')
        self.source_comboBox.addItem('Jhajjar')
        self.source_comboBox.addItem('Jind')
        self.source_comboBox.addItem('Kaithal')
        self.source_comboBox.addItem('Karnal')
        self.source_comboBox.addItem('Narnaul')
        self.source_comboBox.addItem('Nuh')
        self.source_comboBox.addItem('Palwal')
        self.source_comboBox.addItem('Panchkula')
        self.source_comboBox.addItem('Panipat')
        self.source_comboBox.addItem('Rewari')
        self.source_comboBox.addItem('Rohtak')
        self.source_comboBox.addItem('Sirsa')
        self.source_comboBox.addItem('Sonipat')
        self.source_comboBox.addItem('Thanesar')
        self.source_comboBox.addItem('Yamuna Nagar')

        self.source_comboBox.activated[str].connect(self.setSourcePath)

        self.destination_comboBox.setGeometry(QtCore.QRect(750, 70, 181, 51))
        self.destination_comboBox.addItem('-- Select --')
        self.destination_comboBox.addItem('Ambala')
        self.destination_comboBox.addItem('Bhiwani')
        self.destination_comboBox.addItem('Charkhi Dadri')
        self.destination_comboBox.addItem('Faridabad')
        self.destination_comboBox.addItem('Fatehabad')
        self.destination_comboBox.addItem('Gurugram')
        self.destination_comboBox.addItem('Hisar')
        self.destination_comboBox.addItem('Jhajjar')
        self.destination_comboBox.addItem('Jind')
        self.destination_comboBox.addItem('Kaithal')
        self.destination_comboBox.addItem('Karnal')
        self.destination_comboBox.addItem('Narnaul')
        self.destination_comboBox.addItem('Nuh')
        self.destination_comboBox.addItem('Palwal')
        self.destination_comboBox.addItem('Panchkula')
        self.destination_comboBox.addItem('Panipat')
        self.destination_comboBox.addItem('Rewari')
        self.destination_comboBox.addItem('Rohtak')
        self.destination_comboBox.addItem('Sirsa')
        self.destination_comboBox.addItem('Sonipat')
        self.destination_comboBox.addItem('Thanesar')
        self.destination_comboBox.addItem('Yamuna Nagar')

        self.destination_comboBox.activated[str].connect(self.setDestinationPath)

        self.transport_comboBox.setGeometry(QtCore.QRect(750, 70, 181, 51))
        self.transport_comboBox.addItem('-- Select --')
        self.transport_comboBox.addItem('Roadways')
        self.transport_comboBox.addItem('Indian Train')
        self.transport_comboBox.addItem('Highways')

        self.transport_comboBox.activated[str].connect(self.setModeOfTransport)

        self.go_button.setGeometry(QtCore.QRect(750, 60, 181, 51))

        self.source_label.setText("Where you are now ?")
        self.destination_label.setText("Where you want to go ?")
        self.transport_label.setText("How are you going to your destination ?")
        self.status_label.setText("You are ready to go from <source> to <destination>")
        self.go_button.setText("Let\'s GO")
        
        

        self.go_button.clicked.connect(self.pathFinder)

    def setSourcePath(self,text):
        self.sourcePath = str(text)
        for i in range(22):
        	if self.state[i] == self.sourcePath:
        		self.source_code = chr(i+97)
        		break

    def setDestinationPath(self,text):
        self.destinationPath = str(text)
        for i in range(22):
        	if self.state[i] == self.destinationPath:
        		self.destination_code = chr(i+97)

    def setModeOfTransport(self,text):
        self.viaTransport = str(text)

    def pathFinder(self):
        if self.source_code is not None and self.source_code != '-- Select --' and self.destination_code is not None and self.destination_code != '-- Select --' and self.viaTransport is not None and self.viaTransport != '-- Select --':
            print('Finding the path from ' + self.source_code + ' to ' + self.destination_code +' via ' + self.viaTransport)
            if self.viaTransport == 'Highways':
            	self.get_data_from_highway()
            else:
            	print 'It is under Construction...'
        else:
        	alert_msg = QtGui.QMessageBox.question(self, 'Alert !!!','I think you have selected a wrong input.\nDo you want to enter again ?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        	if alert_msg == QtGui.QMessageBox.No:
        		sys.exit()

    def get_data_from_highway(self):
    	self.path = highway_data.get_data_from_main(self.source_code,self.destination_code)
    	print(self.path)
    	self.convert_code_to_name(self.path)
    	print(self.path)
    	self.removeUserWindow()

    	state_name = self.path
    	path_string = ''

    	for name in state_name:
			path_string += name + ' -> '
    	
    	self.label_path.setText(path_string)
    	self.label_path.move(200,200)
    	self.label_path.setGeometry(QtCore.QRect(10,100,200,500))
    	self.show()
    
    def convert_code_to_name(self,codes):
    	for index in range(len(codes)):
    		codes[index] = self.state_key.get(codes[index])
    	self.path = codes
    
    def removeUserWindow(self):
    	self.source_frame.deleteLater()
    	self.destination_frame.deleteLater()
    	self.transport_frame.deleteLater()
    	self.letgo_frame.deleteLater()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app_icon = QtGui.QIcon()
    app_icon.addFile('icon.png')
    app.setWindowIcon(app_icon)
    ui = MainWindow()
    sys.exit(app.exec_())