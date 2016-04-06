symbol N = 50
symbol V = 5

main:
    gosub avein
    sertxd("w1 ave: ", #w1, lf)
    if w1 < 5030 then
        high 1
    else
        low 1
        pwmout 2,OFF
    endif

    select case w1
        case < 4800
            pwmout pwmdiv4,2,88,286
        case 4800 to 4999
            pwmout pwmdiv4,2,88,36
        case 5000 to 5030
            pwmout pwmdiv4,2,88,18
        endselect
    pause 1
    goto main

avein:
    let w1 = 0
    for b4  = 1 to N
        readadc10 4, w0
        let w1 = w0 + w1
    next b4
    let w1 = w1 / N
    let w1 = 10 * w1
    return
