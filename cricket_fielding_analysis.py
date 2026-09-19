import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fielding_data.csv")

df["Performance_Score"] = (
    df["Catches"] * 10
    + df["Direct_Hits"] * 8
    + df["Runs_Saved"]
    + df["Good_Throws"] * 2
    - df["Runs_Conceded"] * 2
)

print("===== CRICKET FIELDING ANALYSIS =====")
print(df.to_string(index=False))

print("\n===== TEAM SUMMARY =====")
print("Total Catches:", df["Catches"].sum())
print("Total Direct Hits:", df["Direct_Hits"].sum())
print("Total Runs Saved:", df["Runs_Saved"].sum())
print("Total Runs Conceded:", df["Runs_Conceded"].sum())
print("Average Performance Score:", round(df["Performance_Score"].mean(), 2))

ranking = df.sort_values("Performance_Score", ascending=False)

print("\n===== PLAYER RANKING =====")
print(ranking[["Player", "Performance_Score"]].to_string(index=False))

top_player = ranking.iloc[0]

print("\n===== TOP PLAYER =====")
print("Player:", top_player["Player"])
print("Score:", top_player["Performance_Score"])

ranking.to_csv("fielding_analysis_results.csv", index=False)

plt.figure(figsize=(10, 5))
plt.bar(ranking["Player"], ranking["Performance_Score"])
plt.xlabel("Player")
plt.ylabel("Performance Score")
plt.title("T20 Cricket Fielding Performance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("fielding_performance_chart.png")
plt.show()