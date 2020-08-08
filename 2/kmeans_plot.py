import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Before clustering
df = pd.read_csv("iris.csv", header=None, usecols = [0, 1])
df.columns = ["Sepal.Length", "Sepal.Width"]
sns.scatterplot(x=df["Sepal.Length"], 
                y=df["Sepal.Width"])
plt.title("Scatterplot of sepals in iris dataset")

# After clustering
plt.figure()
df = pd.read_csv("output.csv")
sns.scatterplot(x=df.x, y=df.y, 
                hue=df.c, 
                palette=sns.color_palette("hls", n_colors=2))
plt.xlabel("Sepal.Length")
plt.ylabel("Sepal.Width")
plt.title("Clustered: K = 2 clusters")

plt.show()
