from matplotlib.pyplot import *
#import math
import pandas as pd
# X=[k/10 for k in range(-3, 4)]
# Y=[x**2 for x in X]
# plot(X, Y, lw= 10, linestyle= ':', c= 'y') #pour obtenir un graphe avec une droite
# plot(X, Y, "y:", lw= 10)
# scatter(X, Y, None, c='y', marker="*", alpha=1) #pour obtenir un
# graphe avec des points
# xlim(-1, 1) #pour délimiter les bords de la fenetre graphique en X
# ylim(-1, 1) #pour délimiter les bords de la fenetre graphique en Y
# title('toto') #pour informer un titre au graphe
# grid(True) #pour avoir un graphe avec un grillage
# show()

# pour obtenir un graphique polaire
# T=[math.pi/6, math.pi/4, math.pi/3]
# R=[1, 2, 3]
# polar(T, R)
# show()

# pour obtenir un diagramme en baton
# X=[1, 2, 10]
# H=[50, 20, 75]
# bar(X, H)
# show()

# pour obtenir un graphique polaire
# path='PS_SD.xlsx'
# df = pd.read_excel(path)
# df2 = [i for i in df['Département établissement']]
# i = [j+1 for j in range(95)]
# T=[math.pi/6, math.pi/4, math.pi/3]
# R=[1, 2, 3]
# print("t: ", T)
# print("r: ", R)
# pie(T, R)
# show()

# Alice={
#    'Math':15,
#    'Stat':18,
#    'Proba':8
# }
# Bob={
#    'Math': 10.5,
#    'Stat': 9,
#    'Proba': 10,
#    'Info': 17
# }

# CLASSE={
#    "Alice" : Alice,
#    "Bob" : Bob
# }

# Classe = pd.DataFrame(CLASSE)
# print(Classe)

#def createDataList():
#   global df3
#    df3 = [i for i in df2]
#    global cpt
#    cpt = [i * 0 for i in range(95)]

#def countInt(val2Check):
#    cpt = 0
#    for i in df2:
#        if i == val2Check:
#            cpt += 1
#    return cpt

#def count():
#    global numDep
#    numDep = [i + 1 for i in range(95)]
#    for i in numDep:
#        for j in df3:
#            if j == i:
#                cpt[i - 1] += 1

#def supprNan():
#    nan = 1191 - len(df3)
#    i = 0
#    while i != len(dict):
#        if cpt[i] == 0:
#            cpt.pop(i)
#            nan += 1
#            numDep.pop(i)
#        else:
#            i += 1
#    numDep.append('nan')
#    cpt.append(nan)

class saeData:
    #permet l'initialisation de la variable et toutes ses instances
    def __init__(self):
        self.path = ""
        self.row2Recup = ""
        self.list = []
        self.data = []
        self.dict = {}
        self.classe = pd.DataFrame()

    #permet de récupérer les données util présentes sur le fichier excel et les enregistrer dans list
    def recupData(self):
        df = pd.read_excel(self.path, usecols=[self.row2Recup])
        self.list = [i for i in df[self.row2Recup] if str(i) != "nan"]

    #permet d'ajouter à la variable dict toutes les associations 'clé-valeur' de la list
    def createDict(self):
        for i in self.list:
            if not (self.dict.get(i)):
                self.dict.update({i: 0})

    #permet d'incrémenter les valeurs de dict en fonction de list
    def countDict(self):
        for i in self.list:
            self.dict[i] = self.dict.get(i) + 1

    #permet de séparer les clés des valeurs et les enregistrer dans 2 variables différentes
    def dictToData(self):
        self.label = [i for i in self.dict.keys()]
        self.data = [i for i in self.dict.values()]

    #permet de regrouper les valeurs inférieur à une certaine limite pour rendre plus lisible le graphe
    def groupInf8(self):
        self.label.append("inférieur à 8")
        self.data.append(0)
        cptInf = 0
        i = 1
        while i < len(self.label) - 1:
            if self.data[i] <= 7:
                self.label.pop(i)
                self.data.pop(i)
                cptInf += 1
            else:
                i += 1
        self.data[-1] = cptInf

    #permet d'afficher le graphe à partir des variables données et label
    def showChartPie(self):
        pie(self.data, explode=None, labels=self.label)
        show()

    #permet d'insérer une 'clé-valeur' en début de liste pour présenter ce qui est affiché et de les afficher
    def printData(self, vals):
        self.label.insert(0, self.row2Recup)
        self.data.insert(0, vals)
        self.classe = pd.DataFrame(self.data, self.label)
        print("classe: ", self.classe)

# le département du précédent établissement scolaire
def depEtScol():
    depEtScol = saeData()
    depEtScol.path = 'PS_SD.xlsx'
    depEtScol.row2Recup = 'Département établissement'
    depEtScol.recupData()
    depEtScol.createDict()
    depEtScol.countDict()
    depEtScol.dict.update({"nan": 1191 - len(depEtScol.list)})
    depEtScol.dictToData()
    depEtScol.groupInf8()
    depEtScol.showChartPie()
    depEtScol.printData("proportion")

# les boursiers/non-boursiers
def bourse():
    bourse = saeData()
    bourse.path = 'PS_SD.xlsx'
    bourse.row2Recup = 'Boursier'
    bourse.recupData()
    bourse.dict = {"Boursier de l'enseignement supérieur": 0, "Boursier du secondaire": 0, "Non boursier": 0}
    bourse.countDict()
    bourse.dictToData()
    bourse.showChartPie()
    bourse.row2Recup = 'statut bourse'
    bourse.printData("proportion")

# homme-femme
def hf():
    hf = saeData()
    hf.path = 'PS_SD.xlsx'
    hf.row2Recup = 'Sexe'
    hf.recupData()
    hf.dict = {"F": 0, "M": 0}
    hf.countDict()
    hf.dictToData()
    hf.showChartPie()
    hf.printData("proportion")

#l'académie de leur ancien établissement scolaire
def academie():
    academie = saeData()
    academie.path = 'PS_SD.xlsx'
    academie.row2Recup = 'Académie du bac'
    academie.recupData()
    academie.createDict()
    academie.countDict()
    academie.dictToData()
    academie.showChartPie()
    academie.printData("proportion")

depEtScol()

