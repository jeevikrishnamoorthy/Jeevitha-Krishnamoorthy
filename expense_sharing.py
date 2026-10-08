import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# 1. CREATE EXPENSE DATA
# ==========================================

data = {
    "Person": ["Jeevitha", "Friend A", "Friend B", "Friend C"],
    "Food": [500, 200, 100, 100],
    "Travel": [300, 200, 100, 0],
    "Shopping": [200, 100, 100, 100]
}

df = pd.DataFrame(data)


# ==========================================
# 2. CALCULATE TOTAL EXPENSE
# ==========================================

df["Total_Expense"] = df[["Food", "Travel", "Shopping"]].sum(axis=1)

total_expense = df["Total_Expense"].sum()

number_of_people = len(df)

fair_share = total_expense / number_of_people


# ==========================================
# 3. CALCULATE BALANCE
# ==========================================

df["Fair_Share"] = fair_share

df["Balance"] = df["Total_Expense"] - df["Fair_Share"]


# ==========================================
# 4. DISPLAY EXPENSE DETAILS
# ==========================================

print("\n========== EXPENSE DETAILS ==========")

print(df)

print("\nTotal Group Expense: ₹", total_expense)

print("Fair Share Per Person: ₹", fair_share)


# ==========================================
# 5. FIND CREDITORS AND DEBTORS
# ==========================================

creditors = []
debtors = []

for _, row in df.iterrows():

    if row["Balance"] > 0:
        creditors.append([row["Person"], row["Balance"]])

    elif row["Balance"] < 0:
        debtors.append([row["Person"], -row["Balance"]])


# ==========================================
# 6. CALCULATE SETTLEMENT
# ==========================================

print("\n========== SETTLEMENT DETAILS ==========")

i = 0
j = 0

while i < len(debtors) and j < len(creditors):

    debtor = debtors[i]
    creditor = creditors[j]

    amount = min(debtor[1], creditor[1])

    print(
        debtor[0],
        "should pay",
        creditor[0],
        "₹",
        round(amount, 2)
    )

    debtor[1] -= amount
    creditor[1] -= amount

    if debtor[1] == 0:
        i += 1

    if creditor[1] == 0:
        j += 1


# ==========================================
# 7. CATEGORY-WISE EXPENSE ANALYSIS
# ==========================================

category_totals = df[["Food", "Travel", "Shopping"]].sum()

print("\n========== CATEGORY-WISE EXPENSE ==========")

print(category_totals)


# ==========================================
# 8. CREATE BAR CHART
# ==========================================

category_totals.plot(
    kind="bar",
    title="Category-wise Spending"
)

plt.xlabel("Expense Category")

plt.ylabel("Amount (₹)")

plt.tight_layout()

plt.show()