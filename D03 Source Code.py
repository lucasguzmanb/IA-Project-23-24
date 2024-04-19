from MFIS_Classes import *
from MFIS_Read_Functions import *

# read all information from files
fuzzySetsDict = readFuzzySetsFile("Files\InputVarSets.txt") # correct file??
rules = readRulesFile()
applicationList = readApplicationsFile()


print("*** Fuzzy sets dict ***")
fuzzySetsDict.printFuzzySetsDict()

print("*** Rule list ***")
rules.printRuleList()

print("*** Application list ***")
for x in applicationList:
    x.printApplication()
