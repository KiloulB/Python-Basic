import time ## Importeert de tijd library
import os
os.system('cls')
os.system('color 4')

## Verstuurt een melding om data op te halen
TGREEN =  '\033[32m' # Groene tekst
TWHITE =  '\033[97m' # Witte tekst
TCYAN =  '\033[96m' # Cyan tekst
print (TGREEN)
print("""\


  _  ___       _
 | |/ / |     | |
 | ' /| | ___ | | __
 |  < | |/ _ \| |/ /
 | . \| | (_) |   <|
 |_|\_\_|\___/|_|\_|


 Bilal Kiloul


                    """)

## Standaardwaarden van de counter
counter=0

print (TWHITE)
info = str(input("We beginnen eerst met wat informatie, klik op ENTER om te beginnen."))

hours = int(input("Aantal uren: "))
print("")

minutes = int(input("Aantal minuten: "))
print("")

seconds = int(input("Aantal seconds: "))
print("")

os.system('cls')
print (TGREEN)
print("""\

  _  ___       _
 | |/ / |     | |
 | ' /| | ___ | | __
 |  < | |/ _ \| |/ /
 | . \| | (_) |   <|
 |_|\_\_|\___/|_|\_|


 Bilal Kiloul

                    """)
print (TWHITE)


## Standaardwaarden van de uren
h = hours
## Standaardwaarden van de minuten
m = minutes
## Standaardwaarden van de secondes
s = seconds

print (TCYAN)
## Maakt een loop aan met uur,minuten en secondes als variabele N
def klok(h, m, s):
    print('{:02d}:{:02d}:{:02d}'.format(h,m,s))
    # uren = str(h)
    # minuten = str(m)
    # secondes = str(s)
    # if (h < 10):
    #     uren = "0" + uren
    # if (m < 10):
    #     minuten = "0" + minuten
    # if (s < 10):
    #     secondes = "0" + secondes
    # tijdstring = uren +':' + minuten +':' + secondes
    # print(tijdstring)
#send function


while True:
    klok(hours, minutes, seconds)
## Maakt een time delay aan tussen de secondes in
    time.sleep(0.2)

## Hier voegt de counter elke keer een seconde toe
    seconds += 1

## Hier voegt de counter ook een seconde toe, zodat als de counter stopt het niet gelijk is aan <=n en dan wordt er een print gerunt
    counter+=1

## Als de variabele secondes op 60 staat, wordt er een minuut bijgevoegd en wordt secondes gereset

    for uren in range(hours,24):
        hours = 0
        for minuten in range(minutes,60):
            minutes = 0
            for secondes in range(seconds,60):
                seconds = 0
                klok(uren, minuten, secondes)



#     if seconds == 60:
#         minutes += 1
#         seconds = 0
#
# ## Als de minuten op 60 staan, wordt er een uur bijgevoegd en worden secondes en minuten gereset
#     if minutes == 60:
#         hours += 1
#         minutes = 0
#         seconds += 0
#
#     if hours == 24:
#         # break;
#         hours = 0
#         mnnutes = 0
#         seconds = 0


## link: python "D:/xampp/htdocs/EagleDev/python-basic/5-eindopdracht/opdracht.py"
