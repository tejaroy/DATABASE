def add(x, y):
    print(x + y)


def add(x, y):
    print(x + y)


def sub(x, y):
    print(x - y)


def sub(x, y):
    print(x - y)


def mul(x, y):
    print(x * y)


def mul(x, y):
    print(x * y)


def div(x, y):
    print(x / y)


def div(x, y):
    print(x / y)


while True:
    a = int(input('enter the value of 1st:'))
    b = int(input('enter the value of 2nd:'))
    print('--------------------------------')
    print('1.addition')
    print('2.subtarction')
    print('3.mulplation')
    print('4.didvision')
    print('5.exit')
    print('----------------------------------')
    opt = int(input('enter any option'))
    # addition
    if opt == 1:
        add(a, b)
        c = a + b
        print('output of value', c)
        d = int(input('enter the value of 3rd'))
        while True:
            print('--------------------------------')
            print('1.addition')
            print('2.subtarction')
            print('3.mulplation')
            print('4.didvision')
            print('5.exit')
            print('----------------------------------')
            opt = int(input('enter any option'))
            if opt == 1:
                add(c, d)
                c = c + d
                print('output of the value', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break
            elif opt == 2:
                sub(c, d)
                c = c - d
                print('final value=', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break
            elif opt == 3:
                mul(c, d)
                c = c * d
                print('final value=', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break

                break
            elif opt == 4:
                div(c, d)
                c = c / d
                print('final value=', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break
            elif opt == 5:
                break
        break
    # sub
    elif opt == 2:
        sub(a, b)
        c = a - b
        print('final value=', c)
        d = int(input('enter the value of 3rd'))
        while True:
            print('--------------------------------')
            print('1.addition')
            print('2.subtarction')
            print('3.mulplation')
            print('4.didvision')
            print('5.exit')
            print('----------------------------------')
            opt = int(input('enter any option'))
            if opt == 1:
                add(c, d)
                c = c + d
                print('output of the value', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break
            elif opt == 2:
                sub(c, d)
                c = c - d
                print('final value=', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break

            elif opt == 3:
                mul(c, d)
                c = c * d
                print('final value=', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break
            elif opt == 4:
                div(c, d)
                c = c / d
                print('final value=', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break
            elif opt == 5:
                break
        break
    # mul
    elif opt == 3:
        mul(a, b)
        c = a * b
        print('final value=', c)
        d = int(input('enter the value of 3rd'))
        while True:
            print('--------------------------------')
            print('1.addition')
            print('2.subtarction')
            print('3.mulplation')
            print('4.didvision')
            print('5.exit')
            print('----------------------------------')
            opt = int(input('enter any option'))
            if opt == 1:
                add(c, d)
                c = c + d
                print('output of the value', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break
            elif opt == 2:
                sub(c, d)
                c = c - d
                print('final value=', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break

            elif opt == 3:
                mul(c, d)
                c = c * d
                print('final value=', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break
            elif opt == 4:
                div(c, d)
                c = c / d
                print('final value=', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break
            elif opt == 5:
                break
        break
    # div
    elif opt == 4:
        div(a, b)
        c = a / b
        print('final value=', c)
        d = int(input('enter the value of 3rd'))
        while True:
            print('--------------------------------')
            print('1.addition')
            print('2.subtarction')
            print('3.mulplation')
            print('4.didvision')
            print('5.exit')
            print('----------------------------------')
            opt = int(input('enter any option'))
            if opt == 1:
                add(c, d)
                c = c + d
                print('output of the value', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break
            elif opt == 2:
                sub(c, d)
                c = c - d
                print('final value=', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break

            elif opt == 3:
                mul(c, d)
                c = c * d
                print('final value=', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))

                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break
            elif opt == 4:
                div(c, d)
                c = c / d
                print('final value=', c)
                d = int(input('enter the value of 4th'))
                while True:
                    print('--------------------------------')
                    print('1.addition')
                    print('2.subtarction')
                    print('3.mulplation')
                    print('4.didvision')
                    print('5.exit')
                    print('----------------------------------')
                    opt = int(input('enter any option'))
                    if opt == 1:
                        add(c, d)
                        c = c + d
                        print('output of the value', c)
                        break
                    elif opt == 2:
                        sub(c, d)
                        c = c - d
                        print('output of the value', c)
                        break
                    elif opt == 3:
                        mul(c, d)
                        c = c * d
                        print('output of the value', c)
                        break
                    elif opt == 4:
                        div(c, d)
                        c = c / d
                        print('output of the value', c)
                        break
                    break
                break
            elif opt == 5:
                break
        break
    elif opt == 5:
        break
    else:
        print('invaild input....')
print()
