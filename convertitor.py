#!/usr/bin/python -tt

import sys

def converti(filename_input, filename_output):
	file_input = open(filename_input, 'r')
	file_out   = open(filename_output, 'w')
	file_out.write("DATA INIZIO;DATA FINE;DESCRIZIONE;NOME\n")
	for line in file_input: 	
		word  = line.split(':')[0]
		if word == 'DTSTART':
			word2 = line.split(':')[1]
			word2 = word2.split('\n')[0]
			anno = getAnno(word2)
			mese = getMese(word2)
			giorno = getGiorno(word2)
			ora = getOra(word2)
			minuti = getMinuti(word2)
			secondi = getSecondi(word2)
			if is_DST:
				ora2 = ora[0] + str(int(ora[1])+2)
				ora = ora2
			else:
				ora2 = ora[0] + ora[1]+'1' 
				ora = ora2
			file_out.write(anno+'-'+mese+'-'+giorno+' '+ora+':'+minuti+':'+secondi+';')
		if word == 'DTEND':
			word2 = line.split(':')[1]
			word2 = word2.split('\n')[0]
			anno = getAnno(word2)
			mese = getMese(word2)
			giorno = getGiorno(word2)
			ora = getOra(word2)
			minuti = getMinuti(word2)
			secondi = getSecondi(word2)
			if is_DST:
				ora2 = ora[0] + str(int(ora[1])+2) 
				ora = ora2
			else:
				ora2 = ora[0] + ora[1]+'1' 
				ora = ora2
			file_out.write(anno+'-'+mese+'-'+giorno+' '+ora+':'+minuti+':'+secondi+';')
		if word == 'SUMMARY':
			word2 = line.split(':')[1]
			word2 = word2.split('\n')[0]
			file_out.write(word2 + '\n')
		if word == 'DESCRIPTION':
			word2 = line.split(':')[1]
			word2 = word2.split('\n')[0]
			file_out.write(word2 + ';')
	file_input.close()
	file_out.close()

def getAnno(stringa):
	anno = ''
	for i in range(4):
		anno += stringa[i]
	return anno

def getMese(stringa):
	mese = ''
	for i in range(4,6):
		mese += stringa[i]
	return mese

def getGiorno(stringa):
	giorno = ''
	for i in range(6,8):
		giorno += stringa[i]
	return giorno

def getOra(stringa):
	ora = ''
	for i in range(9,11):
		ora += stringa[i]
	return ora

def getMinuti(stringa):
	minuti = ''
	for i in range(11,13):
		minuti += stringa[i]
	return minuti

def getSecondi(stringa):
	secondi = ''
	for i in range(13,15):
		secondi += stringa[i]
	return secondi


def is_DST(anno, mese, giorno):
	return bool(pytz.timezone('Europe/Amsterdam').dst(datetime(anno, mese, giorno), is_dst=None))

def main():

	if len(sys.argv) != 3:
		print "Non sono stati dichiarati tutti i dati di input: Nome File ICS, Nome File di uscita CSV"
		sys.exit(1)

	filename_input  = sys.argv[1]
	filename_output = sys.argv[2]
	converti(filename_input, filename_output)
	print 'Conversione Completata'

if __name__ == "__main__":
	main()