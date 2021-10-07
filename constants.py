NUMBERS = range(37)

NUMBER_RANGES = {
    'red': [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
    'black': [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
    '1-18': range(1, 19),
    '19-36': range(19, 37),
    'even': [n for n in NUMBERS if n % 2 == 0],
    'odd': [n for n in NUMBERS if n % 2 == 1],
    '1-12': range(1, 13),
    '13-24': range(13, 25),
    '25-36': range(25, 37)
}


