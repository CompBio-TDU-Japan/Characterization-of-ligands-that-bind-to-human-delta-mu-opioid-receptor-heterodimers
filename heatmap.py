import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("OPRM1-OPRD1_PCA_heatmap_data.csv")

sns.set(style="white", color_codes = True)
sns.jointplot(x = df.loc[:, "X"], y = df.loc[:, "Y"], kind = "hist", color = "deepskyblue")
plt.savefig('OPRM1-OPRD1_PCA_heatmap.png')