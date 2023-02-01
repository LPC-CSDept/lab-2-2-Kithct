def main():
    ##################################################
    # Comlete your code here
    ##################################################
    WH = int(input('Working hours: '))
    RH = 40
    RR = 18.25
    OR = 27.78
    RC = RH*RR
    OC = (WH-RH)*OR
    TT = OC+RC
    print("Regular Charges: ", RC)
    print("Overtime Hours: ", OC)
    print("Total wages: ", TT)
    pass


if __name__ == '__main__':
    main()
