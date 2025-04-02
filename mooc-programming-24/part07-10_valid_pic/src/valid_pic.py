from datetime import datetime


def is_it_valid(pic: str) -> bool:
    # if PIC has 11 characters
    if len(pic) != 11:
        return False

    # try to convert date into numbers
    try:
        day = int(pic[0:2])
        month = int(pic[2:4])
        year = int(pic[4:6])
    except ValueError:
        return False

    # check century character
    if pic[6] == "+":
        century = 1800
    elif pic[6] == "-":
        century = 1900
    elif pic[6] == "A":
        century = 2000
    else:
        return False

    # check whether data in PIC when put together forms valid date
    try:
        birth_date = datetime(century + year, month, day)
    except ValueError:
        return False

    pic_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    # try if pid is number
    try:
        control_number = int(pic[0:6] + pic[7:10])
    except ValueError:
        return False
    # index of chacter in pic_string that should match control chacter
    if pic_string[control_number % 31] != pic[10]:
        return False

    return True
