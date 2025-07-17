from math import exp, sqrt
from datetime import date
from typing import Counter
today = date.today()

##def prim_iter(n):
##  temp = 2
##  controller = (n > temp)
##
##  if controller:
##      while temp < n:
##          controller = not (n % temp == 0)
##          if not controller:
##              break
##          temp += 1
##
##  return controller
##
##def result():
##  print("scrivi un numero\n")
##  x = int(input("Inserisci un numero intero: "))
##  controller = prim_iter(x)
##  if controller == 0:
##   print("no primo")
##  else:
##    print("primo")
##  return 0
##result()

#funzione che ritorna il numero di numeri primi in un array
##

##
##def primeInArray(arr):
##  countPrime =0 ## return dei numeri primi
##
##  for i in arr:
##   if i != 0 and i  !=1:
##    temp = 2
##    while temp<i:
##      controller =(i%temp == 0) ## se true allora no primo
##      if not  controller:
##          countPrime = countPrime +1
##      temp = temp +1
##
##  return  countPrime
##
##print(primeInArray([6,6,6]))

#classi
# le funzioni dentro classi = metodi
# ad ogni classe corrisponde un oggetto
#il parametro self serve per riferimento allo scope esterno del metodo abbaia se tolgo self mi dice che razza non esiste
#__init__ è il costruttore del oggetto
# se inizializzo

##class cane():
##  razza = 'olmo'
##  def __init__(self,colore,peso):
##    self.colore = colore
##
##  def abbaia(self):
##        print(self.razza)
##        print('bau')
##
##
##pluto = cane("nero",40)
##print(pluto.colore)
##pluto.razza = 'gatto'
##print(pluto.razza)
##print(pluto.razza)
##
##
##
##class Borsa():
##  def __init__(self,nome):
##    self.nome = nome
##    self.contenuto = []
##  def aggiungi(self, oggetto):
##    self.contenuto.append(oggetto)
##
##borsa_blu = Borsa("blue")
##borsa_blu.aggiungi("occhiali")
##print(borsa_blu.contenuto)
##
##borsa_blu.aggiungi("chiavi")
##print(borsa_blu.contenuto)

# scrivere un metodo che prende in input 2 paramentri 1 oggetto che deve essere messo dentro la borsa e il 2 paramentro dice numero di vole che deve essere  inserito

##class Mynum():
##  def __init__(self, num):
##    self.num = num
##
##  def __iter__(self):
##    return self
##
##  def __next__(self):
##    self.num += 3
##    if (self.num <30):
##      return self.num
##    else:
##      raise StopIteration
##
##  def __str__(self):
##    return 'Il mio valore è {}'.format(self.num)
##
##iteratore = Mynum(2)
##print(iteratore) # questo deve essere uguale a
##for item in iteratore:
##  print(item)
##print(iteratore) # questo

##Definisci una classe Persona  con le variabili nome  e età. Aggiungi un metodo che stampi un saluto con nome ed età.

#class Persona():
#  def __init__(self, nome):
#    self.nome = nome
#  def saluta(self):
#    return  f"ciao {self.nome}"
#
#
#
#test = Persona('giva')
#
#print(test.saluta())

# 2. Crea una classe Rettangolo

# La classe deve avere base  e altezza  come attributi. Aggiungi un metodo area   che restituisca l’area del #rettangolo.

#class rettangolo():
#   def __init__(self, base, altezza):
#     self.base = base
#     self.altezza = altezza
#   def calcola(self):
#       #area =   sqrt(exp(self.base) * exp(self.altezza))
#       area = self.base * self.altezza /2
#       return area
#
#
#retQ = rettangolo(2,10)
#print(retQ.calcola())
#

#3. Classe Contatore
#Crea una classe che rappresenta un contatore. Deve avere un metodo incrementa()  e un metodo valore().
#
#class Contatore():
#  def __init__(self,counter = 0):
#    self.counter = counter
#  def incrementa(self):
#    self.counter = self.counter +1
#    return self.counter
#  def valore(self):
#    return  self.incrementa()
#
#time = Contatore(0)
#print(time.valore())
#

# 4. Classe Libro
#Crea una classe con titolo, autore, e numero di pagine. Aggiungi un metodo __str__  che restituisca una descrizione del libro.

#class Libro():
#  def __init__(self,titolo,autore,n_pagine):
#    self.titolo = titolo
#    self.autore = autore
#    self.n_pagine = n_pagine
#  def __str__(self):
#    return f"{self.titolo} {self.autore} {self.n_pagine}"
#
#libro1 = Libro("gatto","pippo",33)
#print(libro1.__str__())

# 5. Classe Studente
#
#Crea una classe Studente  che tenga traccia del nome e del numero diesami superati. Aggiungi un metodo per aggiungere un esame e stampare il totale.
#
#class Studente():
#  def __init__(self,nome,esami_superati =[]):
#    self.nome = nome
#    self.esami_superati = esami_superati
#
#  def inserisci(self,nome):
#    self.esami_superati.append(nome)
#
#  def __str__(self):
#    return f"{self.nome} {self.esami_superati}"
#
#
#studente1  = Studente("martin",['aaa','bbbb'] )
#studente1.inserisci('gatto')
#print(studente1)

# 6. Classe ContoBancario
#Implementa una classe con saldo, deposita(), preleva()  e un metodo __str__()  che mostri il saldo.
#
#class ContoBancario():
#  def __init__(self,conto):
#    self.conto = conto
#
#  def deposita(self,deposito):
#    self.conto =  self.conto + deposito
#  def preleva(self,prelievo):
#    self.conto =  self.conto -prelievo
#  def __str__(self):
#    return  f"{self.conto}"
#
#persona1 = ContoBancario(100)
#persona1.preleva(150)
#print(persona1)

# 7. Classe Animale
#Crea una classe Animale  con metodo verso()  che stampa “verso generico”. Crea una sottoclasse Cane  che sovrascrive il metodo con “bau”.


#class Animale():
#
#  def __init__(self, nome):
#    self.nome = nome
#
#  def verso(self):
#    verso = "verso generico"
#    return verso
#
#  def __str__(self):
#    ret = f"{self.verso()}"
#    return ret
#
#
#class Cane(Animale):
#
#  def verso(self):
#    verso = "bau"
#    return verso
#
#
#a = Cane('a')
#a.verso()
#print()
# 16. Classe Quadrato  che eredita da Rettangolo
#Utilizza l'esercizio 2 e crea una sottoclasse Quadrato  che imposta base e altezza uguali.
 
#class Rettangolo():
#    def __init__(self, altezza , base):
#          self.base = base
#          self.altezza = altezza
#
#    def calcola(self):   
#            res = self.base * self.altezza
#            return res
#    
#class Quadrato(Rettangolo):
#    def  __init__(self, altezza, base):
#          super().__init__(altezza, base)
#
#    def reset(self):
#         if(self.base != self.altezza):
#               self.base =  self.altezza
#      
#     
#    
#            
#ret1 = Quadrato(5 ,100)
#ret1.reset()
#print( ret1.calcola() )



#class rettangolo():
#   def __init__(self, base, altezza):
#     self.base = base
#     self.altezza = altezza
#   def calcola(self):
#       #area =   sqrt(exp(self.base) * exp(self.altezza))
#       area = self.base * self.altezza /2
#       return area
#
#
#retQ = rettangolo(2,10)
#print(retQ.calcola())
#
# 8. Classe Temperatura

#Crea una classe con un attributo gradi_celsius. Aggiungi un metodo per convertirla in Fahrenheit.
 #
 #class Temperatura():
 #  def __init__(self,C):
 #    self.C = C
 ## da Celsius (°C) a Fahrenheit (°F) input * 9/5 + 32
 #  def convert(self):
 #    F = self.C * (9/5) +32
 #    return F
 #
 #nuovaTemperatura = Temperatura(10)
 #print(nuovaTemperatura.convert())

#9. Classe ContoCorrente  con limiti

#Estendi l’esercizio 6 con un limite massimo di prelievo giornaliero.
 


#class ContoCorrente():
#   dateToday =   today.strftime("%d/%m/%Y")
#   Data_ultimo_prelievo = ''  
#   Counter = 0
#   def __init__(self,conto):
#     self.conto = conto
#     
#   def deposita(self,deposito):
#     self.conto =  self.conto + deposito
#     
#   def preleva(self,prelievo):
#     self.Counter = self.Counter +1
#     if(self.Counter == 1):
#        self.Data_ultimo_prelievo = self.dateToday
#     if(self.Counter  <= 6 and  self.Data_ultimo_prelievo == self.dateToday ):
#        self.conto =  self.conto -prelievo
#        
#     if(self.Data_ultimo_prelievo != self.dateToday):
#        self.Counter = 0
     
#       
#   def __str__(self):
#     return  f"{self.conto}"
#
# persona1 = ContoCorrente(0)

#10. Classe Timer  iterabile
#Crea una classe che conta da 1 a N usando __iter__()  e __next__(). Stampare i numeri con un ciclo for.

#class Timer():
#    counter = 1
#    def __init__(self,n):
#        self.n = n
#    def  __iter__(self):
#        return self   
#    def __next__(self):
#        if(self.counter < self.n   ):
#            self.counter = self.counter +1
#            return self.counter
#        else:
#            raise StopIteration 
#temp = Timer(5)
#for x in temp:
#    print(x)
#
#0. Classe Rubrica

#Crea una classe che gestisce nomi e numeri di telefono. Aggiungi metodi per aggiungere, cercare e stampare i contatti.

#class Rubrica():
#    nominativi ={}
#
#    def aggiungi(self, nome ,numero_telefono):
#         self.nominativi[nome] =  numero_telefono
#    def cerca(self ,nome,numero_telefono):
#        #passo nome ma non numero di telefono
#        if(nome and numero_telefono == False):
#            trovato='disperso'
#            for x in self.nominativi:
#                if(x == nome):
#                    trovato = self.nominativi[x]
#                    break
#            return trovato
#        #passo numero di telefono ma non nome
#        elif(numero_telefono and nome== False):
#            trovato = 'numero disperso'
#            for x in self.nominativi:
#                if(self.nominativi[x]== numero_telefono):
#                    trovato = x
#                    break
#            return trovato
#    def __str__(self):
#        return f"{self.nominativi}"
#test1 = Rubrica()
#test1.aggiungi('pippo',111)
#test1.aggiungi('osvaldo',222)
#ricerca =  test1.cerca('pippo',False)
#print(ricerca )  
#    def __str__(self):
#        return    f"{self.nominativi}"
#
#utente1 = Rubrica()
#utente1.aggiungi('pippo',11111)
#utente1.aggiungi('giovanni',2222)
#utente1.cerca('giovanni',False)
#print(utente1)

#  trasformatore da int a binario
#class Trasformatore():
#   
#   def IntToBin(self, n) :
#      res = ''
#      while(n >= 1):
#         temp = n % 2  
#         n = n//2
#         res = res + str(temp)
#      return res[::-1]
#  
#ret =  Trasformatore()
#print(ret.IntToBin(25))
#print(ret.IntToBin(5))
# 
#a =  123
#invert = str(a)
#print( invert[::-1])
#

        

#
#class Nodo():
#  def __init__(self, valore, successivo = None):
#    self.valore = valore
#    self.successivo = successivo
# 
#class LinkedList():
#  def __init__(self,valore):
#    self.valore = valore
#  
#  def Add(self,valore):
#    
#    
#   
#nodo1 = Nodo(1)
#nodo2 = Nodo(2,nodo1)    
# 
#print(nodo2.successivo.valore) 

######################################
# dato che le liste sono composte da nodi, creiamo una classe che contenga questo tipo di oggetti
# ogni nodo in questo caso avrà come attributi il valore del nodo e il nodo a cui è associato

 
#class nodo_sing:
#  def __init__(self, valore, prec):
#    self.valore = valore
#    self.prec = prec
#
#class Coda: 
#  def __init__(self):
#    self.head = None # dove inseriamo
#    self.tail = None # dove togliamo
#
#  def enqueue(self, valore):
#    new_nodo = nodo_sing(valore, None)
#    if(self.head == None):
#      self.head = new_nodo
#    else:
#      self.head.prec = new_nodo
#      self.head = new_nodo
## head <-(4) <-(3) <-(-2) <-(1) tail
#  def dequeue(self):
#    valore = self.tail.valore
#    self.tail = self.tail.prec
#    return valore
# implementare una funzione di ricerca che torni se un valore è presente o meno nella coda
# alla fine la coda deve rimanere intatta
#lista1 = Coda()
#lista1.enqueue(1) 
#lista1.enqueue(2) 
#print(lista1.head.valore)

#lista  = linkedList()
#lista.append(1 )  
#lista.append(2 )  
#for  el in lista:
#  print(lista.head.valore)
 
#
## qui andiamo a creare la classe lista che sarà compsta da nodi.
## In questa struttura ci basta salvari il valore del nodo di testa per poi risalire a tutti gli altri
#class lista:
#  def __init__(self):
#    self.head = None # nodo in testa alla lista concatenata.
#    # quando creiamo la lista, questa è vuota quindi la testa non punta ad alcun elemento
#
#  def append(self, valore):
#    # aggiunge il valore in un nodo in testa alla lista e aggiorna la testa
#    # in modo che punti sempre all'ultimo valore inserito
#    my_nodo = nodo(valore, self.head)
#    self.head = my_nodo
#
#  def search(self, valore_cercato):
#    # cerchiamo se un valore è presente all'interno della lista
#    # usiamo una variabile "nodo" per tenere traccia di dove siamo arrivati nella ricerca
#    nodo = self.head
#    while (nodo != None):
#      if nodo.valore == valore_cercato:
#        return True
#      nodo = nodo.successivo
#    return False # Se arrivo in fondo alla lista senza trovare il valore cercato
#
#  def len(self): # torna di quanti valori è composta la lista
#    nodo = self.head
#    count = 0
#    while (nodo != None):
#      count += 1
#      nodo = nodo.successivo
#    return count
#
#  def remove_value(self, valore_cercato):
#    # rimuoviamo il valore cercato dalla lista e diciamo se siamo riusciti a rimuoverlo
#    if self.head == None: # se la testa è vuota ovviamente non c'è il valore non c'è il valore
#      return False
#
#    # per come è costruito il codice non riusicamo a vedere se l'elemento cercato è nel
#    # primo nodo della lista, quindi dobbiamo aggiungere un controllo su questo
#    if self.head.valore == valore_cercato:
#      self.head = self.head.successivo
#      return True
#
#    # Ci serve tenere traccia sia del nodo che quello che stiamo guardando.
#    # In questa maniera quando troveremo il nodo da rimuovere, possiamo reindirizzare
#    # il successivo del nodo precedente al sucessivo del nodo che stiamo guardando.
#    # Questa operazione ci serve perché altrimenti nel momento in cui eliminiamo un elemento
#    # andremmo a spezzare la lista e perderemmo il riferimento a molti dei noti
#    nodo_prec = self.head
#    nodo_att = nodo_prec.successivo
#   
#    while(nodo_att != None):
#      if nodo_att.valore == valore_cercato:
#        nodo_prec.successivo = nodo_att.successivo
#        return True
#      nodo_prec = nodo_att
#      nodo_att = nodo_att.successivo
#   
#    return False
#
#╭─────────────╮
#│ Array 1     │ → [ 50 , 20 , 70 ]
#╰─────────────╯
#       │         │     │
#       ▼         ▼     ▼
#╭─────────────╮
#│ Array 2     │ → ['A', 'B', 'C']
#╰─────────────╯
#
#╭────────────────────────────╮
#│ Array 3 (output associato) │ → [ ?, ?, ? ]
#il 3 array corrisponde ai valori del secondo array riordinato seconod i valori del primo
#
#arr1 = [ 50 , 20 , 70 ]
#for a in arr1:
#   i = a+1
#   if(i<= len(arr1)):
#     
#arr2 = ['A', 'B', 'C']
#
#obj = {1:'b', 2:'c'}
#  obj.keys() : print (obj.keys())
#keys = obj.keys()
#
#print(keys)
#def  reorder(arr1 ,arr2):
#      obj = {}
#      arr3 = []
#      for index , name in enumerate(arr1):       
#        obj[name] =   arr2[index]    
#      keys = obj.keys()
#      for  a in keys:
#        
#        if()
#        
#print(reorder(arr1 ,arr2))

###################################################
#metodo __prepr__

#Costruzione di un dizionario da zero: MyDict
#class MyDict:
#    def __init__(self):
#        self._buckets = {}
#
#    def _hash(self, key):
#        return hash(key)
#
#    def _get_bucket(self, key):
#        h = self._hash(key)
#        return self._buckets.setdefault(h, [])
#
#    def _find_pair(self, bucket, key):
#        for i, (k, v) in enumerate(bucket):
#            if k == key:
#                return i, (k, v)
#        return -1, None
#
#    def __setitem__(self, key, value):
#        bucket = self._get_bucket(key)
#        i, _ = self._find_pair(bucket, key)
#        if i == -1:
#            bucket.append((key, value))
#        else:
#            bucket[i] = (key, value)
#
#    def __getitem__(self, key):
#        bucket = self._get_bucket(key)
#        i, pair = self._find_pair(bucket, key)
#        if i == -1:
#            raise KeyError(key)
#        return pair[1]
#    
#    def __delitem__(self, key):
#        bucket = self._get_bucket(key)
#        i, _ = self._find_pair(bucket, key)
#        if i == -1:
#            raise KeyError(key)
#        bucket.pop(i)
#
#    def __contains__(self, key):
#        bucket = self._get_bucket(key)
#        i, _ = self._find_pair(bucket, key)
#        return i != -1
#    
#    def __len__(self):
#        return sum(len(bucket) for bucket in self._buckets.values())
#    
#    def __iter__(self):
#        for bucket in self._buckets.values():
#            for k, _ in bucket:
#                yield k
#
#    def get(self, key, default=None):
#        return self[key] if key in self else default
#    
#    def setdefault(self, key, default=None):
#        if key not in self:
#            self[key] = default
#        return self[key]
#    
#    def update(self, other=None, **kwargs):
#        if other:
#            for k, v in dict(other).items():
#                self[k] = v
#        for k, v in kwargs.items():
#            self[k] = v
#            
#    def pop(self, key, default=None):
#        if key not in self:
#            if default is not None:
#                return default
#            raise KeyError(key)
#        value = self[key]
#        del self[key]
#        return value
#    
#    def popitem(self):
#        for h in list(self._buckets.keys()):
#            bucket = self._buckets[h]
#            if bucket:
#                k, v = bucket.pop()
#                if not bucket:
#                    del self._buckets[h]
#                return k, v
#        raise KeyError("popitem(): dictionary is empty")
#    
#    def clear(self):
#        self._buckets.clear()
#
#    def copy(self):
#        new_dict = MyDict()
#        for k, v in self.items():
#            new_dict[k] = v
#        return new_dict
#    
#    def __repr__(self):
#
#        return self
#    def __eq__(self):
#        pass
#    @staticmethod
#    def fromkeys(keys, value = None):
#        newDict =  MyDict()
#        for x in  keys:
#            newDict[x] = value
#        return newDict
# 
#
#test1 = MyDict.fromkeys([1,2,3,4,5])
##quando la classe viene inizializzata su test1 test1 diventa un oggettoa
##quindi quando l'oggetto test1 viene chiamato detro print  il ritorno sara di default il metodo __repr__
##che serve a far si ceh il return del oggetto test  ritorni 
#
#print(test1)

#class B(Exception):
#    pass
#class C(B):
#    pass
#class D(C):
#    pass
#for cls in [B,C,D]:
#    try:
#        raise cls()
#    except D:
#        print("D")
#    except C:
#        print("C")    
#    except B:
#        print("B")
#
