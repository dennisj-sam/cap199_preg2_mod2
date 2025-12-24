# Solución
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Boxplots de variables age, BMI y cholesterol_level', fontsize=16, fontweight='bold')


# Boxplot de edad

axes[0].boxplot(df['age'], vert=True)
axes[0].set_title('Age')
axes[0].set_ylabel('Edad')


# Boxplot de BMI

axes[1].boxplot(df['bmi'], vert=True)
axes[1].set_title('BMI')
axes[1].set_ylabel('Índice de Masa Corporal')


# Boxplot de colesterol

axes[2].boxplot(df['cholesterol_level'], vert=True)
axes[2].set_title('Cholesterol Level')
axes[2].set_ylabel('Nivel de colesterol')

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()
