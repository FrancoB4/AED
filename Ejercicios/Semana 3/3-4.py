"""Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo (hora y minutos),
determine cuál es su duración en minutos. Si el viajero necesita luego 45 minutos más para ir del aeropuerto al hotel
que ha reservado, ¿a qué hora llegara al mismo? """

start_time = input('Horario de partida (hh:mm): ')
end_time = input('Horario de llegada (hh:mm): ')

h1, h2 = int(start_time[:2]), int(end_time[:2])
m1, m2 = int(start_time[3:5]), int(end_time[3:5])

duration = (h2 * 60 + m2) - (h1 * 60 + m1)
minutes_hotel_total = (h2 * 60 + m2) + 45
hours_hotel = minutes_hotel_total // 60
minutes_hotel = minutes_hotel_total - (hours_hotel * 60)

print(f"El vuelo tiene una duracion de: {duration}\nla hora de llegada al hotel es: {hours_hotel}:{minutes_hotel}")