# -*- coding: utf-8 -*-
"""
necesita las siguientes librerias para funcionar:

pyserial
    pip install pyserial
    
pymsqgbox
    pip install PyMsgBox

"""

"#LIBRERIAS UTILIZADAS"
import serial
import pymsgbox

"#CONSTANTES UTILIZADAS"
botonON = 16753245
boton0 = 16738455
boton1= 16724175
boton2=16718055
boton3=16743045
boton4=16716015
boton5=16726215
boton6=16734885
boton7=16728765
boton8=16730805
boton9=16732845
boton_mas_100=16750695
boton_mas_200=16756815
boton_menos=16769055
boton_mas=16754775
boton_eq=16748655
boton_play=16761405



def conexion_arduino():
    try:
        terminal=""
        arduino = serial.Serial('COM3', 9600)
        pymsgbox.alert('Inicio Correcto ...',timeout=3000)
        while True:
            rawString = int(arduino.readline())
            if rawString==botonON:
                arduino.close()
                pymsgbox.alert('------ADIOS-----',timeout=2000)
                break
            elif rawString==boton0:
                terminal=terminal+"0"
            elif rawString==boton1:
                terminal=terminal+"1"
            elif rawString==boton2:
                terminal=terminal+"2"   
            elif rawString==boton3:
                terminal=terminal+"3" 
            elif rawString==boton4:
                terminal=terminal+"4"
            elif rawString==boton5:
                terminal=terminal+"5"  
            elif rawString==boton6:
                terminal=terminal+"6"
            elif rawString==boton7:
                terminal=terminal+"7"
            elif rawString==boton8:
                terminal=terminal+"8"
            elif rawString==boton9:
                terminal=terminal+"9"
            elif rawString==boton_mas_100:
                terminal=terminal+"+100"               
            elif rawString==boton_mas_200:
                terminal=terminal+"+200"  
            elif rawString==boton_mas:
                terminal=terminal+"+"           
            elif rawString==boton_menos:
                terminal=terminal+"-"       
            elif rawString==boton_play:
                if terminal!="":
                    pymsgbox.alert('Input:  '+terminal,timeout=2000)
                    try:
                        pymsgbox.alert('Resultado:  '+str(eval(terminal)),timeout=2000)
                    except:
                        pymsgbox.alert('NO ES POSIBLE CALCULAR '+terminal,timeout=2000)
                else:
                    pymsgbox.alert('Memoria Vacia',timeout=2000)
            elif rawString==boton_eq:
                pymsgbox.alert('Memoria Limpiada Correctamente',timeout=2000)
                terminal=""
            else:
                if rawString!=4294967295:
                    pymsgbox.alert('Boton Invalido',timeout=1000)
    except:
        pymsgbox.alert('El Puerto COM3 no se puede abrir',timeout=2000)
                
conexion_arduino()







            
        
        