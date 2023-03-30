'''---------------------------------------------------------------------------

# Feladat: Két szám összege.
# Írj egy függvényt "osszead" néven, amely két számot kap ésvisszatér a két szám összegével.'''
def osszead(szam1, szam2):
  ...
  return szam1 + szam2

print(f'Két szám összege: 12 és -8 összege: 4')
print(f'Két szám összege: 12 és -8 összege: {osszead(12, -8)}\n')

'''-------------------------------------------------------------------

# Feladat: Melyik a kisebb?
# Írj egy függvényt "kisebb" néven, amely két számot kap és visszatér a legkisebbel.'''
def kisebb(szam1, szam2):
    if szam1 < szam2:
        return szam1
    else:
        return szam2

print(f'Melyik a kisebb?: 12 és -8 közül a kisebb: -8')        
print(f'Melyik a kisebb?: 12 és -8 közül a kisebb: {kisebb(12, -8)}\n')

'''---------------------------------------------------------------------------

# Feladat: Melyik a nagyobb?
# Írj egy függvényt "nagyobb" néven, amely két számot kap és visszatér a legnagyobbal.'''
def nagyobb(szam1, szam2):
    if szam1 > szam2:
      return szam1
    else:
      return szam2

print(f'Melyik a nagyobb?: 12 és -8 közül a nagyobb: 12')
print(f'Melyik a nagyobb?: 12 és -8 közül a nagyobb: {nagyobb(12, -8)}\n')

'''---------------------------------------------------------------------------

# Feladat: Számtani közép
# Írj "szamtani_kozep" néven függvényt, amely két számot kap bemenetként és visszatér a számtani középpel.'''

def szamtani_kozep(szam1, szam2):
    ...
    

print(f'Számtani közép: 3.0 és 5.0 számtani közepe: 4.0')
print(f'Számtani közép: 3.0 és 5.0 számtani közepe: {szamtani_kozep(3, 5)}\n')

'''---------------------------------------------------------------------------

# Feladat: Négyzet kerülete
# Írj "negyzet_kerulet" néven függvényt, amely egy négyzet oldalhosszát kapja bemenetként és visszatér a négyzet kerületével.'''

def negyzet_kerulet(oldalhossz):
    ...
    return 4 * oldalhossz
    
print(f'Négyzet kerülete: Ha 5.1 a négyzet oldala, akkor a négyzet kerülete = 20.4')
print(f'Négyzet kerülete: Ha 5.1 a négyzet oldala, akkor a négyzet kerülete = {negyzet_kerulet(5.1)}\n')

'''---------------------------------------------------------------------------

# Feladat: Négyzet területe
# Írj "negyzet_terulet" néven függvényt, amely egy négyzet oldalhosszát kapja bemenetként és visszatér a négyzet területével.'''

def negyzet_terulet(oldalhossz):
    return oldalhossz ** 2
    
print(f'Négyzet területe: Ha 5.0 a négyzet oldala, akkor a négyzet területe = 25.0')
print(f'Négyzet területe: Ha 5.0 a négyzet oldala, akkor a négyzet területe = {negyzet_terulet(5.0)}\n')

'''---------------------------------------------------------------------------

# Feladat: Téglalap kerülete
# Írj "teglalap_kerulet" néven függvényt, amely egy téglalap oldalhosszait kapja bemenetként és visszatér a téglalap kerületével.'''

def teglalap_kerulet(oldal1, oldal2):
   oldal3 = (oldal1 + oldal2)* 2
   return oldal3 

    
print(f'Téglalap kerülete: Ha 5 az egyik oldal és 6 a másik oldal, akkor a téglalap kerülete =', 22)
print(f'Téglalap kerülete: Ha 5 az egyik oldal és 6 a másik oldal, akkor a téglalap kerülete = {teglalap_kerulet(5, 6)}\n')
  
'''---------------------------------------------------------------------------

# Feladat: Téglalap területe
# Írj "teglalap_terulet" néven függvényt, amely egy téglalap oldalhosszait kapja bemenetként és visszatér a téglalap területével.'''

def teglalap_terulet(oldal1, oldal2):
   oldal3 = oldal1 * oldal2
   return oldal3 
   

print(f'Téglalap területe: Ha 5 az egyik oldal és 6 a másik oldal, akkor a téglalap területe = 30')
print(f'Téglalap területe: Ha 5 az egyik oldal és 6 a másik oldal, akkor a téglalap területe = {teglalap_terulet(5, 6)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Két szám különbsége
# Írj "kulonbseg" néven függvényt, amely két számot kap bemenetként és visszatér a két szám különbségével.'''
def kulonbseg(szam1, szam2):
    ...
    return szam1 - szam2
    
print(f'Két szám különbsége: Ha 5 az egyik szám és 6 a másik szám, akkor a két szám különbsége = -1')
print(f'Két szám különbsége: Ha 5 az egyik szám és 6 a másik szám, akkor a két szám különbsége = {kulonbseg(5, 6)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Maradékos osztás:  
# Írj egy "maradek" nevü függvényt, amely két számot kap bemenetként és visszatér a két szám osztásának maradékával. '''
def maradek(szam1, szam2):
    szam3 = szam1 % szam2
    return szam3 

print(f'Maradékos osztás: Ha 9 az egyik szám és 4 a másik szám, akkor a két szám osztásának maradéka = 1')
print(f'Maradékos osztás: Ha 9 az egyik szám és 4 a másik szám, akkor a két szám osztásának maradéka = {maradek(9, 4)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Páros szám:  
Írj egy "paros" nevü függvényt, amely egy számot kap bemenetként, majd True-val tér vissza, ha a szám páros és False-al ha a szám páratlan. '''
def paros(szam1):
    if szam1 % 2 == 0:
      return True
    else:
      return False
print(f'Páros szám: Ha a  szám 9 akkor a visszatérési érték: False')
print(f'Páros szám: Ha a  szám 9 akkor a visszatérési érték: {paros(9)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Kettővel osztható:  
# Írj egy "kettovel_oszthato" nevü függvényt, amely egy számot kap bemenetként és True-val tér vissza, ha a szám kettővel osztható és False-al ha nem. '''
def kettovel_oszthato(szam1):
    if szam1 % 2 == 0:
      return True
    else:
      return False 

print(f'Kettővel osztható: Ha a  szám 12 akkor a visszatérési érték: True')
print(f'Kettővel osztható: Ha a  szám 12 akkor a visszatérési érték: {kettovel_oszthato(12)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Hárommal osztható:  
# Írj egy "harommal_oszthato" nevü függvényt, amely egy számot kap bemenetként és True-val tér vissza, ha a szám hárommal osztható és False-al ha nem. '''
def harommal_oszthato(szam1):
    if szam1 % 3 == 0:
      return True
    else:
      return False

print(f'Hárommal osztható: Ha a  szám 15 akkor a visszatérési érték: True')
print(f'Hárommal osztható: Ha a  szám 15 akkor a visszatérési érték: {harommal_oszthato(15)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Héttel osztható:  
# Írj egy "hettel_oszthato" nevü függvényt , amely egy számot kap bemenetként és True-val tér vissza, ha a szám héttel osztható és False-al ha nem. '''
def hettel_oszthato(szam1):
    if szam1 % 7 == 0:
      return True
    else:
      return False

print(f'Héttel osztható: Ha a  szám 21 akkor a visszatérési érték: True')
print(f'Héttel osztható: Ha a  szám 21 akkor a visszatérési érték: {hettel_oszthato(21)}\n')







#------------------------------------------------------------------------------------------------------------

