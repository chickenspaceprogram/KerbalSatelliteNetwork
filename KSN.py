import math


version = '0.1'
print(f"\nWelcome to Kerbal Satellite Networks v{version}!\nThis program helps you create satellite networks in Kerbal Space Program.\n")

bodiesInfo = {
    'kerbol': {
        'gm': 1.172 * 10 ** 18,
        'minsafeorbit': 262200000,
        'radius' : 261600000
    },
    'moho': {
        'gm': 1.686 * 10 ** 11,
        'minsafeorbit': 257000,
        'radius' : 250000
    },
    'eve': {
        'gm': 8.172 * 10 ** 12,
        'minsafeorbit': 790000,
        'radius' : 700000
    },
    'gilly': {
        'gm': 8.289 * 10 ** 6,
        'minsafeorbit': 20000,
        'radius' : 13000
    },
    'kerbin': {
        'gm': 3.532 * 10 ** 12,
        'minsafeorbit': 670000,
        'radius' : 600000
    },
    'mun': {
        'gm': 6.514 * 10 ** 10,
        'minsafeorbit': 207500,
        'radius' : 200000
    },
    'minmus': {
        'gm': 1.766 * 10 ** 9,
        'minsafeorbit': 66000,
        'radius' : 60000
    },
    'duna': {
        'gm': 3.014 * 10 ** 11,
        'minsafeorbit': 370000,
        'radius' : 320000
    },
    'ike': {
        'gm': 1.857 * 10 ** 10,
        'minsafeorbit': 143000,
        'radius' : 130000
    },
    'dres': {
        'gm': 2.148 * 10 ** 10,
        'minsafeorbit': 144000,
        'radius' : 138000
    },
    'jool': {
        'gm': 2.825 * 10 ** 14,
        'minsafeorbit': 6200000,
        'radius' : 6000000
    },
    'laythe': {
        'gm': 1.962 * 10 ** 12,
        'minsafeorbit': 550000,
        'radius' : 500000
    },
    'vall': {
        'gm': 2.075 * 10 ** 11,
        'minsafeorbit': 308000,
        'radius' : 300000
    },
    'tylo': {
        'gm': 2.825 * 10 ** 12,
        'minsafeorbit': 613000,
        'radius' : 600000
    },
    'bop': {
        'gm': 2.487 * 10 ** 9,
        'minsafeorbit': 87000,
        'radius' : 65000
    },
    'pol': {
        'gm': 7.217 * 10 ** 8,
        'minsafeorbit': 49000,
        'radius' : 44000
    },
    'eeloo': {
        'gm': 7.441 * 10 ** 10,
        'minsafeorbit': 214000,
        'radius' : 210000
    },
    'custom': {
        'gm': 0,
        'minsafeorbit': 0,
        'radius' : 0
    }}

dictSelectDefaultString = 'Please select an option by entering the corresponding key.'
def dictSelect(menuDict: dict, infoMessage: str=dictSelectDefaultString, showKeys: bool=True, valuesHaveInfo: bool=True):
    print(infoMessage)
    if showKeys:
        for key in menuDict:
            if valuesHaveInfo:
                value = f" : {menuDict[key]}"
            else:
                value = ''
            print(f"{key}{value}")
    selection = input().lower()
    while selection not in menuDict:
        if selection == 'keys':
            print("Displaying possible selections.\n")
            for key in menuDict:
                if valuesHaveInfo:
                    value = f" : {menuDict[key]}"
                else:
                    value = ''
                print(f"{key}{value}")
            print()
        else:
            print("Your selection was invalid. Please try again. If you'd like to see the possible selections again, enter 'keys'. If you'd like to enter custom data for a body, enter 'custom'.")
        selection = input().lower()
    return selection

body = dictSelect(bodiesInfo, "To start, enter the name of the body you want your satellite network to orbit.", False, False)
if body == 'custom':
    bodiesInfo['custom']['gm'] = float(input("Please enter the standard gravitational parameter for the body (equal to G * M). "))
    bodiesInfo['custom']['radius'] = float(input("Please enter the radius of the body. "))
    bodiesInfo['custom']['minsafeorbit'] = bodiesInfo['custom']['radius'] + float(input("Please enter the altitude of the minimum safe orbit on the body (the height of the tallest mountain or the atmosphere). "))

numSats = int(input("Please enter the numnber of satellites you want in the constellation. If the number is less than 3, 3 satellites will be used instead. "))
if numSats < 3:
    numSats = 3

orbitSelectDict = {
    'min' : 'Uses an orbit with the minimum safe radius possible.',
    'select' : 'Allows you to select the altitude of an orbit you want to use.'
}
orbitSelection = dictSelect(orbitSelectDict, "Do you want to automatically select the lowest possible orbit, or do you want to use your own orbit?")
if orbitSelection == 'min':
    finalSMA = bodiesInfo[body]['minsafeorbit'] / math.cos(math.pi / numSats)
else:
    finalSMA = float(input("Please enter the height of the orbit you want to use in meters (the orbit is assumed to be circular). ")) + bodiesInfo[body]['radius']

periodMult = (numSats + 1) / numSats
finalPeriod = 2 * math.pi * math.sqrt((finalSMA ** 3) / bodiesInfo[body]['gm'])
transferPeriod = finalPeriod * periodMult
transferSMA = (((transferPeriod ** 2) * bodiesInfo[body]['gm']) / (4 * math.pi ** 2)) ** (1 / 3)
transferPeriapsis = finalSMA - bodiesInfo[body]['radius']
transferApoapsis = 2 * transferSMA - finalSMA - bodiesInfo[body]['radius']
finalOrbitHeight = finalSMA - bodiesInfo[body]['radius']

print("\nTransfer orbit characteristics:\n\n", f"Period: {int(transferPeriod // 60)}m {round(transferPeriod % 60, 3)}s\n", f"Apoapsis: {round(transferApoapsis, 1)}m\n", f"Periapsis: {round(transferPeriapsis, 1)}m\n", f"Semi-major axis: {round(transferSMA, 1)}m")
print("\nFinal orbit characteristics:\n\n", f"Period: {int(finalPeriod // 60)}m {round(finalPeriod % 60, 3)}s\n", f"Apoapsis: {round(finalOrbitHeight, 1)}m\n", f"Periapsis: {round(finalOrbitHeight, 1)}m\n", f"Semi-major axis: {round(finalSMA, 1)}m")