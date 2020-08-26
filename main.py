import math
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, \
    QGroupBox, QFormLayout, QDialogButtonBox, QDialog, QComboBox, QDesktopWidget


# Results window
# Pops up after user presses Ok after typing in their information
# noinspection PyAttributeOutsideInit,DuplicatedCode
class RWindow(QWidget):
    def __init__(self):
        super(RWindow, self).__init__()

        self.setWindowTitle("Results")
        self.resize(250, 100)
        self.show()

    # This function does all the calculations and displays them in the results window
    def calc(self, s, w, h, n, a, wst, hps, e):

        bmi = 703 * w / (h * h)

        # Calculations for females
        if s == "Female":
            bfp = 163.205 * math.log10(wst + hps - n) - 97.684 * math.log10(h) - 78.387
            idealWt = (53.1 + (1.36 * (h - 60))) * 2.204623
            bmr = 655.1 + (4.35 * w) + (4.7 * h) - (4.7 * a)
            recCal = 9.247 * w * 0.45 + 3.098 * h * 2.54 - 4.330 * a + 447.593
            recCal = recCal * e

        # Calculations for males
        if s == "Male":
            bfp = 86.010 * math.log10(wst - n) - 70.041 * math.log10(h) + 36.76
            idealWt = (56.2 + (1.41 * (h - 60))) * 2.204623
            bmr = 66.47 + (6.24 * w) + (12.7 * h) - (6.755 * a)
            recCal = 13.397 * w * 0.45 + 4.799 * h * 2.54 - 5.677 * a + 88.362
            recCal = recCal * e

        # Rounded Body Mass Index
        rBMI = round(bmi, 2)
        # Rounded Body Fat Percentage
        rBFP = round(bfp, 2)
        # Rounded Ideal Weight
        rIW = round(idealWt, 2)
        # Rounded Basic Metabolic Rate
        rBMR = round(bmr, 2)
        # Rounded Recommended Calories
        rRC = round(recCal, 2)

        vB = QVBoxLayout()
        placeHolder = QLabel("Results:")
        self.yourBMI = QLabel("Your BMI is: ")
        self.bmiLabel = QLabel(str(rBMI))
        self.yourBFP = QLabel("Your Body Fat Percentage is: ")
        self.bfpLabel = QLabel(str(rBFP))
        self.prct = QLabel("%")
        self.yourIW = QLabel("Your Ideal Weight is: ")
        self.iwLabel = QLabel(str(rIW))
        self.pnds = QLabel("lbs")
        self.yourBMR = QLabel("The number of calories you burn by being alive is: ")
        self.bmrLabel = QLabel(str(rBMR))
        self.kcals = QLabel("calories per day")
        self.recCalories = QLabel("With your activity level, you should be eating")
        self.rcLabel = QLabel(str(rRC))
        self.kcals_two = QLabel("calories per day")
        self.okBtn = QPushButton("Okay")
        self.qtBtn = QPushButton("Quit")

        hBox1 = QHBoxLayout()
        hBox2 = QHBoxLayout()
        hBox3 = QHBoxLayout()
        hBox4 = QHBoxLayout()
        hBox5 = QHBoxLayout()
        hBox6 = QHBoxLayout()
        hBox7 = QHBoxLayout()

        hBox1.addWidget(placeHolder)
        hBox2.addWidget(self.yourBMI)
        hBox2.addStretch()
        hBox2.addWidget(self.bmiLabel)
        hBox3.addWidget(self.yourBFP)
        hBox3.addWidget(self.prct)
        hBox3.addStretch()
        hBox3.addWidget(self.bfpLabel)
        hBox4.addWidget(self.yourIW)
        hBox4.addStretch()
        hBox4.addWidget(self.iwLabel)
        hBox4.addWidget(self.pnds)
        hBox5.addWidget(self.yourBMR)
        hBox3.addWidget(self.prct)
        hBox5.addStretch()
        hBox5.addWidget(self.bmrLabel)
        hBox6.addWidget(self.recCalories)
        hBox6.addWidget(self.rcLabel)
        hBox6.addWidget(self.kcals_two)
        hBox7.addWidget(self.okBtn)
        hBox7.addWidget(self.qtBtn)

        vB.addLayout(hBox1)
        vB.addLayout(hBox2)
        vB.addLayout(hBox3)
        vB.addLayout(hBox4)
        vB.addLayout(hBox5)
        vB.addLayout(hBox6)
        vB.addLayout(hBox7)

        self.setLayout(vB)

        self.okBtn.clicked.connect(self.onOk)
        self.qtBtn.clicked.connect(self.onQt)

    # Takes user back to main window
    def onOk(self):
        self.close()

    # Exits the entire program
    def onQt(self):
        QCoreApplication.quit()


# Main window/user input window
# noinspection DuplicatedCode
class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Health Calculator")
        self.resize(220, 200)
        self.formGroupBox = QGroupBox("Please Input your Data:")

        self.sex = QComboBox()
        self.sex.addItems(["Male", "Female"])
        self.age = QLineEdit()
        self.weight = QLineEdit()
        self.weight.setPlaceholderText("pounds")
        self.height = QLineEdit()
        self.height.setPlaceholderText("inches")
        self.neck = QLineEdit()
        self.neck.setToolTip("Measure your neck at its widest point")
        self.neck.setPlaceholderText("inches")
        self.waist = QLineEdit()
        self.waist.setToolTip("Measure your waist at its smallest point")
        self.waist.setPlaceholderText("inches")
        self.hip = QLineEdit()
        self.hip.setToolTip("Measure your hips at their widest point")
        self.hip.setPlaceholderText("inches")
        self.exercise = QComboBox()
        self.exercise.addItems(["Sedentary: Little to no exercise", "Light: Exercise 1 - 3 times a week",
                                "Moderate: Exercise 4 - 5 times a week", "Active: Exercise 6 - 7 times a week"])

        # Using a form layout because it is less rigid than grid, but more organized than box
        self.createForm()

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.getInfo)
        self.buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()

        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.buttonBox)

        self.setLayout(mainLayout)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def getInfo(self):
        # Translating all of the QLineEdit entries into usable values
        sx = str(self.sex.currentText())
        ag = int(self.age.text())
        wt = int(self.weight.text())
        ht = int(self.height.text())
        nk = int(self.neck.text())
        ws = int(self.waist.text())
        hp = int(self.hip.text())
        ex = str(self.exercise.currentText())

        if ex == "Sedentary: Little to no exercise":
            al = 1.2

        if ex == "Light: Exercise 1 - 3 times a week":
            al = 1.45

        if ex == "Moderate: Exercise 4 - 5 times a week":
            al = 1.7

        if ex == "Active: Exercise 6 - 7 times a week":
            al = 1.95

        # Creates an instance of the results window, and passes the user inputs through
        self.rWin = RWindow()
        self.rWin.calc(sx, wt, ht, nk, ag, ws, hp, al)

    def createForm(self):
        # creating a form layout
        layout = QFormLayout()

        layout.addRow(QLabel("Sex"), self.sex)
        layout.addRow(QLabel("Age"), self.age)
        layout.addRow(QLabel("Weight"), self.weight)
        layout.addRow(QLabel("Height"), self.height)
        layout.addRow(QLabel("Neck"), self.neck)
        layout.addRow(QLabel("Waist"), self.waist)
        layout.addRow(QLabel("Hips"), self.hip)
        layout.addRow(QLabel("Exercise"), self.exercise)

        self.formGroupBox.setLayout(layout)


if __name__ == '__main__':
    # create PyQt5 app
    app = QApplication(sys.argv)
    # create the instance of our Window
    window = Window()
    # showing the window
    window.show()
    # start the app
    sys.exit(app.exec())
