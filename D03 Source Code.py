from MFIS_Classes import *
from MFIS_Read_Functions import *
import skfuzzy as fuzz

# read all information from files
fuzzySetsDict = readFuzzySetsFile("Files\InputVarSets.txt")  # correct file??
rules = readRulesFile()
applicationList = readApplicationsFile()


print("*** Fuzzy sets dict ***")
fuzzySetsDict.printFuzzySetsDict()

print("*** Rule list ***")
rules.printRuleList()

# print("*** Application list ***")
# for x in applicationList:
#     x.printApplication()


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
    for rule in RuleList:
        # Calculate the rule activation as the minimum of the membership degrees of the fuzzy sets in the rule's antecedent
        rule_activation_value = min(
            fuzzySetsDict[setid].memDegree for setid in rule.antecedent
        )
        # rule_activation_value *= rule.strength # uncomment if we want to take strength of rules into account
        # Add the rule activation to the list
        rule_activations[rule.ruleName] = max(rule_activation_value, 0)

    rule_activations = {
        key: value for key, value in rule_activations.items() if value > 0
    }  # discard all non-activated rules (those with activation value 0)

    # DEFUZZYFICATION
    # INTERPRET THE RESULT
