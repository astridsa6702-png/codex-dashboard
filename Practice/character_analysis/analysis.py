import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("characters.csv")
# print(df)

# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.describe())

stat_cols = ["Power", "Endurance", "Defense", "Agility", "Intelligence", "Perception"]

group_avg = df.groupby("Group")[stat_cols].mean().round(2)
group_avg["Group Average"] = group_avg.mean(axis=1).round(2)
group_avg = group_avg.sort_values("Group Average", ascending=False)
# print(group_avg)
# print("\n")

# # How many characters have Power above 75?
# high_power = df[df["Power"] > 75]
# print("How many characters have Power above 75?")
# print(len(high_power))

# # Who are they?
# print("Who are they?")
# print(high_power["Name"])
# print("\n")

# # Characters with Agility below 60 — how many and who are they?
# low_agility = df[df["Agility"] < 60]
# print("How many characters with Agility below 60?")
# print(len(low_agility))
# print("Who are they?")
# print(low_agility["Name"])
# print("\n")

# # Average Defense of characters with Total above 440
# avg_defense = df[df["Total"] > 440]
# print("Average Defense of characters with Total above 440")
# print(avg_defense["Defense"].mean())
# print("\n")

# # Average Intelligence of Analysts only
# analysts = df[df["Group"] == "Analysts"]
# print("Average Intelligence of Analysts only")
# print(analysts["Intelligence"].mean())

# # Average Power per group
# group_avg.plot(kind="bar", y="Power", legend=False)
# plt.title("Average Power by Group")
# plt.ylabel("Power")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# The two characters to compare
chars = ["Paula Lopez", "Hayami Amamiya"]
stats = ["Power", "Endurance", "Defense", "Agility", "Intelligence", "Perception"]

# Get their stat values
paula = df[df["Name"] == "Paula Lopez"][stats].values.flatten().tolist()
hayami = df[df["Name"] == "Hayami Amamiya"][stats].values.flatten().tolist()

# Radar charts need the data to loop back to the start
angles = np.linspace(0, 2 * np.pi, len(stats), endpoint=False).tolist()
angles += angles[:1]
paula += paula[:1]
hayami += hayami[:1]

# Build the chart
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

ax.plot(angles, paula, "b-", linewidth=2, label="Paula")
ax.plot(angles, hayami, "r-", linewidth=2, label="Hayami")
ax.fill(angles, paula, alpha=0.1, color="blue")
ax.fill(angles, hayami, alpha=0.1, color="red")

ax.set_xticks(angles[:-1])
ax.set_xticklabels(stats)
ax.set_title("Paula vs Hayami — Stat Profile", size=14)
ax.legend(loc="upper right")

plt.tight_layout()
plt.show()