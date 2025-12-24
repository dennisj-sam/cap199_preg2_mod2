# Solución
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0.5, 2*np.pi, 500)
y = np.sin(x)

plt.style.use('default')

puntos = [0, np.pi/4, np.pi/2, np.pi, 3*np.pi/2]
colores = ['red', 'green', 'blue', 'magenta', 'cyan']
labels = [
    'Tangente en x=0',
    'Tangente en x=π/4',
    'Tangente en x=π/2',
    'Tangente en x=π',
    'Tangente en x=3π/2'
]

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(x, y, color='0.3', linewidth=3, label='f(x) = sin(x)')

for x0, color, label in zip(puntos, colores, labels):
    y0 = np.sin(x0)
    m = np.cos(x0)
    xt = np.linspace(x0 - 0.8, x0 + 0.8, 100)
    yt = m * (xt - x0) + y0
    ax.plot(xt, yt, color=color, linewidth=2, label=label)
    ax.scatter(x0, y0, color=color, s=80, zorder=5)

ax.axhline(0, color='gray', linewidth=1)
ax.axvline(0, color='gray', linewidth=1)
ax.set_title('Rectas tangentes a f(x) = sin(x)', fontsize=14)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_xlim(-0.5, 2*np.pi)
ax.set_ylim(-1.1, 1.5)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()
