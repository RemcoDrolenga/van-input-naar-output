#Remco Drolenga: PizzaCalculor

SmallPizza = float(9.45)
MediumPizza = float(11.45)
LargePizza = float(14.50)

print('Welkom, u kunt hier uw pizza bestellen, u kunt de keuzes maken tussen: Small, Medium of large. ')

SmallPizzaA = int(input("Hoeveel small sized Pizza's zou u willen bestellen?  "))
MediumPizzaA = int(input("Hoeveel medium sized Pizza's zou u willen bestellen? "))
LargePizzaA = int(input("Hoeveel Large sized Pizza's zou u willen bestellen?  "))

SmallPizzaT = SmallPizza + SmallPizzaA
MediumPizzaT = MediumPizza + MediumPizzaA
LargePizzaT = LargePizza + LargePizzaA

Totaal = str(LargePizzaT + MediumPizzaT + LargePizzaT)

print("Uw totaal bedrag bedraagd €" + Totaal + " euro. ")