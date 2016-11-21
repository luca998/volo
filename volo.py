carburante = 1460
consumo_h = 320

durata_volo = carburante/consumo_h
min = float (float(carburante % consumo_h)/float(consumo_h))
minuti1 = float (min*60)
minuti = int (minuti1)
sec = minuti1 - minuti
secondi = int(sec*60)
print "la durata massima di volo e'",durata_volo,"ore",minuti,"minuti",secondi,"secondi"  
