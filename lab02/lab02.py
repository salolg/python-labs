from sys import argv
if len(argv)==1:
	print('Zle uruchomienie programu, nalezy podac parametry wywolania programu')

l=argv[1:]
a=""
s=a.join(l)
print(s)

m_l = [el for el in s if el.islower()]
print(m_l)

d_l = [el for el in s if el.isupper()]
print(d_l)

n = [el for el in s if el.isdigit()]
print(n)

n_n = [el for el in s if not el.isalpha()]
print(n_n)


m_bez_powt=[]

for el in m_l:
	if el not in m_bez_powt:
		m_bez_powt.append(el)
print(m_bez_powt)

count_l=[]

for el in m_bez_powt:
	count_l.append((el, s.count(el)))
print(count_l)

count_l.sort(key = lambda x : x[1])
print(count_l)

samogloski=['a','i','o', 'e', 'u', 'y', 'A', 'I','O', 'E', 'U', 'Y']
liczba_sam=0

for el in s:
	if el in samogloski:
		liczba_sam+=1
print(liczba_sam)


liczba_spol=0

for el in s:
	if el not in samogloski:
		liczba_spol+=1
print(liczba_spol)


list_2=[]

for el in n:
	list_2.append((int(el), (liczba_sam*int(el) + liczba_spol)))
print(list_2)

list_2=[(int(el), (liczba_sam*int(el) + liczba_spol)) for el in n ]
print(list_2)


x_srednie=0
x_srednie=sum(i[0] for i in list_2)
x_srednie=x_srednie/len(list_2)
print(x_srednie)

y_srednie=0
y_srednie=sum(i[1] for i in list_2)
y_srednie=y_srednie/len(list_2)
print(y_srednie)

D= sum((i[0]-x_srednie)**2 for i in list_2)
print(D)

b=y_srednie - liczba_sam*y_srednie
a=(1/D)*sum(y*(x-x_srednie) for x,y in list_2)
print(b)
print(a)

