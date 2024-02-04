import math

def crivo(n):
	p = [True] * (n + 1)
	p[1] = False
	p[0] = False
	for i in range(2, int(math.sqrt(n) + 1)):
		if p[i]:
			j = 2 * i
			while(j <= n):
				p[j] = False
				j = j + i
	return p
				
def dec_minima_prima(n, to_print=False):
	l = int(math.floor(n / 2.0))
	r = n - l
	if to_print:
		print(f"^{n} = l: {l} r: {r}")
	if l == r:
		return False
	if l % 3 == 0 or r % 3 == 0:
		return True
	return False
	
N_MAX = 1000000	
primo = crivo(N_MAX)
verdadeiro = True
print("Primos:")
for n in range(1, N_MAX):
	if(n > 3 and primo[n] == True and dec_minima_prima(n, True) == False):
		print (f"Falhou para {n}")
		verdadeiro = False
		break
		
print("Não primos:")
for n in range(3, N_MAX, 2):
	if primo[n] == False and dec_minima_prima(n) == True:
		#print (f"Falhou para {n}")
		verdadeiro = False
		break
		
if verdadeiro == True:
	print(f"Verdadeiro")
else:
	print(f"Verdadeiro")
