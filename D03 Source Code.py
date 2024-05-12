from MFIS_Classes import *
from MFIS_Read_Functions import *
import skfuzzy as fuzz

# read all information from files
fuzzySetsDict = readFuzzySetsFile("Files\InputVarSets.txt")
ruleList = readRulesFile()
applicationList = readApplicationsFile()
riskDict = readFuzzySetsFile("Files\Risks.txt")

# print("*** Risks set dict ***")
# riskDict.printFuzzySetsDict()

# print("*** Rule list ***")
# rules.printRuleList()

# print("*** Application list ***")
# for x in applicationList:
#     x.printApplication()

resultFile = open(
    "Files\Results.txt", "w"
)  # open/create results file (truncate content)
resultFile.write("----- RISK RESULTS -----\n")
minimum = 100
maximum = 0 # for analysis Q2

for app in applicationList:
    print(f"\n*** APP {app.appId} ***")

    # FUZZYFICATION
    inputDict = {str(key): val for key, val in app.data}
    # obtain memdegree for each fuzzyset for this application
    for setid in fuzzySetsDict:
        fuzzySetsDict[setid].memDegree = fuzz.interp_membership(
            fuzzySetsDict[setid].x,
            fuzzySetsDict[setid].y,
            inputDict[fuzzySetsDict[setid].var],
        )

    # INFERENCE FROM RULES
    rule_activations = {}
    for rule in ruleList:
        # Calculate the rule activation as the minimum of the membership degrees of the fuzzy sets in the rule's antecedent
        rule_activation_value = float("inf")
        for setid in rule.antecedent:
            rule_activation_value = np.fmin(
                fuzzySetsDict[setid].memDegree, rule_activation_value
            )
            # rule_activation_value *= rule.strength # uncomment if we want to take strength of rules into account
        if rule_activation_value != 0:
            riskDict[rule.consequent].memDegree = np.fmin(
                rule_activation_value, riskDict[rule.consequent].y
            )

    # DEFUZZYFICATION
    aggregated = np.fmax(
        riskDict["Risk=LowR"].memDegree,
        np.fmax(riskDict["Risk=MediumR"].memDegree, riskDict["Risk=HighR"].memDegree),
    )
    x = np.arange(0, 101, 1)
    risk_result = fuzz.defuzz(x, aggregated, "centroid")
    print(f"FINAL RESULT: {risk_result}")
    minimum = min(minimum, risk_result)
    maximum = max(maximum, risk_result)
    
    # WRITE ON RESULTS FILE
    resultFile.write(f"\n*** APP {app.appId} ***\nRISK: {risk_result}\n")

print(minimum)
print(maximum)

resultFile.close()
