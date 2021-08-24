from PyQt5 import QtWidgets, uic, QtCore
import sys
from .model import Model

class WordnetUi(QtWidgets.QMainWindow):
    startID=93155
    endID=95116
    iterator = startID
    db = Model()
    def __init__(self):
        super(WordnetUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('translator.ui', self) # Load the .ui file
        self.checkedButton = self.findChild(QtWidgets.QPushButton, 'pb_checked')
        self.checkedButton.clicked.connect(self.checkedButtonPressed)
        self.persian = self.findChild(QtWidgets.QTextEdit,'te_persian')
        self.id = self.findChild(QtWidgets.QTextBrowser,'tb_id')
        self.english = self.findChild(QtWidgets.QTextBrowser,'tb_english')
        self.show() # Show the GUI

        item = self.db.select(model_name="wordnet", condition="id={}".format(self.startID))  # id:0, pos:1, gloss:2, gloss_persion:3, checked:4
        item = item[0]
        self.id.setPlainText(str(item[0]))
        self.english.setPlainText(item[2])
        self.persian.setPlainText(item[3])

    def append_text(self,text):
        self.tb.append(text)
        self.le.clear()

    def checkedButtonPressed(self):
        # This is executed when the button is pressed
        print('checkedButtonPressed')
        itemID = self.id.toPlainText()
        checkedTranslate = self.persian.toPlainText()
        self.db.update(model_name="wordnet", update_array={
            "gloss_persian": "N'{}'".format(checkedTranslate),
            "checked": "true"
        }, condition="id={}".format(itemID))
        self.iterator += 1
        if self.iterator <= self.endID:
            item = self.db.select(model_name="wordnet", condition="id={}".format(self.iterator))  # id:0, pos:1, gloss:2, gloss_persion:3, checked:4
            item = item[0]
            self.id.setPlainText(str(item[0]))
            self.english.setPlainText(item[2])
            self.persian.setPlainText(item[3])
        print(itemID) #when click login print text in username edittext


def main():  
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = WordnetUi() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()
