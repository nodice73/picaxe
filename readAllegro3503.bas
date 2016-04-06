symbol N = 100 ; number of reads to make average

main:
    gosub avein
    sertxd("w1 ave: ", #w1, lf)

    select case w1
        case < 5070
            pwmout pwmdiv4,2,88, 286 
        case > 5070
            pwmout pwmdiv4,2,88, 286 
        else
            pwmout 2,OFF
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
