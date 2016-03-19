main:
    for b0 = 1 to 5
        let w1 = b0*500
        sertxd("b0 = ", #b0, lf, "w1 = ", #w1, lf)
        high 1
        pause w1
        low 1
    next b0
    goto main
