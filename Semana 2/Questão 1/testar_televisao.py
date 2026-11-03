from televisao import Televisao

tv1 = Televisao("Samsung", 43)
tv2 = Televisao("LG", 50)
tv3 = Televisao("Philco", 32)

televisores = [tv1, tv2, tv3]

tv1.ligada = True
tv1.canal = 5
tv1.volume = 25

tv2.ligada = True
tv2.canal = 12
tv2.volume = 70

for tv in televisores:
    if tv.ligada:
        print(f'{tv.marca} {tv.polegadas}" | Ligada | Canal {tv.canal} | Volume {tv.volume}')
    else:
        print(f'{tv.marca} {tv.polegadas}" | Desligada')

ligadas = 0

for tv in televisores:
    if tv.ligada:
        ligadas += 1

print(f"Televisores ligados: {ligadas}")

maior = None

for tv in televisores:
    if maior is None or tv.polegadas > maior.polegadas:
        maior = tv

print(f'Maior televisor: {maior.marca} {maior.polegadas}"')

media = sum(tv.polegadas for tv in televisores) / len(televisores)

print(f"Média de polegadas: {media:.2f}")