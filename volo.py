carburante = 1460.
consumo_h = 320.

durata_volo = int (carburante/consumo_h)
resto_h= float (float(carburante % consumo_h)/float(consumo_h))
minuti_dec = float (resto_h*60)
minuti = int (minuti_dec)
diff_min = minuti_dec - minuti
secondi = int(diff_min*60)
print "la durata massima di volo e'",durata_volo,"ore",minuti,"minuti",secondi,"secondi" 
