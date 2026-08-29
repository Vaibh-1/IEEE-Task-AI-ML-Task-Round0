import pandas as pd
df = pd.read_csv("student_performance.csv")
print(df[0:5])
print("The no of rows and columns are:",df.shape)
print("Columns\n",list(df.columns))
print("Any empty values:",df.isnull().values.any())
print("The average of fianal score is:",df["Final_Score"].mean())
highest = df["Final_Score"].max()
max_score = df[df["Final_Score"] == highest]
print("Highest marks:",max_score)
df["Improvement"] = df["Final_Score"] - df["Previous_Score"] 
print("The first 5 rows:\n",df[0:5])
print(df[df["Attendance"]>=80])
df_arranged = df.sort_values("Final_Score", ascending=False)
df_arranged.to_csv("processed_student_performance.csv", index=False)





