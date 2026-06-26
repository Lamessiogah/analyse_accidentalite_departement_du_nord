import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# 1. CHARGEMENT DES DONNÉES
# =====================================

caract = pd.read_csv("caract-2024.csv", sep=";")
lieux = pd.read_csv("lieux-2024.csv", sep=";")
usagers = pd.read_csv("usagers-2024.csv", sep=";")

# =====================================
# 2. FILTRE DEPARTEMENT DU NORD
# =====================================

caract["dep"] = caract["dep"].astype(str).str.strip()

# Certains fichiers utilisent 59, d'autres 059
caract = caract[
    caract["dep"].isin(["59", "059"])
]

print("\nNombre d'accidents dans le Nord :")
print(caract["Num_Acc"].nunique())

# =====================================
# 3. AGRÉGATION DES USAGERS
# =====================================

usagers_accident = (
    usagers.groupby("Num_Acc")
    .agg(
        nb_tues=("grav", lambda x: (x == 2).sum()),
        nb_blesses_graves=("grav", lambda x: (x == 3).sum()),
        nb_blesses_legers=("grav", lambda x: (x == 4).sum())
    )
    .reset_index()
)

# =====================================
# 4. FUSION
# =====================================

df = caract.merge(lieux, on="Num_Acc", how="left")
df = df.merge(usagers_accident, on="Num_Acc", how="left")

print("Base fusionnée :", df.shape)

# =====================================
# 5. VARIABLES
# =====================================

df["accident_grave"] = (
    (df["nb_tues"] > 0)
    | (df["nb_blesses_graves"] > 0)
)

# =====================================
# 6. LIBELLÉS
# =====================================

route_labels = {
    1: "Autoroute",
    2: "Route nationale",
    3: "Route départementale",
    4: "Voie communale",
    5: "Hors réseau public",
    6: "Parking public",
    7: "Route métropolitaine",
    9: "Autre"
}

meteo_labels = {
    1: "Normale",
    2: "Pluie légère",
    3: "Pluie forte",
    4: "Neige/Grêle",
    5: "Brouillard",
    6: "Vent fort",
    7: "Temps éblouissant",
    8: "Temps couvert",
    9: "Autre"
}

df["type_route"] = df["catr"].map(route_labels)
df["meteo"] = df["atm"].map(meteo_labels)

# =====================================
# 7. ACCIDENTS PAR MOIS
# =====================================

accidents_mois = (
    df.groupby("mois")["Num_Acc"]
    .nunique()
    .sort_index()
)

plt.figure(figsize=(10,5))
accidents_mois.plot(kind="bar")
plt.title("Nord - Accidents par mois")
plt.ylabel("Nombre d'accidents")
plt.tight_layout()
plt.show()

# =====================================
# 8. ACCIDENTS PAR METEO
# =====================================

meteo = (
    df.groupby("meteo")["Num_Acc"]
    .nunique()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,5))
meteo.plot(kind="bar")
plt.title("Nord - Accidents selon la météo")
plt.ylabel("Nombre d'accidents")
plt.tight_layout()
plt.show()

# =====================================
# 9. ACCIDENTS PAR TYPE DE ROUTE
# =====================================

route = (
    df.groupby("type_route")["Num_Acc"]
    .nunique()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,5))
route.plot(kind="bar")
plt.title("Nord - Accidents par type de route")
plt.ylabel("Nombre d'accidents")
plt.tight_layout()
plt.show()

# =====================================
# 10. TAUX D'ACCIDENTS GRAVES
# =====================================

taux_grave = (
    df.groupby("type_route")["accident_grave"]
    .mean()
    .sort_values(ascending=False)
)

print("\n====================")
print("TAUX D'ACCIDENTS GRAVES")
print("====================")
print((100 * taux_grave).round(2))

# =====================================
# 11. SCORE DE RISQUE
# =====================================

risque = (
    df.groupby("type_route")
    .agg(
        accidents=("Num_Acc", "nunique"),
        blesses_graves=("nb_blesses_graves", "sum"),
        tues=("nb_tues", "sum")
    )
)

risque["score"] = (
      risque["accidents"]
    + 3 * risque["blesses_graves"]
    + 5 * risque["tues"]
)

risque = risque.sort_values(
    "score",
    ascending=False
)

print("\n====================")
print("CLASSEMENT DES RISQUES")
print("====================")
print(risque)

# =====================================
# 12. TABLEAU DE BORD
# =====================================

nb_accidents = df["Num_Acc"].nunique()

nb_accidents_graves = (
    df[df["accident_grave"]]
    ["Num_Acc"]
    .nunique()
)

print("\n====================")
print("TABLEAU DE BORD NORD")
print("====================")
print("Nombre d'accidents :", nb_accidents)
print("Accidents graves :", nb_accidents_graves)

# =====================================
# 13. EXPORT
# =====================================

risque.to_csv(
    "classement_risque_nord.csv",
    sep=";"
)

print("\nFichier exporté : classement_risque_nord.csv")