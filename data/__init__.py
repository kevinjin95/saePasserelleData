from data.Data import saeData

# le département du précédent établissement scolaire
def depEtScol():
    depEtScol = saeData()
    depEtScol.path = '/home/jk1234/Documents/BUT2/SAE/saePasserelleData/data/static/excel/PS_SD.xlsx'
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
    bourse.path = '/home/jk1234/Documents/BUT2/SAE/saePasserelleData/data/static/excel/PS_SD.xlsx'
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
    hf.path = '/home/jk1234/Documents/BUT2/SAE/saePasserelleData/data/static/excel/PS_SD.xlsx'
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
    academie.path = '/home/jk1234/Documents/BUT2/SAE/saePasserelleData/data/static/excel/PS_SD.xlsx'
    academie.row2Recup = 'Académie du bac'
    academie.recupData()
    academie.createDict()
    academie.countDict()
    academie.dictToData()
    academie.showChartPie()
    academie.printData("proportion")
