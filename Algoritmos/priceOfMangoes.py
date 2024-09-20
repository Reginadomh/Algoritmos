def mango_cost(quantity, price_per_mango):
    # Los mangos que se pagan son todos los que están en grupos de 2 + los que sobran fuera de esos grupos
    paid_mangoes = (quantity // 3) * 2 + (quantity % 3)
    # Multiplicamos los mangos que se pagan por el precio unitario
    return paid_mangoes * price_per_mango

# Casos de prueba
print(mango_cost(3, 5))  # Debería devolver 10 (3 mangos, pero pagamos por 2)
print(mango_cost(9, 2))  # Debería devolver 12 (9 mangos, pero pagamos por 6)
print(mango_cost(7, 4))  # Debería devolver 20 (7 mangos, pagamos por 4 + 1)
