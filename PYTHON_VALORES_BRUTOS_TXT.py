#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import glob
import serial
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
import numpy as np
from collections import deque
from threading import Thread
from itertools import islice  # Adicionando importação do islice
from PyQt5 import QtWidgets

#Lê as portas seriais disponíveis
if sys.platform.startswith('win'): #Windows
    portas = ['COM%s' % (i + 1) for i in range(256)]
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'): #Linux
    portas = glob.glob('/dev/tty[A-Za-z]*')
elif sys.platform.startswith('darwin'):
    portas = glob.glob('/dev/tty.*')
else:
    raise EnvironmentError('Plataforma não suportada')

resultado = []
for porta in portas:
    try:
        s = serial.Serial(porta)
        s.close()
        resultado.append(porta)
    except (OSError, serial.SerialException):
        pass
print(resultado)

#usb = input('Escolha a porta serial: ')
usb = "COM3"
arduinoData = serial.Serial(usb, 115200)


freq = 2000              # 1/T
amostras = 2048             # 500
frequencia = np.linspace(0.0, 1.0/(2.0*1/freq), freq//2)

acelx = deque([], maxlen=amostras)

win = pg.GraphicsWindow()

win.setWindowTitle('FFT')#Título do programa
pg.setConfigOption('foreground', 'w') #branco = w
pg.setConfigOption('background', 'w')

#editar cor e texto do gráfico 1
p1 = win.addPlot(
    title="<span style='color: #ffffff; font-weight: bold; font-size:20px'>MPU6050</span>")
linha1 = pg.mkPen((0, 255, 0), width=2) 
p1.addLegend(offset=(10, 5))

curva1 = p1.plot(acelx,
                 pen=linha1,
                 name="<span style='color: #ffffff; font-weight: bold; font-size: 12px'>X</span>")

#Intervalo do gráfico 1
p1.setRange(yRange=[-30000, 30000], xRange=[0, 500])
p1.setLabel('bottom',
            text="<span style='color: #ffffff; font-weight: bold; font-size: 12px'>Tempo</span>")
p1.showGrid(x=True, y=False)

win.nextRow()
p2 = win.addPlot()
linha4 = pg.mkPen((255, 0, 0), width=2)
p2.addLegend(offset=(10, 5))

curva2 = p2.plot(frequencia,
                 pen=linha4,
                 name="<span style='color: #ffffff; font-weight: bold; font-size: 12px'>Amplitude</span>")

#Intervalo do gráfico 2
p2.setRange(xRange=[0, int(freq/2)])
p2.setRange(yRange=[0, 10000], xRange=[0, 500])
#editar cor e texto do gráfico 2
p2.setLabel('bottom',
            text="<span style='color: #ffffff; font-weight: bold; font-size: 12px'>Frequência (Hz)</span>")
p2.showGrid(x=False, y=True)
ax = p2.getAxis('bottom')
ax.setTicks([[(v, str(v)) for v in np.arange(0, int(freq/2)+1, 100)]])

dados = []

# Ler dados do sensor
def entrada_dados():
    global dados
    for linha in arduinoData:
        try:
            valor = float(linha)
            acelx.append(valor)
            if len(acelx) == amostras:
                dados = np.fft.fft(acelx)
                escrever_arquivo_txt(acelx)
                break
        except ValueError:
            pass

# Escrever os valores brutos em um arquivo txt
def escrever_arquivo_txt(valores):
    with open('valores_brutos.txt', 'w') as arquivo:
        arquivo.write(','.join(map(str, valores)))

# inicie o thread de entrada de dados. Isso será executado em segundo plano, não sendo afetado pela GUI.
t = Thread(target=entrada_dados)
t.daemon = True
t.start()

#Atualizar os dados do gráfico
def atualizar():
    curva1.setData(deque(islice(acelx, 0, 500), maxlen=500))
    if len(acelx) == amostras:
        curva2.setData((2/amostras * np.abs(dados[1:int(amostras/2)])))

#A cada 100 milissegundos o gráfico é atualizado
cronômetro = pg.QtCore.QTimer()
cronômetro.timeout.connect(atualizar)
cronômetro.start(100)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()


