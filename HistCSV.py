# Use this script to inspect the CSV file outputted from root2csv.py
import pandas as pd
import matplotlib.pyplot as plt
from features import column_names

fname = "csv/topreco_augmented1.csv"
df = pd.read_csv(fname, names=column_names)
columns = df.columns
shape = df.shape
print("Shape of Data: {}".format(shape))
for i in range(len(columns)):
    plt.clf()
    fig = plt.figure()
    plt.hist(df[column_names[i]], bins=100, label=column_names[i])
    plt.legend()
    plt.title("Number of Events: {}".format(shape[0]))
    plt.ylabel("Counts")
    output_filedir = fname.split("/")[-1].split("_")[-1].split(".")[0]
    plt.savefig("Plots/{0}/{1}.png".format(output_filedir, column_names[i]))
