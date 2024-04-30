CODES = [
    "1101",
    "0110",
    "00001",
    "11001",
    "10010",
    "00011",
    "1010"
]

DEPTH = 10


def check_available_places(start_code: str):
    if start_code in CODES:
        return False
    if len(start_code) == DEPTH:
        return True
    code0 = start_code+"0"
    code1 = start_code+"1"
    code0_available = check_available_places(code0)
    code1_available = check_available_places(code1)
    if code0_available and code1_available:
        return True
    elif code0_available:
        print(code0)
        return False
    elif code1_available:
        print(code1)
        return False


check_available_places("")
