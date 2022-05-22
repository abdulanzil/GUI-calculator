from tkinter import *
from decimal import Decimal

window = Tk()

# window characteristics

window.title("Calculator")
window.iconbitmap("./calculator_icon.ico")
window.geometry("277x390")
window.configure(bg="#e3e0d8")
window.resizable(False, False)


def button_action(button_text):  # for buttons 0,1,...,9
    global flag
    disp_num = bottom_display_field.get()
    if flag == 1 or disp_num == '0':
        bottom_display.set(button_text)
        flag = 0
    elif flag == 0:
        old_number = bottom_display_field.get()
        bottom_display.set(old_number + button_text)


''' 
a = Decimal('23') 
b = Decimal('2.000')
result = a + b      # here we will get the result as 25.000

cleaning function will remove all the unwanted zeros at fractional part of the result
i.e; we gets result as 25
'''


def cleaning(result_string):
    if '.' not in result_string:
        return result_string
    else:
        point_index = result_string.index('.')
        integer_part = result_string[:point_index]
        fraction_part = result_string[point_index:]
        while fraction_part[-1] == '0' and len(fraction_part) != 1:
            fraction_part = fraction_part[:-1]
        if fraction_part == '.':
            return integer_part
        else:
            return integer_part + fraction_part


def operation_action(button_text):  # for operations +, -, x, /, =
    global flag, result, previous_operator
    prev_number = Decimal(bottom_display_field.get())
    if flag == 0 or flag == 1 and button_text == '':
        if previous_operator == '+':
            result += prev_number
        elif previous_operator == '-':
            result -= prev_number
        elif previous_operator == 'x':
            result *= prev_number
        elif previous_operator == '/':
            try:
                if not (result == 0 and prev_number == 0):
                    result /= prev_number
                else:
                    flag = 2
            except ZeroDivisionError:
                flag = 2
        else:
            result = prev_number

    previous_operator = button_text
    if flag != 2:
        top_display.set(cleaning(str(result)) + previous_operator)
        bottom_display.set('0')
        flag = 1
    else:
        top_display.set('Calculation Error')
        bottom_display.set('Press C to clear')


def message7():
    button_action('7')


def message8():
    button_action('8')


def message9():
    button_action('9')


def message4():
    button_action('4')


def message5():
    button_action('5')


def message6():
    button_action('6')


def message1():
    button_action('1')


def message2():
    button_action('2')


def message3():
    button_action('3')


def message0():
    button_action('0')


def message_point():  # . button
    global flag
    if flag == 1:
        bottom_display.set('0.')
        flag = 0
    elif flag == 0:
        old_number = bottom_display_field.get()
        if '.' not in old_number:
            bottom_display.set(old_number + '.')


def message_del():  # DEL button
    old_number = bottom_display_field.get()
    if old_number != '0' and flag != 2:
        if Decimal(old_number) // 10 == 0 and '.' not in old_number:
            bottom_display.set('0')
        else:
            bottom_display.set(old_number[:-1])


def message_plus():  # addition operation
    operation_action('+')


def message_minus():  # subtraction operation
    operation_action('-')


def message_into():  # multiplication operation
    operation_action('x')


def message_div():  # division operation
    operation_action('/')


def message_equal():  # = operation
    operation_action('')


def message_clear():  # clear all and reset calculator
    global flag, result, previous_operator
    bottom_display.set('0')
    top_display.set('0')
    flag, result = 0, 0
    previous_operator = '+'


# display fields values
top_display = StringVar()
bottom_display = StringVar()

bottom_display.set('0')
top_display.set('0')
flag, result = 0, 0
previous_operator = '+'


# for keyboards: buttons 0,1,...,9
def bind7(_):
    message7()


def bind8(_):
    message8()


def bind9(_):
    message9()


def bind4(_):
    message4()


def bind5(_):
    message5()


def bind6(_):
    message6()


def bind1(_):
    message1()


def bind2(_):
    message2()


def bind3(_):
    message3()


def bind0(_):
    message0()


def bind_point(_):
    message_point()


def bind_plus(_):
    message_plus()


def bind_minus(_):
    message_minus()


def bind_into(_):
    message_into()


def bind_div(_):
    message_div()


def bind_equal(_):
    message_equal()


def bind_del(_):
    message_del()


def bind_clear(_):
    message_clear()


window.bind('7', bind7)
window.bind('8', bind8)
window.bind('9', bind9)
window.bind('4', bind4)
window.bind('5', bind5)
window.bind('6', bind6)
window.bind('1', bind1)
window.bind('2', bind2)
window.bind('3', bind3)
window.bind('0', bind0)
window.bind('.', bind_point)
window.bind('+', bind_plus)
window.bind('-', bind_minus)
window.bind('*', bind_into)
window.bind('/', bind_div)
window.bind('=', bind_equal)
window.bind('<BackSpace>', bind_del)
window.bind('c', bind_clear)


# calculator front-end

top_display_field = Entry(window, bg="#918f89", width=23, justify=LEFT,
                          font="TimesNewRoman 15", state=DISABLED, textvariable=top_display)
bottom_display_field = Entry(window, bg="#918f89", width=14, justify=RIGHT,
                             font="TimesNewRoman 24", state=DISABLED, textvariable=bottom_display)
bt7 = Button(window, text="7", font="Arial 15 bold ", width=3, bg="#b0afab", fg="white", command=message7)
bt8 = Button(window, text="8", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message8)
bt9 = Button(window, text="9", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message9)
bt_del = Button(window, text="DEL", font="Arial 15 bold", width=3, bg="#eb2348", fg="white", command=message_del)
bt4 = Button(window, text="4", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message4)
bt5 = Button(window, text="5", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message5)
bt6 = Button(window, text="6", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message6)
bt_div = Button(window, text="/", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message_div)
bt1 = Button(window, text="1", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message1)
bt2 = Button(window, text="2", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message2)
bt3 = Button(window, text="3", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message3)
bt_into = Button(window, text="x", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message_into)
bt0 = Button(window, text="0", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message0)
bt_point = Button(window, text=".", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message_point)
bt_equal = Button(window, text="=", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message_equal)
bt_minus = Button(window, text="-", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message_minus)
bt_clear = Button(window, text="C", font="Arial 15 bold", width=3, bg="#eb2348", fg="white", command=message_clear)
bt_plus = Button(window, text="+", font="Arial 15 bold", width=3, bg="#b0afab", fg="white", command=message_plus)


top_display_field.grid(row=0, columnspan=4, pady=(10, 5), padx=10)
bottom_display_field.grid(row=1, columnspan=4, padx=10)
bt7.grid(row=2, column=0, pady=15)
bt8.grid(row=2, column=1)
bt9.grid(row=2, column=2)
bt_del.grid(row=2, column=3)
bt4.grid(row=3, column=0)
bt5.grid(row=3, column=1)
bt6.grid(row=3, column=2)
bt_div.grid(row=3, column=3)
bt1.grid(row=4, column=0, pady=15)
bt2.grid(row=4, column=1)
bt3.grid(row=4, column=2)
bt_into.grid(row=4, column=3)
bt0.grid(row=5, column=0)
bt_point.grid(row=5, column=1)
bt_equal.grid(row=5, column=2)
bt_minus.grid(row=5, column=3)
bt_clear.grid(row=6, column=0, pady=15)
bt_plus.grid(row=6, column=3)

window.mainloop()
