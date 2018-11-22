def konversiSuhu (C = "none", F = "none"):
    "mengkonversikan suhu dari Celcius ke fahrenheit dan sebaliknya"
    suhu = 0
    if (C == "none") and (F == "none"):
        print ("suhu 0 celcius setara dengan 32 fahrenheit")
    elif (C == "none") and (F == "none"):
        suhu = (F - 32) * 5/9
        print "suhu", F, "Fahrenheit setara dengan", int(suhu), "celcius"
    elif (C != "none") and (F == "none"):
        suhu = (C * 9/5) + 32
        print "suhu", C, "Celcius setara dengan", int(suhu), "Fahrenheit"
