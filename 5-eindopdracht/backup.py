import time ## Importeert de tijd library, zie lijn 13
# import os

## Standaardwaarden van de counter
counter=0
## Standaardwaarden van de secondes
s = 0
## Standaardwaarden van de minuten
m = 0
## Standaardwaarden van de uren
h = 0

## Verstuurt een melding met hoeveel secondes je wilt
n = int(input("Aantal uren: "))
print("")

## Maakt een loop aan met uur,minuten en secondes als variabele N
while counter <= n:
    uren = str(h)
    minuten = str(m)
    secondes = str(s)

    if (h < 10):
        uren = '0' + uren

    if (m < 10):
        minuten = '0' + minuten

    if (s < 10):
        secondes = '0' + secondes

    tijdstring = uren +':' + minuten +':' + secondes
    print(tijdstring)
## Maakt een time delay aan tussen de secondes in
    time.sleep(0.1)

## Hier voegt de counter elke keer een seconde toe
    s += 1

## Hier voegt de counter ook een seconde toe, zodat als de counter stopt het niet gelijk is aan <=n en dan wordt er een print gerunt
    counter+=1

## Als de variabele secondes op 60 staat, wordt er een minuut bijgevoegd en wordt secondes gereset
    if s == 60:
        m += 1
        s = 0

## Als de minuten op 60 staan, wordt er een uur bijgevoegd en worden secondes en minuten gereset
    if m == 60:
        h += 1
        m = 0
        s += 0

print("\nTijd is op!\n")

## link: python "D:/xampp/htdocs/EagleDev/python-basic/5-eindopdracht/opdracht.py"
