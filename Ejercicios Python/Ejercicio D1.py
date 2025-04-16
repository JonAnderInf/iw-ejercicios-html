    
diccionario = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}

valor_unico = []

for key in diccionario:
    valor_actual=diccionario[key]
    if valor_actual not in valor_unico:
     valor_unico.append(valor_actual)


