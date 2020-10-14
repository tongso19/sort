input.onButtonPressed(Button.A, function () {
    A += 1
})
input.onButtonPressed(Button.AB, function () {
    C += 1
})
input.onButtonPressed(Button.B, function () {
    B += 1
})
let A = 0
let B = 0
let C = 0
basic.forever(function () {
    if (A < B && B < C) {
        basic.showNumber(A)
        basic.showNumber(B)
        basic.showNumber(C)
    } else if (A < B && B > C) {
        basic.showNumber(A)
        basic.showNumber(C)
        basic.showNumber(B)
    } else if (B < A && A < C) {
        basic.showNumber(B)
        basic.showNumber(A)
        basic.showNumber(C)
    } else if (B < C && A > C) {
        basic.showNumber(B)
        basic.showNumber(C)
        basic.showNumber(A)
    } else if (C < A && B > A) {
        basic.showNumber(C)
        basic.showNumber(A)
        basic.showNumber(B)
    } else if (C < B && B < A) {
        basic.showNumber(C)
        basic.showNumber(B)
        basic.showNumber(A)
    }
})
