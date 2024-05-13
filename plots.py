from matplotlib import pyplot as plt
from MFIS_Classes import *
from MFIS_Read_Functions import *
import skfuzzy as fuzz
import numpy as np

fuzzySetsDict = readFuzzySetsFile("Files\InputVarSets.txt")
riskDict = readFuzzySetsFile("Files\Risks.txt")
applicationList = readApplicationsFile()

# Income
plt.figure()

x = np.arange(0, 151, 1)
low = fuzz.trapmf(x, [-20, -10, 25, 40])
med = fuzz.trapmf(x, [20, 30, 50, 80])
high = fuzz.trapmf(x, [40, 80, 160, 170])

plt.plot(x, low, "r", linewidth=1.5)
plt.plot(x, med, "g", linewidth=1.5)
plt.plot(x, high, "b", linewidth=1.5)
plt.title(f"IncomeLevel")
plt.xlabel("Value")
plt.ylabel("Membership")

plt.show()

# Assets
plt.figure()

x = np.arange(0, 51, 1)
low = fuzz.trapmf(x, [-2, -1, 5, 20])
med = fuzz.trapmf(x, [5, 10, 20, 30])
high = fuzz.trapmf(x, [25, 30, 60, 70])

plt.plot(x, low, "r", linewidth=1.5)
plt.plot(x, med, "g", linewidth=1.5)
plt.plot(x, high, "b", linewidth=1.5)
plt.title(f"Assets")
plt.xlabel("Value")
plt.ylabel("Membership")

plt.show()

# Risk
riskId = "LowR"
plt.figure()

plt.fill_between(
riskDict[f"Risk={riskId}"].x,
np.zeros_like(riskDict[f"Risk={riskId}"].x),
riskDict[f"Risk={riskId}"].memDegree,
facecolor="b",
alpha=0.7,
)
plt.plot(
riskDict[f"Risk={riskId}"].x,
riskDict[f"Risk={riskId}"].y,
"b",
linewidth=1.5,
linestyle="--",
)
riskId = "MediumR"
plt.fill_between(
riskDict[f"Risk={riskId}"].x,
np.zeros_like(riskDict[f"Risk={riskId}"].x),
riskDict[f"Risk={riskId}"].memDegree,
facecolor="g",
alpha=0.7,
)
plt.plot(
riskDict[f"Risk={riskId}"].x,
riskDict[f"Risk={riskId}"].y,
"g",
linewidth=1.5,
linestyle="--",
)
riskId = "HighR"
plt.fill_between(
riskDict[f"Risk={riskId}"].x,
np.zeros_like(riskDict[f"Risk={riskId}"].x),
riskDict[f"Risk={riskId}"].memDegree,
facecolor="r",
alpha=0.7,
)
plt.plot(
riskDict[f"Risk={riskId}"].x,
riskDict[f"Risk={riskId}"].y,
"r",
linewidth=1.5,
linestyle="--",
)
plt.title(f"Risk of app {app.appId}")
plt.xlabel("Value")
plt.ylabel("Membership")
plt.show()


"""

    if app.appId == "0041":
        riskId = "LowR"
        plt.figure()
        plt.plot(
            riskDict[f"Risk={riskId}"].x,
            riskDict[f"Risk={riskId}"].y,
            "b",
            linewidth=1.5,
            linestyle="--",
        )
        riskId = "MediumR"
        plt.plot(
            riskDict[f"Risk={riskId}"].x,
            riskDict[f"Risk={riskId}"].y,
            "g",
            linewidth=1.5,
            linestyle="--",
        )
        riskId = "HighR"
        plt.plot(
            riskDict[f"Risk={riskId}"].x,
            riskDict[f"Risk={riskId}"].y,
            "r",
            linewidth=1.5,
            linestyle="--",
        )
        plt.fill_between(
            x,
            np.zeros_like(x),
            aggregated,
            facecolor="Orange",
            alpha=0.6,
        )
        plt.plot([risk_result, risk_result], [0, 0.5], "k", linewidth=1.5)
        plt.text(
            risk_result,
            0.5,
            round(risk_result, 4),
            bbox=dict(facecolor="white"),
            ha="center",
        )
        plt.title(f"Risk of application {app.appId}")
        plt.show()
"""