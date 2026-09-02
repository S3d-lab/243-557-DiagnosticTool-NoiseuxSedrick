from motor import Motor

moteur_1 = Motor("Moteur 1", "Km/h",)

print(moteur_1.name, moteur_1.read(), moteur_1.vitesse)

moteur_1.set_value(50.0)

print(moteur_1.name, moteur_1.read(), moteur_1.vitesse)