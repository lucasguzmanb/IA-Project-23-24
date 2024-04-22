from MFIS_Classes import *
from MFIS_Read_Functions import *
import skfuzzy as fuzz

# read all information from files
fuzzySetsDict = readFuzzySetsFile("Files\InputVarSets.txt")  # correct file??
rules = readRulesFile()
applicationList = readApplicationsFile()


# print("*** Fuzzy sets dict ***")
# fuzzySetsDict.printFuzzySetsDict()

# print("*** Rule list ***")
# rules.printRuleList()

# print("*** Application list ***")
# for x in applicationList:
#     x.printApplication()

# for app in applicationList:
# obtain memdegree for each fuzzyset
"""     inputDict = {
    str(key): val for key, val in applicationList[0].data
}  # {Age: 34, IncomeLeve: 73...} """
inputDict = {"Age": 35, "IncomeLevel": 38, "Assets": 19,"Amount": 8, "Job": 0, "History": 1}
for setid in fuzzySetsDict:
    fuzzySetsDict[setid].memDegree = fuzz.interp_membership(
        fuzzySetsDict[setid].x,
        fuzzySetsDict[setid].y,
        inputDict[fuzzySetsDict[setid].var],
    )
    fuzzySetsDict[setid].printSet()

