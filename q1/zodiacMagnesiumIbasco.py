birthyear = int(input("Enter your birth year: "))

if birthyear < 1900:
    print("Invalid Year.")
else:
    zodiac_sign = (birthyear - 4) % 12

    if zodiac_sign == 0:
        print("Your zodiac sign is Rat (鼠 / Shǔ).")
    elif zodiac_sign == 1:
        print("Your zodiac sign is Ox (牛 / Niú).")
    elif zodiac_sign == 2:
        print("Your zodiac sign is Tiger (虎 / Hǔ).")
    elif zodiac_sign == 3:
        print("Your zodiac sign is Rabbit (兔 / Tù).")
    elif zodiac_sign == 4:
        print("Your zodiac sign is Dragon (龙 / Lóng).")
    elif zodiac_sign == 5:
        print("Your zodiac sign is Snake (蛇 / Shé).")
    elif zodiac_sign == 6:
        print("Your zodiac sign is Horse (马 / Mǎ).")
    elif zodiac_sign == 7:
        print("Your zodiac sign is Goat (羊 / Yáng).")
    elif zodiac_sign == 8:
        print("Your zodiac sign is Monkey (猴 / Hóu).")
    elif zodiac_sign == 9:
        print("Your zodiac sign is Rooster (鸡 / Jī).")
    elif zodiac_sign == 10:
        print("Your zodiac sign is Dog (狗 / Gǒu).")
    else:
        print("Your zodiac sign is Pig (猪 / Zhū).")