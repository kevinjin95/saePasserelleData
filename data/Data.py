import pandas as pd
import matplotlib.pyplot as plt

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
        print(self.path)
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
        plt.pie(self.data, explode=None, labels=self.label)
        plt.show()

    #permet d'insérer une 'clé-valeur' en début de liste pour présenter ce qui est affiché et de les afficher
    def printData(self, vals):
        self.label.insert(0, self.row2Recup)
        self.data.insert(0, vals)
        self.classe = pd.DataFrame(self.data, self.label)
        print("classe: ", self.classe)