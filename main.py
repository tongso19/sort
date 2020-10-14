def on_button_pressed_a():
    global A
    A += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global C
    C += 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global B
    B += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

A = 0
B = 0
C = 0

def on_forever():
    if A < B and B < C:
        basic.show_number(A)
        basic.show_number(B)
        basic.show_number(C)
    elif A < B and B > C:
        basic.show_number(A)
        basic.show_number(C)
        basic.show_number(B)
    elif B < A and A < C:
        basic.show_number(B)
        basic.show_number(A)
        basic.show_number(C)
    elif B < C and A > C:
        basic.show_number(B)
        basic.show_number(C)
        basic.show_number(A)
    elif C < A and B > A:
        basic.show_number(C)
        basic.show_number(A)
        basic.show_number(B)
    elif C < B and B < A:
        basic.show_number(C)
        basic.show_number(B)
        basic.show_number(A)
basic.forever(on_forever)
