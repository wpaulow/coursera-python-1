segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // 86400
resto_segundos_dias = segundos % 86400

horas = resto_segundos_dias // 3600
resto_segundos_horas = resto_segundos_dias % 3600

minutos = resto_segundos_horas // 60

segundos_restantes = resto_segundos_horas % 60

print ("%d dias, %d horas, %d minutos e %d segundos." %(dias, horas, minutos, segundos_restantes))
