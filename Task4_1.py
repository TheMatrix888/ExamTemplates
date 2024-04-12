table = {
    "И": "0001",
    "Н": "1110",
    "Ф": "1111",
    "О": "1000",
    "Р": "001",
    "М": "110",
    "А": "0000",
    "Т": "101",
    "К": "01"
}


def available_positions(code=""):
    for letter, letter_code in table.items():
        if code == letter_code:
            return False
    if len(code) > 4:
        print(code)
        return True
    h = [available_positions(code + digit) for digit in "01"]
    if not h[0] and not h[1]:
        return False


available_positions()
