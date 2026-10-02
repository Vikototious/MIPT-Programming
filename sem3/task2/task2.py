import matplotlib.pyplot as plt
import numpy as np
import random

N_steps = 1000
N_particles = 1000

steps = np.random.choice([-1, 1], size=(N_particles, N_steps))

positions = np.zeros((N_particles, N_steps + 1))
positions[:, 1:] = np.cumsum(steps, axis=1)
N_axis = np.arange(N_steps + 1)

plt.figure(figsize=(15, 5))

# Траектория одной частицы x(N)
plt.subplot(1, 3, 1)
plt.plot(N_axis, positions[0], color='tab:blue', lw=1.5)
plt.title("Траектория одной частицы $x(N)$")
plt.xlabel("Количество шагов ($N$)")
plt.ylabel("Положение ($x$)")
plt.grid(True)


# Конечные положения 1000 частиц после 1000 шагов
plt.subplot(1, 3, 2)
plt.hist(positions[:, -1], bins=30, color='tab:orange', edgecolor='black', alpha=0.7)
plt.title("Гистограмма положений после 1000 шагов")
plt.xlabel("Конечное положение ($x$)")
plt.ylabel("Количество частиц")
plt.grid(True)

# Среднеквадратичное отклоение?
plt.subplot(1, 3, 3)
rms = np.sqrt(np.mean(positions**2, axis=0))

plt.plot(N_axis, rms, label="Экспериментальный RMS", color='tab:green', lw=2)
plt.plot(N_axis, np.sqrt(N_axis), label="Теоретический $\sqrt{N}$", color='black', linestyle='--')
plt.title("Зависимость RMS от шагов $N$")
plt.xlabel("Количество шагов ($N$)")
plt.ylabel("RMS")
plt.legend()
plt.grid(True)

plt.savefig('sem3/task2/mysecondplot.pdf', bbox_inches='tight')
plt.tight_layout()
plt.show()