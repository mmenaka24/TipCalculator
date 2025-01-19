def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollarsNumStr = d.lstrip("$")
    return float(dollarsNumStr)


def percent_to_float(p):
    percentNumStr = p.rstrip("%")
    return float(percentNumStr) / 100


main()
