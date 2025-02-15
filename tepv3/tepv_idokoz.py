from sys import stdin

def convert_date_to_int(time_str: str) -> int:
    return int(time_str[:2]) * 60 + int(time_str[3:])

def main():
    peti_erkezesi_ideje = stdin.readline().strip()
    aktualis_ido = stdin.readline().strip()
    int_erk_ido = convert_date_to_int(peti_erkezesi_ideje)
    int_akt_ido = convert_date_to_int(aktualis_ido)

    print((int_akt_ido - int_erk_ido) % 1440)

if __name__ == '__main__':
    main()
