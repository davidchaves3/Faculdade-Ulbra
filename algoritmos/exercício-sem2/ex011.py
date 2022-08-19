seg = int(input('Digite o valor em segundos ===>'))

horas = seg // 3600
sobrahoras = seg % 3600
minu = sobrahoras // 60
seg = sobrahoras % 60

print('Duração do evento hrs, min e seg ===>', int(horas), ':', int(minu), ':', int(seg))
