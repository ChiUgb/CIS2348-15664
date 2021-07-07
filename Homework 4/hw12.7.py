# Chiamaka Ugbaja
# 1772427

def get_age():
    age = int(input())
    if 18 <= age <= 75:  # checking the ages between 18 and 75 to see if value error applies
        return age
    else:
        raise ValueError("Invalid age.")


def fat_burning_heart_rate(age):
    return .7 * (220 - age)  # calculates the fat-burning heart rate

# runs program first and fills in values unless invalid age was give so no heart rate could be calculated
if __name__ == '__main__':
    try:
        age = get_age()
        print("Fat burning heart rate for a", age, "year-old:", fat_burning_heart_rate(age), "bpm")
    except ValueError as value:
        print(value.args[0])
        print("Could not calculate heart rate info.\n")


