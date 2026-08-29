import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("IEEE AI ML/student_performance.csv")

plt.figure(figsize=(20, 6))
plt.bar(df["Student"], df["Final_Score"])
plt.xlabel("Student")
plt.ylabel("Final Scores")
plt.title("Student vs Scores")
plt.xticks(rotation=45)   
plt.show()

plt.scatter(df["Hours_Studied"],df["Final_Score"])
plt.xlabel("Hours Studied")
plt.ylabel("Final Scores")
plt.title("Hours Studied vs Scores") 
plt.show()

plt.hist(df["Final_Score"], rwidth=0.9, edgecolor="black")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.xticks(range(0, 90, 10))    
plt.yticks(range(0, 25, 2))     
plt.title("Final Scores") 
plt.show()

plt.bar(df["Final_Score"] - df["Previous_Score"],df["Hours_Studied"])
plt.xlabel("Improvement")
plt.ylabel("Hours Studied")     
plt.title("Improvement vs Hours Studied") 
plt.show()
