import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import matplotlib.artist as art
import os

dat_dir = os.getcwd()
os.chdir("..")
dat_dir = os.getcwd()
dat_dir += '\\data\\dat.txt'
f = open(dat_dir) #Открываем файл dat.txt, находящийся в директории data для чтения

q1 = []
p1 = []
s = ''
while True: #считываем значения концентраций и скоростей звука в массивы
    s = f.readline()
    if s == '\n':
        break
    s = list(map(float, s.split()))
    qs = s[0] # qs=s[:s.find(' ')]
    ps = s[1] # то же самое, только s.find + 1:
    q1.append(float(qs))
    p1.append(float(ps))

q2 = []
p2 = []
while True: #считываем значения концентраций и скоростей звука в массивы
    s = f.readline()
    if s == '\n':
        break
    s = list(map(float, s.split()))
    qs = s[0] # qs=s[:s.find(' ')]
    ps = s[1] # то же самое, только s.find + 1:
    q2.append(float(qs))
    p2.append(float(ps))

# --- Считывание точек для графика (пункт 5) --- #
s = f.readline().split()
a_clear_air = float(s[0])
c_clear_air = float(s[1])
s = f.readline().split()
a_no = float(s[0])
c_no = float(s[1])
f.close()

# --- Собственно построение --- #
fig, ax = plt.subplots()
ax.scatter(c_clear_air, a_clear_air, marker='D', edgecolors='black', s=30, label='Значения в воздухе: 346.577 м/с, 0.836 %', color='yellow', zorder=4)
ax.scatter(c_no, a_no, marker='D', edgecolors='black', s=30, label='Значения в выдохе: 344.515 м/с, 4.368 %', color='red', zorder=4)
ax.plot(q1, p1, linestyle='-', linewidth = 1.5,  color= 'forestgreen', label='Аналитическая зависимость для чистого воздуха', zorder=3) #строим график
ax.plot(q2, p2, linestyle='-', linewidth = 1.5,  color= 'crimson', label='Аналитическая зависимость для воздуха из лёгких', zorder=3)
ax.legend(loc=0) #добавляем легенду
ax.set_ylabel('Скорость звука, м/с') #подписываем оси
ax.set_xlabel('Концентрация CO2, %')
ax.set_title('Зависимость скорости звука\nот концентрации углекислого газа', loc='center', pad=10) #подписываем график
ax.set_xlim([-0.1, 5.1]) #устанавливаем пределы концентраций и скоростей звука для графика
ax.set_ylim([342.8, 348.5])
ax.yaxis.set_minor_locator(tic.MultipleLocator(0.2)) #делаем сетку
ax.xaxis.set_minor_locator(tic.MultipleLocator(0.2))
ax.yaxis.set_major_locator(tic.MultipleLocator(1))
ax.xaxis.set_major_locator(tic.MultipleLocator(1))
ax.grid(axis= 'both', which = 'minor', linestyle='--', linewidth=0.5, color='lightgrey')
ax.grid(axis= 'both', which = 'major', linestyle='-', linewidth=1, color='lightgrey')
plt.show() #показ графика
dat_dir = os.getcwd() #сохранение графика в директорию plots
dat_dir += '\\plots\\plot.svg'
fig.savefig(dat_dir)