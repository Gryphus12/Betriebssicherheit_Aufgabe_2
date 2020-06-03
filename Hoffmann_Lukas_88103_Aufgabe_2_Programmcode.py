# LOPA
# Die Instanzen der Klassen sollen mit doppelt verketteten Listen verbunden werden
from graphviz import *


class EVENT:
    def __init__(self, name, impact, freq):
        self.next = None                    # Das Attribut der Klasse self.next verkettet die folgende USE Instanz mit der EVENT Instanz
        self.pre = None                     # Das Attribut der Klasse self.pre verkettet das davorliegende USE mit dem EVENT.
        self.freq = freq
    
    def setSuccessor(self, node):


    def draw(self, img, start):             # Die draw Methode wird vom Initialereignis aus aufgerufen (f0 in Bild 1). Die Methode gibt dann
                                            # ein Pfeil mit entsprechender Breite und Länge aus. Danach wird rekursiv die draw Methode des
                                            # folgenden USE aufgerufen, welcher ein Rechteck zeichnet. Dies wird wiederholt, bis alle EVENT
                                            # und USE der Kette gezeichnet wurden.


    
    def frequency(self):                    # Mit der Methode frequency kann die Häufigkeit eines
                                            # Ereignisses ermittelt werden, indem die Methode bei der letzten USE Instanz (USE5 in Bild 1) der
                                            # Kette aufgerufen wird. Diese wieder ruft rekursiv die Methode frequency der davorliegenden Instanz (EVENT) auf und multipliziert die Ausfallwahrscheinlichkeit des USE mit der Häufigkeit des
                                            # EVENT. Dies wird wiederholt, bis alle frequency Methoden der Kette aufgerufen wurde. Danach
                                            # wird das Ergebnis ausgegeben


class USE:
    def __init__(self, )