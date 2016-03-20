symbol N = 50
symbol V = 5
main:
    let w1 = 0
    for b4  = 1 to N
        readadc10 4, w0
        let w1 = w0 + w1
    next b4
    let w1 = w1 / N
    let w1 = 10 * w1
    sertxd("w1 ave: ", #w1, lf)

    if w1 < 5070 then 
        high 1 
    else 
        low 1
    endif
    pause 1
    goto main
