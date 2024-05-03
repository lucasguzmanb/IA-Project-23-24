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

resultFile = open("Files\Results.txt", "w")  # open/create results file (truncate content)

for app in applicationList:

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
        rule_activation_value = min(
            fuzzySetsDict[setid].memDegree for setid in rule.antecedent
        )
        # rule_activation_value *= rule.strength # uncomment if we want to take strength of rules into account
        # Add the rule activation to the list
        rule_activations[rule.ruleName] = [
            max(rule_activation_value, 0),
            rule.consequent,
        ]

    rule_activations = {
        key: [value, consequent]
        for key, [value, consequent] in rule_activations.items()
        if value > 0
    }  # discard all non-activated rules (those with activation value 0)

    # DEFUZZYFICATION
    for key in riskDict:
        rules_that_apply = [
            rule_activations[rule][0]
            for rule in rule_activations
            if rule_activations[rule][1] == key
        ]  # discard all rules from rule_activations that are not of the risk we are looking for
        if not rules_that_apply:
            riskDict[key].memDegree = 0
        else:
            riskDict[key].memDegree = max(
                [
                    rule_activations[rule][0]
                    for rule in rule_activations
                    if rule_activations[rule][1] == key
                ]
            )

    # INTERPRET THE RESULT & WRITE ON RESULTS FILE
    # obtaining the maximum degree of the 3 risk values
    max_degree = float("-inf")
    resultRisk = ""
    for value in riskDict.values():
        if max_degree < value.memDegree:
            max_degree = value.memDegree
            resultRisk = value.label
    riskWord = {"LowR": "Low", "MediumR": "Medium", "HighR": "High"}
    resultFile.write(f"App {app.appId}: {riskWord[resultRisk]} risk, degree {max_degree}\n")

resultFile.close()
