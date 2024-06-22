def convert_units(value, from_unit, to_unit):
    conversions = {
        'meters': {
            'kilometers': value / 1000,
            'centimeters': value * 100,
            'feet': value * 3.28084
        },
        'kilometers': {
            'meters': value * 1000,
            'centimeters': value * 100000,
            'feet': value * 3280.84
        },
        'centimeters': {
            'meters': value / 100,
            'kilometers': value / 100000,
            'feet': value * 0.0328084
        },
        'feet': {
            'meters': value / 3.28084,
            'kilometers': value / 3280.84,
            'centimeters': value * 30.48
        },
        'kilograms': {
            'grams': value * 1000,
            'pounds': value * 2.20462,
            'ounces': value * 35.274
        },
        'grams': {
            'kilograms': value / 1000,
            'pounds': value * 0.00220462,
            'ounces': value * 0.035274
        },
        'pounds': {
            'kilograms': value / 2.20462,
            'grams': value / 0.00220462,
            'ounces': value * 16
        },
        'ounces': {
            'kilograms': value / 35.274,
            'grams': value / 0.035274,
            'pounds': value / 16
        },
        'liters': {
            'milliliters': value * 1000,
            'gallons': value * 0.264172
        },
        'milliliters': {
            'liters': value / 1000,
            'gallons': value * 0.000264172
        },
        'gallons': {
            'liters': value / 0.264172,
            'milliliters': value / 0.000264172
        },
        'celsius': {
            'fahrenheit': (value * 9/5) + 32,
            'kelvin': value + 273.15
        },
        'fahrenheit': {
            'celsius': (value - 32) * 5/9,
            'kelvin': (value - 32) * 5/9 + 273.15
        },
        'kelvin': {
            'celsius': value - 273.15,
            'fahrenheit': (value - 273.15) * 9/5 + 32
        }
    }

    # Lookup the conversion path and handle unsupported conversions
    if from_unit in conversions and to_unit in conversions[from_unit]:
        return conversions[from_unit][to_unit]
    else:
        return "Conversion not supported"

