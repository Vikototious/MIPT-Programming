import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('sem3/iris_data.csv')

fig, axes = plt.subplots(2, 3, figsize=(16, 9))
axes = axes.flatten() 

combinations = [
    ('SepalWidthCm', 'SepalLengthCm'),
    ('PetalLengthCm', 'SepalLengthCm'),
    ('PetalWidthCm', 'SepalLengthCm'),
    ('PetalLengthCm', 'SepalWidthCm'),
    ('PetalWidthCm', 'SepalWidthCm'),
    ('PetalWidthCm', 'PetalLengthCm')
]

species_list = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = {'Iris-setosa': 'tab:blue', 'Iris-versicolor': 'tab:orange', 'Iris-virginica': 'tab:green'}

print("=== КОЭФФИЦИЕНТЫ ПРЯМЫХ МНК (y = k*x + b) ===\n")

for i, (x_col, y_col) in enumerate(combinations):
    ax = axes[i]
    
    print(f"График {i+1}: {y_col} от {x_col}")
    
    # 1. Общая прямая МНК по всем видам вместе
    coef_all = np.polyfit(data[x_col], data[y_col], 1)
    print(f"  [Все виды вместе]  k = {coef_all[0]:.4f}, b = {coef_all[1]:.4f}")
    
    for sp in species_list:
        sub = data[data['Species'] == sp]
        x_val = sub[x_col].values
        y_val = sub[y_col].values
        
        ax.scatter(x_val, y_val, label=sp, color=colors[sp], alpha=0.7)
        
        coef = np.polyfit(x_val, y_val, 1)
        p = np.poly1d(coef)
        x_sorted = np.sort(x_val)
        
        ax.plot(x_sorted, p(x_sorted), color=colors[sp], linestyle='--')
        print(f"  [{sp:15s}] k = {coef[0]:.4f}, b = {coef[1]:.4f}")
    
    ax.set_title(f"{y_col} vs {x_col}")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.6)
    print("-" * 50)

plt.tight_layout()

plt.savefig('sem3/task1/myplot.pdf', bbox_inches='tight')

plt.show()  