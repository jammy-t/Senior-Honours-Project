import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_11 = pd.read_csv(r"C:\Users\myles\.vscode\DAQ\SenHon\1_1_extended_flowcurve.csv")
df_10 = pd.read_csv(r"C:\Users\myles\.vscode\DAQ\SenHon\1_0_flowcurve.csv")
df_00 = pd.read_csv(r"C:\Users\myles\.vscode\DAQ\SenHon\0_0_flowcurve.csv")

plt.figure(figsize=(8,6))

plt.loglog(df_11["phi"], df_11["sigma_y"], 'o-', label="μS=1 μR=1")
plt.loglog(df_10["phi"], df_10["sigma_y"], 's-', label="μS=1 μR=0")
plt.loglog(df_00["phi"], df_00["sigma_y"], '^-', label="μS=0 μR=0")

plt.xlabel("Packing fraction φ", fontsize=14, fontweight='bold')
plt.ylabel("Yield stress σ_y", fontsize=14, fontweight='bold')
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()