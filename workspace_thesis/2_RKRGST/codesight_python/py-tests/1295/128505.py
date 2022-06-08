"""problema de cifrado"""
import sys
dic = "abcdefghijklmnopqrstuvwxyz"
if __name__ == "__main__":
	for cod in sys.stdin:
		n = int(input())
		#frases = []
		for i in range(0, n):
			trad = ""
			cad = input()
			for letra in cad:
				if letra != " ":
					trad += dic[cod.index(letra)]
				else:
					trad += " "
			print(trad)
		print("") 

