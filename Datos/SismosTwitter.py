from logging import disable, makeLogRecord
import sys
sys.path.append('D:\\UPT\\2021-II\\Inteligencia de Negocios\\Proyecto')

from BD.sql import clsSQL
import datetime

def fechasql(cadenafecha):
    dia = int(cadenafecha[0:2])
    mes = int(cadenafecha[3:5])
    year = int(cadenafecha[6:10])
    date = datetime.datetime(year=year, month=mes, day=dia)
    return date.date()

def horasql(cadenahora):
    hora = int(cadenahora[0:2])
    minuto = int(cadenahora[3:5])
    segundo = int(cadenahora[6:8])
    time = datetime.time(hour=hora,minute=minuto,second=segundo)
    return time

sql = clsSQL()

datos = sql.sqlQuery("SELECT TweetText FROM TwitterIGP")

for dato in datos:
    texto = str(dato[0])
    if texto.__contains__("IGP/CENSIS/RS"):
        sismo = texto.split("\n")
        id = sismo[0]
        id = id[14:len(id)]

        fecha = sismo[1]
        fecha = fecha[20:30]
        fecha = fechasql(fecha)

        hora = sismo[1]
        hora = hora[31:39]
        hora = horasql(hora)

        magnitud = sismo[2]
        magnitud = float(magnitud[10:len(magnitud)])

        profundidad = sismo[3]
        profundidad = float(profundidad[13:len(profundidad)-2])

        latitud = sismo[4]
        latitud = float(latitud[9:len(latitud)])

        longitud = sismo[5]
        longitud = float(longitud[10:len(longitud)])

        referencia = sismo[6]
        referencia = referencia[12:len(referencia)]

        query = ("INSERT INTO Sismo (SismoID, Magnitud, Fecha, Hora, Latitud, Longitud, Profundidad, Referencia) VALUES ('{0}', {1}, '{2}', '{3}', {4}, {5}, {6}, '{7}');"
                .format(id, magnitud, fecha, hora, latitud, longitud, profundidad, referencia))
         
        sql.sqlInsert(query)






#print(len("IGP/CENSIS/RS "))

# IGP/CENSIS/RS 2021-0775                       (14 - 23)
# Fecha y Hora Local: 06/12/2021 01:30:50 
# Magnitud: 5.2 
# Profundidad: 40km 
# Latitud: -2.80 
# Longitud: -77.31 
# Referencia: 102 km al O de Pastaza, Alto Amazonas - Loreto

# Fecha y Hora Local: 11/02/2020,10:39:16 
# Fecha y Hora UTC: 11/02/2020,15:39:16 
# Magnitud: 3.5 
# Profundidad: 30 km 
# Latitud: -13.98 
# Longitud: -75.87 
# Intensidad: II 
# Referencia: 18 km al O de La Tinguiña, Ica - Ica 
# Mapa: https://t.co/Dc3ptbyIER

# Fecha y Hora Local: 28/01/2020 09:55:31 
# Magnitud: 3.8 
# Profundidad: 16km 
# Latitud: -15.68 
# Longitud: -71.84 
# Referencia: 9 km al SO de Maca, Caylloma - Arequipa 
# Mapa: https://t.co/WoF78fFSwM

#HL 13/04/2018 00:02:19; 
# Mag 4.2; 
# Pro 129km; 
# La -08.70; 
# Lo -74.96;
# 36 Km SE de Curimaná-Ucayali  
# https://t.co/ZNINhiF1rS

#Sismo 28/02/2018 13:36:22 HL 
# Mag4.0 ;
# Pro68 Km 
# La-11.4 
# Lo-77.8 
# 37 Km SO de Huacho-Lima  
# https://t.co/JnNwmXNeWE

# CREATE TABLE dbo.Sismo(
#   ID int PRIMARY KEY IDENTITY(1,1) NOT NULL,
#   SismoID VARCHAR(50) NULL,
#   Magnitud REAL NOT NULL,
#   Fecha DATE NOT NULL,
#   Hora TIME NOT NULL,
#   Latitud REAL NOT NULL,
#   Longitud REAL NOT NULL,
#   Profundidad REAL NOT NULL,
#   Referencia VARCHAR(100) NULL)