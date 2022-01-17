#!usr/bin/python3

import crypt
print("\t"*4,"#### By: Abd Almoen Arafa (0.1Arafa) ####"),print("\t"*4,"#### Age: 15			      ####\n")
def main():
	text=input("[*] Enter the salted text: ")
	file=input("[*] Enter The File: ")
	if not text or not file :	main()
	else:
		File=open(file,"r")
		for Line in File:
			line=crypt.crypt(Line.strip(),text[0:2])
			print("[!!] Trying:",Line.strip("\n"))
			if line == text:	print("[+] Password Found!!:",Line.strip(),":",line,"\n"),quit()
			else:	pass
main()
