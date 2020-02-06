import sys
import antigravity


def check_param(datedow):
    check = 0
    for elem in datedow:
        if elem.isdigit() is False:
            check = 1
            break
    if len(datedow) != 3 or check == 1:
        print("Wrong value of datedow!\n"
              "Right format: 2005-05-26-10458.68")
        return False
    return True


def check_correctness(latitude: str, longitude: str, datedow: str):
    res = datedow.split('-')
    try:
        latitude_val = float(latitude)
        longtitude_val = float(longitude)
        last_part_of_dow = float(res[3])
    except ValueError:
        print("Wrong value of parameter!\n"
              "Right format: 12.089")
        return
    if check_param(res[0:-1]) is False:
        return None
    datedow_val = bytes(datedow, 'utf-8')
    return [latitude_val, longtitude_val, datedow_val]


if __name__ == '__main__':
    if len(sys.argv) == 4:
        result = check_correctness(sys.argv[1], sys.argv[2], sys.argv[3])
        if result is not None:
            antigravity.geohash(result[0], result[1], result[2])
    else:
        print("usage: 12.089 (latitude), -122.085589 (longitude), 2005-05-26-10458.68 (datedow)")