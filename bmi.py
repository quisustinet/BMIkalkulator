from easygui import *
def error_msg(missing):
    msgbox(
        f"Wystąpił błąd. Nie podano prawidłowych danych: {missing}.\n"\
        +"Uruchom program jeszcze raz.","Kalkulator BMI", "Zakończ"
        )
def bmi_main():
    msgbox(
        "Witaj w programie obliczającym Twoje BMI(Body Mass Index).\n\n"\
        +"Obliczenia i wnioski wyciągnięte na ich podstawie"\
        +"mają charakter poglądowy i dotyczą jedynie osób dorosłych.\n\n"\
        +"Dla wyliczeń dotyczących dzieci stosuje się np. siatki centylowe."\
        ,"Kalkulator BMI","Dalej"
        )
    age=integerbox(
        "Podaj swój wiek:","Kalkulator BMI",None,19,120
        )
    height=integerbox(
        "Podaj swój wzrost [cm]:","Kalkulator BMI",None,50,250
        )
    weight=integerbox(
        "Podaj swoją wagę [kg]:","Kalkulator BMI",None,10,350
        )
    try:
        height/=100
    except:
        error_msg("wzrost")
        raise ValueError("Nie podano wzrostu")
    try:
        bmi=round(weight/height**2,2)
    except:
        error_msg("waga")
        raise ValueError("Nie podano wagi.")
    risk1="minimalne, ale zwiększony poziom wystąpienia innych problemów zdrowotnych"
    risk2="minimalne"
    risk3="średnie"
    risk4="wysokie"
    risk5="bardzo wysokie"
    risk6="ekstremalny poziom ryzyka"
    if bmi<16:
        cat="wygłodzenie"
        risk=risk1
    elif bmi<17:
        cat="wychudzenie"
        risk=risk1
    elif bmi<18.5:
        cat="niedowaga"
        risk=risk1
    elif bmi<25:
        cat="optimum"
        risk=risk2
    elif bmi<30:
        cat="nadwaga"
        risk=risk3
    elif bmi<35:
        cat="otyłość I stopnia"
        risk=risk4
    elif bmi<40:
        cat="otyłość II stopnia (duża)"
        risk=risk5
    elif bmi>=40:
        cat="otyłość III stopnia (chorobliwa)"
        risk=risk6
    else:
        error_msg()
    try:
        if age<25:
            dbmi="19 - 24"
        elif age<35:
            dbmi="20 - 25"
        elif age<45:
            dbmi="21 - 26"
        elif age<55:
            dbmi="22 - 27"
        elif age<65:
            dbmi="23 - 28"
        elif age>=65:
            dbmi="24 - 29"
    except:
        error_msg("wiek")
    msgbox(
        "Twoje BMI wynosi "+str(bmi).replace(".",",")+".\n"\
        +f"Twoja kategoria masy ciała według WHO to: {cat}.\n\n"\
        +"Według WHO BMI osób dorosłych powinno być w przedziale 18,5 - 24,99,\n"\
        +"natomiast według autorów książki \"Żywienie : atlas i podręcznik\""\
        +"(ISBN 978-83-7609-653-7) w Twoim wieku pożądanym BMI jest to "\
        +f" mieszczące się w przedziale: {dbmi}.\n\n"\
        +f"Twoje ryzyko chorób towarzyszących otyłości:\n{risk}.\n"
        ,"Kalkulator BMI","Zakończ"
        )
    return 0
bmi_main()
