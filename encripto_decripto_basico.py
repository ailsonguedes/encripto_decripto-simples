from PyQt5 import uic,QtWidgets

def crip(): # função criptografar
    
    line_text = crip_screen.lineEdit_1.text() # linha do texto a ser criptografado
    line_crip = crip_screen.lineEdit_2.text() # recebe o texto já encriptado
    
    encript = ''

    for i in line_text:
        encript = encript + chr (ord(i)+5)

    crip_screen.lineEdit_1.setText("") # limpa a caixa que recebe o texto a ser criptografado
    crip_screen.lineEdit_2.setText(encript) # mostra o texto encriptado na caixa 2

def decrip(): # função decriptografar
    
    line_crip = crip_screen.lineEdit_3.text() # linha do texto a ser decriptografado
    line_text = crip_screen.lineEdit_4.text() # recebe o texto decriptografado

    decript = ''

    for i in line_crip:
        decript = decript + chr (ord(i)-5)

    crip_screen.lineEdit_3.setText("")
    crip_screen.lineEdit_4.setText(decript) # mosta o texto decriptado
# screen
app=QtWidgets.QApplication([])
crip_screen=uic.loadUi("criptotela.ui")
# buttons
crip_screen.pushButton_1.clicked.connect(crip)
crip_screen.pushButton_2.clicked.connect(decrip)
# show screen
crip_screen.show()
app.exec()