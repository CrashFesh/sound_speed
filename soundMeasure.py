import soundFunctions as sf
import os

dat_dir = os.getcwd()
os.chdir("..")
dat_dir = os.getcwd()
dat_dir += '\\data\\dat.txt'
f = open(dat_dir, 'w') #Открываем файл dat.txt, находящийся в директории data для записи

# строим 2 массива на 5 тыс значений, вычисляющий для каждой концентрации углекислого газа (0-5%) скорость звука
q1 = []
p1 = []
for i in range (0, 5001): 
    q1.append(i / 1000)
    p1.append(sf.speed_of_sound(24, 2990 * 30 / 100, q1[i])) #24 град. C , давление насыщенного пара при 24 град., ~ (нигде не было написано: сколько градусов и какая влажность была)
    f.write(str(q1[i]) + ' ' + str(p1[i]) + '\n')
f.write('\n')

q2 = []
p2 = []
for i in range(0, 5001):
    q2.append(i / 1000)
    p2.append(sf.speed_of_sound(24, 2990 * 30 / 100, q2[i]))
    f.write(str(q2[i]) + ' ' + str(p2[i]) + '\n')

k1 = (p1[0] - p1[5000]) / (q1[5000] - q1[0]) #убеждаемся, что график приближённо линеен, и определяем модуль коэффициента наклона (функция имеет вид: a(x3)=p[0]-k*x3)
k2 = (p2[0] - p2[5000]) / (q2[5000] - q2[0])
f.close()

# --- Поиск экспериментально полученных значений скорости звука --- #
collected = {}
clear_air = sf.experimental_v('\\data\\1-clear.txt')
no = sf.experimental_v('\\data\\1-no.txt')
collected[clear_air] = round((p1[0] - clear_air) / k1, 3) #расчёт концентраций CO2
collected[no] = round((p2[0] - no) / k2, 3) 
f = open(dat_dir, 'a')
f.write(f'\n{str(clear_air)} {collected[clear_air]}\n{str(no)} {collected[no]}')
f.close()