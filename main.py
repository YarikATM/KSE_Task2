from tkinter import *
from sympy import *

root = Tk()
root.geometry('800x700')
root.resizable(width=True, height=True)

t_title = Label(text='Введите \nзначение времени:')
row_t_value = IntVar()
t_entry = Entry(textvariable=row_t_value)

eq_title = Label(text='Уравнение:\n 21 + 100t^2')
row_eq_value = StringVar()
eq_entry = Entry(textvariable=row_eq_value)

R2_title = Label(text='Значение R2:\n60мм')
row_R2_value = IntVar()
R2_entry = Entry(textvariable=row_R2_value)

r2_title = Label(text='Значение r2:\n82мм')
row_r2_value = IntVar()
r2_entry = Entry(textvariable=row_r2_value)

R3_title = Label(text='Значение R3:\n170мм')
row_R3_value = IntVar()
R3_entry = Entry(textvariable=row_R3_value)

r3_title = Label(text='Значение r3:\n100мм')
row_r3_value = IntVar()
r3_entry = Entry(textvariable=row_r3_value)

Name_res_label = Label(text='Вычисление:')
S1_l = Label(text='S1 = y1')
V1_l = Label(text='V1 = dS1 / dt')
V1_diff_l = Label(text='V1 = dS1 / dt')
a_t1_l = Label(text='a_t1 = a1 = dV1 / dt')
Va_l = Label(text='Va = V1')
a_ta_l = Label(text='a_ta = a_1')
omega2_l = Label(text='o2 = Va / R2')
epsilon2_l = Label(text='e2 = a_ta / R2')
Vb_l = Label(text='Vb = o2 * r2')
atb_l = Label(text='atb = e2 * r2')
omega3_l = Label(text='o3 = Vb / R3')
epsilon3_l = Label(text='e3 = atb / R3')
Vm_l = Label(text='Vm = o3 * r3')
atm_l = Label(text='atm = e3 * r3')
anm_l = Label(text='anm = Vm^2 / r3')
am_l = Label(text='am = sqrt(anm^2 + atm^2)')
result = Label(text='')
result_ = Label(text='')


def calculate(event):
    try:
        eq_value = '21 + 120 * t**2'
        t_value = row_t_value.get()
        t = t_value
        R2_value = 60 / 1000
        r2_value = 82 / 1000
        R3_value = 170 / 1000
        r3_value = 100 / 1000
        S1 = eval(eq_value)  # MM
        S1_l["text"] = f'S1 = y1 = {eq_value} = {S1} мм.'
        V1_diff = diff(eq_value)  # MM/c
        V1_diff_l["text"] = f'V1 = dS1 / dt = {V1_diff} мм/с.'
        V1 = eval(str(V1_diff / 1000))  # M/c
        V1_l["text"] = f'V1 = dS1 / dt = {V1} м/с.'
        Va_l["text"] = f'Va = V1 = {V1} мм/с.'
        a1 = float(diff(V1_diff) / 1000)  # M/с^2
        a_t1_l["text"] = f'a_t1 = a1 = d({V1_diff})/dt = {a1} м/с^2.'
        a_ta_l["text"] = f'a_ta = a_1 = {a1} м/с^2.'
        omega2 = round(V1 / R2_value, 3)  # c^-1
        omega2_l["text"] = f'o2 = Va / R2 = {omega2} c^-1.'
        epsilon2 = round(a1 / R2_value, 3)  # c^-2
        epsilon2_l["text"] = f'e2 = a_ta / R2 = {epsilon2} c^-2.'
        Vb = round(omega2 * r2_value, 3)  # M/c
        Vb_l["text"] = f'Vb = o2 * r2 = {Vb} м/c.'
        atb = round(epsilon2 * r2_value, 3)  # M/c^2
        atb_l["text"] = f'atb = e2 * r2 = {atb} м/c^2.'
        omega3 = round(Vb / R3_value, 3)  # c^-1
        omega3_l["text"] = f'o3 = Vb / R3 = {omega3} с^-1.'
        epsilon3 = round(atb / R3_value, 3)  # c^-2
        epsilon3_l["text"] = f'e3 = atb / R3 = {epsilon3} с^-2.'
        Vm = round(omega3 * r3_value, 3)  # M/c
        Vm_l["text"] = f'Vm = o3 * r3 = {Vm} м/c.'
        atm = round(epsilon3 * r3_value, 3)  # M/c^2
        atm_l["text"] = f'atm = e3 * r3 = {atm} м/c^2.'
        anm = round(Vm ** 2 / r3_value, 3)
        anm_l["text"] = f'anm = Vm^2 / r3 = {anm} м/c^2.'
        am = round(sqrt(anm ** 2 + atm ** 2), 3)
        am_l["text"] = f'am = sqrt(anm^2 + atm^2) = {am} м/c^2.'
        result["text"] = f'Ответ:'
        result_["text"] = f'В момент времени t = {t} с груз 1 прошел «путь» равный {S1} мм,\n ' \
                          f'а точка М малого цилиндра блока 3 механизма имеет «нормальное ускорение» {anm} м/с2,\n ' \
                          f'«тангенциальное ускорение» {atm} м/с2 и «полное ускорение» {am} м/с2.'


    except:
        result["foreground"] = 'red'
        result["font"] = '20'
        result["text"] = f'Проверьте введенные данные.'
        pass


button = Button(text='Рассчитать')

t_title.grid(column=2, row=1)
t_entry.grid(column=2, row=2)
eq_title.grid(column=1, row=1)
R2_title.grid(column=3, row=1)
r2_title.grid(column=1, row=3)
R3_title.grid(column=2, row=3)
r3_title.grid(column=3, row=3)
button.grid(column=2, row=5)
Name_res_label.grid(column=2, row=10)
S1_l.grid(column=2, row=11)
V1_l.grid(column=2, row=13)
V1_diff_l.grid(column=2, row=12)
a_t1_l.grid(column=2, row=14)
Va_l.grid(column=2, row=15)
a_ta_l.grid(column=2, row=16)
omega2_l.grid(column=2, row=17)
epsilon2_l.grid(column=2, row=18)
Vb_l.grid(column=2, row=19)
atb_l.grid(column=2, row=20)
omega3_l.grid(column=2, row=21)
epsilon3_l.grid(column=2, row=22)
Vm_l.grid(column=2, row=23)
atm_l.grid(column=2, row=24)
anm_l.grid(column=2, row=25)
am_l.grid(column=2, row=26)
result.grid(column=2, row=27)
result_.grid(column=2, row=28)
button.bind('<Button-1>', calculate)

if __name__ == '__main__':
    root.mainloop()
    init_printing(use_unicode=False, wrap_line=False, no_global=True)
