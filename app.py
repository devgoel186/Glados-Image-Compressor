import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 600)
        self.setObjectName("main_window")
        self.setWindowTitle("Glados Image Compressor")
        with open("stylesheet.qss") as file:
            self.setStyleSheet(file.read())

    def createBubbles(self):
        #####################
        ### SINGLE BUBBLE ###
        #####################
        self.single_bubble = QFrame(self)
        self.single_bubble.setObjectName("bubble")
        self.single_bubble.setFixedSize(300, 125)
        self.single_bubble.move(50, 100)
        self.single_bubble.mousePressEvent = self.singleBubbleClicked

        # Single Bubble Heading
        self.single_bubble_heading = QLabel(self.single_bubble)
        self.single_bubble_heading.setObjectName("bubble_heading")
        self.single_bubble_heading.setText("Compress Image")
        self.single_bubble_heading.move(100, 8)

        # Single Bubble Paragraph
        self.single_bubble_para = QLabel(self.single_bubble)
        self.single_bubble_para.setObjectName("bubble_para")
        self.single_bubble_para.setText(
            "Click this button to compress a single image")
        self.single_bubble_para.move(25, 32)

        ##################
        ### DIR BUBBLE ###
        ##################
        self.dir_bubble = QFrame(self)
        self.dir_bubble.setObjectName("bubble")
        self.dir_bubble.setFixedSize(300, 125)
        self.dir_bubble.move(50, 275)
        self.dir_bubble.mousePressEvent = self.dirBubbleClicked

        # Dir Bubble Heading
        self.dir_bubble_heading = QLabel(self.dir_bubble)
        self.dir_bubble_heading.setObjectName("bubble_heading")
        self.dir_bubble_heading.setText("Compress Multiple Images")
        self.dir_bubble_heading.move(70, 8)

        # Dir Bubble Paragraph
        self.dir_bubble_para = QLabel(self.dir_bubble)
        self.dir_bubble_para.setObjectName("bubble_para")
        self.dir_bubble_para.setText(
            "Click here to compress multiple images at once")
        self.dir_bubble_para.setWordWrap(True)
        self.dir_bubble_para.move(25, 32)

        ##############################
        ### SINGLE BUBBLE EXPANDED ###
        ##############################
        self.single_bubble_expanded = QFrame(self)
        self.single_bubble_expanded.setObjectName("bubble_expanded")
        self.single_bubble_expanded.setFixedSize(300, 350)
        self.single_bubble_expanded.move(50, 100)
        self.single_bubble_expanded.setVisible(False)

        # Back Arrow
        self.back_arrow_single = QLabel(self.single_bubble_expanded)
        self.back_arrow_single.setObjectName("back_arrow")
        self.back_arrow_single.move(30, 5)
        self.back_arrow_single.setTextFormat(Qt.RichText)
        self.back_arrow_single.setText("&#8592;")
        self.back_arrow_single.mousePressEvent = self.backArrowClicked

        # Single Bubble Heading
        self.single_bubble_heading = QLabel(self.single_bubble_expanded)
        self.single_bubble_heading.setObjectName("bubble_heading")
        self.single_bubble_heading.setText("Compress Image")
        self.single_bubble_heading.move(100, 8)

        # Select Image Heading
        self.select_image = QLabel(self.single_bubble_expanded)
        self.select_image.setObjectName("bubble_para")
        self.select_image.setText("Choose Image")
        self.select_image.move(30, 50)

        # Select Image Path
        self.select_image_path = QLineEdit(self.single_bubble_expanded)
        self.select_image_path.setObjectName("select_path")
        self.select_image_path.move(60, 85)

        # Select Image Button (Browse)
        self.browse_button = QPushButton(self.single_bubble_expanded)
        self.browse_button.setObjectName("browse_button")
        self.browse_button.setFixedSize(30, 25)
        self.browse_button.setText("...")
        self.browse_button.move(210, 84)
        self.browse_button.clicked.connect(self.openFileNameDialog)

        # Select Image Quality Heading
        self.select_quality = QLabel(self.single_bubble_expanded)
        self.select_quality.setObjectName("bubble_para")
        self.select_quality.setText("Choose Quality")
        self.select_quality.move(30, 130)

        # Select Image Quality
        self.select_quality_choice = QLineEdit(self.single_bubble_expanded)
        self.select_quality_choice.setObjectName("select_quality")
        self.select_quality_choice.setMaximumWidth(100)
        self.select_quality_choice.move(60, 165)

        # Select Image Quality (Choice)
        self.select_quality_box = QComboBox(self.single_bubble_expanded)
        self.select_quality_box.addItem("High")
        self.select_quality_box.addItem("Medium")
        self.select_quality_box.addItem("Low")
        self.select_quality_box.setObjectName("select_quality_box")
        self.select_quality_box.move(170, 165)

        # Compress Image Button
        self.compress_button = QPushButton(self.single_bubble_expanded)
        self.compress_button.setObjectName("compress_button")
        self.compress_button.setText("Compress")
        self.compress_button.move(110, 260)

        ###########################
        ### DIR BUBBLE EXPANDED ###
        ###########################
        self.dir_bubble_expanded = QFrame(self)
        self.dir_bubble_expanded.setObjectName("bubble_expanded")
        self.dir_bubble_expanded.setFixedSize(300, 350)
        self.dir_bubble_expanded.move(50, 100)
        self.dir_bubble_expanded.setVisible(False)

        # Back Arrow
        self.back_arrow_dir = QLabel(self.dir_bubble_expanded)
        self.back_arrow_dir.setObjectName("back_arrow")
        self.back_arrow_dir.move(30, 5)
        self.back_arrow_dir.setTextFormat(Qt.RichText)
        self.back_arrow_dir.setText("&#8592;")
        self.back_arrow_dir.mousePressEvent = self.backArrowClicked

        # Dir Bubble Heading
        self.dir_bubble_heading = QLabel(self.dir_bubble_expanded)
        self.dir_bubble_heading.setObjectName("bubble_heading")
        self.dir_bubble_heading.setText("Compress Multiple Images")
        self.dir_bubble_heading.move(70, 8)

        # Select Source Directory Heading
        self.select_image = QLabel(self.dir_bubble_expanded)
        self.select_image.setObjectName("bubble_para")
        self.select_image.setText("Choose Source Directory")
        self.select_image.move(30, 50)

        # Select Source Path
        self.select_source_path = QLineEdit(self.dir_bubble_expanded)
        self.select_source_path.setObjectName("select_path")
        self.select_source_path.move(60, 85)

        # Select Source Button (Browse)
        self.source_browse_button = QPushButton(self.dir_bubble_expanded)
        self.source_browse_button.setObjectName("browse_button")
        self.source_browse_button.setFixedSize(30, 25)
        self.source_browse_button.setText("...")
        self.source_browse_button.move(210, 84)
        self.source_browse_button.clicked.connect(
            self.openFileNamesDialogSource)

        # Select Destination Directory Heading
        self.select_image = QLabel(self.dir_bubble_expanded)
        self.select_image.setObjectName("bubble_para")
        self.select_image.setText("Choose Destination Directory")
        self.select_image.move(30, 130)

        # Select Destination Path
        self.select_destination_path = QLineEdit(self.dir_bubble_expanded)
        self.select_destination_path.setObjectName("select_path")
        self.select_destination_path.move(60, 165)

        # Select Destination Button (Browse)
        self.destination_browse_button = QPushButton(self.dir_bubble_expanded)
        self.destination_browse_button.setObjectName("browse_button")
        self.destination_browse_button.setFixedSize(30, 25)
        self.destination_browse_button.setText("...")
        self.destination_browse_button.move(210, 164)
        self.destination_browse_button.clicked.connect(
            self.openFileNamesDialogDestination)

        # Select Image Quality Heading
        self.select_quality = QLabel(self.dir_bubble_expanded)
        self.select_quality.setObjectName("bubble_para")
        self.select_quality.setText("Choose Quality")
        self.select_quality.move(30, 210)

        # Select Image Quality
        self.select_quality_choice = QLineEdit(self.dir_bubble_expanded)
        self.select_quality_choice.setObjectName("select_quality")
        self.select_quality_choice.setMaximumWidth(100)
        self.select_quality_choice.move(60, 245)

        # Select Image Quality (Choice)
        self.select_quality_box = QComboBox(self.dir_bubble_expanded)
        self.select_quality_box.addItem("High")
        self.select_quality_box.addItem("Medium")
        self.select_quality_box.addItem("Low")
        self.select_quality_box.setObjectName("select_quality_box")
        self.select_quality_box.move(170, 245)

        # Compress Image Button
        self.compress_button = QPushButton(self.dir_bubble_expanded)
        self.compress_button.setObjectName("compress_button")
        self.compress_button.setText("Compress")
        self.compress_button.move(110, 290)

    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Select File", "", "All Files (*);;Image Files (*.jpg *.jpeg *.png)")
        if fileName:
            print(fileName, _)
            self.select_image_path.setText(fileName)

    def openFileNamesDialog(self):
        folderName = QFileDialog.getExistingDirectory(
            self, "Select Directory")
        if folderName:
            return folderName
        return ""

    def openFileNamesDialogSource(self):
        folderName = self.openFileNamesDialog()
        self.select_source_path.setText(folderName)

    def openFileNamesDialogDestination(self):
        folderName = self.openFileNamesDialog()
        print(folderName)
        self.select_destination_path.setText(folderName)

    def backArrowClicked(self, event):
        self.single_bubble_expanded.setVisible(False)
        self.dir_bubble_expanded.setVisible(False)
        self.single_bubble.setVisible(True)
        self.dir_bubble.setVisible(True)

    def singleBubbleClicked(self, event):
        self.single_bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        self.single_bubble_expanded.setVisible(True)

    def dirBubbleClicked(self, event):
        self.single_bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        self.dir_bubble_expanded.setVisible(True)


def creationGod(ex):
    ex.createBubbles()
    ex.show()  # Show the window


def main():
    app = QApplication(sys.argv)
    ex = window()
    creationGod(ex)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
