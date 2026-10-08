import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Dataset base sur les tendances officielles du chômage au Maroc (HCP)
data = {
    'Année': [2021, 2022, 2023, 2024, 2025],
    'Taux_Chomage_%': [12.3, 11.8, 13.0, 13.5, 13.1],
}

df = pd.DataFrame(data)

print('--- Aperçu des données du Chômage au Maroc ---')
print(df)

# Configuration du graphique
sns.set_theme(style='whitegrid')
plt.figure(figsize=(8, 5))

plt.plot(
    df['Année'],
    df['Taux_Chomage_%'],
    marker='o',
    color='b',
    linestyle='-',
    linewidth=2.5,
    markersize=8,
)

plt.title(
    "Évolution du Taux de Chômage au Maroc (2021-2025)",
    fontsize=14,
    fontweight='bold',
    pad=15,
)
plt.xlabel('Années', fontsize=12)
plt.ylabel('Taux de Chômage (%)', fontsize=12)
plt.ylim(10, 15)

for i, txt in enumerate(df['Taux_Chomage_%']):
    plt.annotate(
        f'{txt}%',
        (df['Année'][i], df['Taux_Chomage_%'][i] + 0.15),
        ha='center',
        fontsize=10,
        fontweight='bold',
    )

plt.tight_layout()
plt.savefig('evolution_chomage_maroc.png', dpi=300)
print(
    "\nGraphique généré et sauvegardé avec succès sous le nom de"
    " 'evolution_chomage_maroc.png' !"
)

plt.show()