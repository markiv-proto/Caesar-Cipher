import pytest
from PySide6.QtCore import Qt
from caesar.gui import CaesarGUI

@pytest.fixture
def app(qtbot):
    test_app = CaesarGUI()
    qtbot.addWidget(test_app)
    return test_app

def test_encrypt_button(app, qtbot):
    app.input_text.setPlainText("Hello")
    app.shift_input.setText("3")
    qtbot.mouseClick(app.encrypt_btn, Qt.LeftButton)
    assert app.output_text.toPlainText() == "Khoor"

def test_decrypt_button(app, qtbot):
    app.input_text.setPlainText("Khoor")
    app.shift_input.setText("3")
    qtbot.mouseClick(app.decrypt_btn, Qt.LeftButton)
    assert app.output_text.toPlainText() == "Hello"

def test_bruteforce_button(app, qtbot):
    app.input_text.setPlainText("Khoor")
    qtbot.mouseClick(app.bruteforce_btn, Qt.LeftButton)
    output = app.output_text.toPlainText()
    assert "Shift 3" in output
    assert "Hello" in output

def test_invalid_shift_defaults_to_3(app, qtbot):
    app.input_text.setPlainText("Hello")
    app.shift_input.setText("abc")  # invalid input
    qtbot.mouseClick(app.encrypt_btn, Qt.LeftButton)
    assert app.output_text.toPlainText() == "Khoor"
