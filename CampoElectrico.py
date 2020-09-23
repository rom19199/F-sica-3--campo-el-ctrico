#TRAYECTORIA DE UNA PARTICULA EN UN CAMPO ELECTRICO
#FISICA 3 - PROYECTO 1
#HUGO ROMAN 19199

from  __future__ import division
import numpy as np
import sys
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import pyplot as p
from matplotlib import animation
from pip._vendor.distlib.compat import raw_input


masa = 1
carga = 1
posicion = np.array([-1000, 0, -1000])
velocidad = np.array([0, 10, 0])
B = np.array([0, 0, 0.09])
E = np.array([0, 0, 0.09])
dt = 0
paso = 0.05
texto1 = 0


texto1 = int(raw_input("Ingrese el numero para elegir la carga : 1.Electron 2.Positron 3.Proton 4.Neutron 5.Particula Alfa\n6.Tauon 7.Muon 8.Neutrino electronico 9.Quark fondo 10.Quark abajo \n "))

while True:
   
    if (texto1 == 1):
        print ("***La masa del Electron es de 9.1e-31 Kg ***")
        texto = raw_input("Ingrese esa masa o la que desee (no ingrese el kg, solo el valor):\n")
        masa = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 2):
        print ("***La masa del Positron es de 9.1e-31 Kg ***")
        texto = raw_input("Ingrese esa masa o la que desee (no ingrese el C solo el valor):\n")
        masa = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 3):
        print ("***La masa del Proton es de 1.6e-27 Kg ***")
        texto = raw_input("Ingrese esa masa o la que desee:\n")
        masa = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 4):
        print ("***La masa del Neutron es de 1.6e-27 Kg ***")
        texto = raw_input("Ingrese esa masa o la que desee:\n")
        masa = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 5):
        print ("***La masa de una Particula Alfa es de 6.64e-27 Kg ***")
        texto = raw_input("Ingrese esa masa o la que desee:\n")
        masa = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 6):
        print ("***La masa de un Tauon es de 3.16e-27 Kg ***")
        texto = raw_input("Ingrese esa masa o la que desee:\n")
        masa = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 7):
        print ("***La masa de un Muon es de 1.8e-28 Kg ***")
        texto = raw_input("Ingrese esa masa o la que desee:\n")
        masa = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 8):
        print ("***La masa de un Neutrino electronico es de 4.5e-36 Kg ***")
        texto = raw_input("Ingrese esa masa o la que desee:\n")
        masa = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 9):
        print ("***La masa del Quark fondo es de 7.13e-27 Kg ***")
        texto = raw_input("Ingrese esa masa o la que desee:\n")
        masa = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 10):
        print ("***La masa del Quark abajo es de 7.13e-30 Kg ***")
        texto = raw_input("Ingrese esa masa o la que desee:\n")
        masa = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    else:
        break
                    
while True: 
    if (texto1 == 1):
        print ("***La carga del Electron es de -1.6e-19 C ***")
        texto = raw_input("ingrese esa carga o la que desee:\n")
        carga = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 2):
        print ("***La carga del Positron es de +1.6e-19 C ***")
        texto = raw_input("Ingrese esa carga o la que desee:\n")
        carga = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 3):
        print ("***La carga del Proton es de +1.6e-19 C ***")
        texto = raw_input("Ingrese esa carga o la que desee:\n")
        carga = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 4):
        print ("***La carga del Neutron es 0***")
        texto = raw_input("Ingrese esa carga o la que desee:\n")
        carga = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 5):
        print ("***La carga de una Particula Alfa es de 3.2e-19 C ***")
        texto = raw_input("Ingrese esa carga o la que desee:\n")
        carga = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 6):
        print ("***La carga de un Tauon es de -1.6e-19 C ***")
        texto = raw_input("Ingrese esa carga o la que desee:\n")
        carga = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 7):
        print ("***La carga de un Muon es de -1.6e-19 C ***")
        texto = raw_input("Ingrese esa carga o la que desee:\n")
        carga = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 8):
        print ("***La carga de un Neutrino electronico es 0 ***")
        texto = raw_input("Ingrese esa carga o la que desee:\n")
        carga = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 9):
        print ("***La carga de un Quark Fondo es -5.33e-20 ***")
        texto = raw_input("Ingrese esa carga o la que desee:\n")
        carga = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    if (texto1 == 10):
        print ("***La carga de un Quark abajo es -5.33e-20 ***")
        texto = raw_input("Ingrese esa carga o la que desee:\n")
        carga = float(texto)
        if masa == 0:
            print("entrada mala.")
        else:
            break
    else:
        break
while True:
    texto = raw_input("ingrese la posicion de la particula separado por espcios:\n")
    ind = texto.split(" ")
    if (len(ind) != 3):
        print("entrada mala.")
    else:
        posicion[0] = float(ind[0])
        posicion[1] = float(ind[1])
        posicion[2] = float(ind[2])
        break
while True:
    texto = raw_input("ingrese la velocidad inicial de la particula separado por espcios:\n")
    ind = texto.split(" ")
    if len(ind) != 3:
        print("entrada mala.")
    else:
        velocidad[0] = float(ind[0])
        velocidad[1] = float(ind[1])
        velocidad[2] = float(ind[2])
        break
while True:
    texto = raw_input("ingrese el campo electrico separado por espcios:\n")
    ind = texto.split(" ")
    if len(ind) != 3:
        print("entrada mala.")
    else:
        E[0] = float(ind[0])
        E[1] = float(ind[1])
        E[2] = float(ind[2])
        break
while True:
   ## texto = raw_input("ingrese el campo magnetico separado por espcios:\n")
    texto = ("0 0 0")
    ind = texto.split(" ")
    if len(ind) != 3:
        print("entrada mala.")
    else:
        B[0] = float(ind[0])
        B[1] = float(ind[1])
        B[2] = float(ind[2])
        break
color = "m"
if carga < 0:
    color = "b"
tamanoCaja = 1000
titulo = "Masa = " + str(masa) + "; carga = " + str(carga) + "; Vo= " + str(velocidad)
fig = p.figure()
fig.suptitle(titulo, fontsize=8, fontweight='bold')
ax = p3.Axes3D(fig)
ax.set_xlim3d({- tamanoCaja, tamanoCaja})
ax.set_ylim3d({- tamanoCaja, tamanoCaja})
ax.set_zlim3d({- tamanoCaja, tamanoCaja})
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
#fig.suptitle(ax)


contador = 0




def anima(a):
    global dt, posicion, velocidad, paso, carga, B, E, masa, color, contador
    contador += 1
    #    ax.elev = 90
    dt += paso
    t = 0.5 * carga * B * dt / masa
    t_2 = np.linalg.norm(t) * np.linalg.norm(t)
    s = 2 * t / (1 + t_2)
    v_minus = velocidad + 0.5 * carga * E * dt / masa
    v_prime = v_minus + np.cross(v_minus, t)
    v_plus = v_minus + np.cross(v_prime, s)


    velocidad = v_plus + 0.5 * carga * E * dt / masa
    posicion = posicion + velocidad * dt
    ax.scatter(posicion[0], posicion[1], posicion[2], s=1, c=color, marker="o")


    if posicion[0] < - tamanoCaja or posicion[0] > tamanoCaja:
        sys.exit()
    if posicion[1] < - tamanoCaja or posicion[1] > tamanoCaja:
        sys.exit()
    if posicion[2] < - tamanoCaja or posicion[2] > tamanoCaja:
        sys.exit()
    print(contador, posicion)


anim = animation.FuncAnimation(fig, anima, frames=10000, interval=1)

p.show()
