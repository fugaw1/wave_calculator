"""
python3
wave_calculator.py
By: fugawi
21JUL2025
Calculate wave length and shit
"""

import argparse
import sys

def wave_converter(full_meter):
    """
    Converts wave lengths to other measurements
    returns cm, feet, and inches
    """
    full_centimeter = full_meter * 100
    full_feet = full_meter * 3.28084
    full_inches = full_meter * 39.37008
    return full_centimeter, full_feet, full_inches

def freq_converter(freq, ghz_or_mhz):
    """
    Converts mhz and ghz to hz
    returns hz frequency
    """
    if ghz_or_mhz:
        new_freq= freq * 1000000
        freq_type="Mhz"
    else:
        new_freq = freq * 1000000000
        freq_type="Ghz"
    return new_freq, freq_type

def wave_calculator(meter_wave):
    """
    Takes in wavelength in meters and converts to frequency
    returns frequency in hertz
    """
    freq_hz = 299792458 / meter_wave
    return freq_hz

def freq_calculator(freq_in_hz):
    """
    Takes in frequency in hertz
    returns: full wave length in meters
    """
    full_meters = 299792458 / freq_in_hz
    return full_meters

def meter_lengther(og_length, length_type):
    """
    Made because pylinter didn't like how long main was
    returns meter_length
    """
    print(length_type)
    if length_type == "Meters":
        return og_length
    if length_type == "Centimeters":
        return og_length / 100
    if length_type == "Feet":
        return og_length * 0.3048
    if length_type == "Inches":
        return og_length * 0.0254
    return "Something is fucky"

def wave_printer(og_freq, freq_type, full_list):
    """
    Shits out all the different possible wants for wavelength
    returns nothing, just prints
    """
    wave_type = ["Meters", "Centimeters", "Feet", "Inches"]
    cuts = ["Full", "Half", "Quarter"]
    calc = [1, .5, .25]
    print(f"Your Frequency:\t{og_freq} {freq_type}")
    # Double for loop with all these lists seemed like the
    # fastest way to iterate and add additional options in the future
    for x in range (0,4,1):
        for y in range (0,3,1):
            wave_print = full_list[x] * calc[y]
            print(f"{wave_type[x]} {cuts[y]}: \t {wave_print}")

def freq_printer(length_type, og_length, hz_freq):
    """
    Prints frequency in Hz, Mhz, and Ghz
    returns nothing, just prints
    """
    freq_nums = [1, 1000000, 1000000000]
    freq_names = ["Hz", "Mhz", "Ghz"]
    # List iteration in for loop again
    for thing in range(0,3,1):
        freq = hz_freq / freq_nums[thing]
        print(f"{length_type} {og_length}: \t {freq}{freq_names[thing]}")


def main():
    '''
    Let's start here.
    '''
    parser = argparse.ArgumentParser(
            prog='wave_calculator.py',
            description="""
            Convert your frequency to wavelngth,
            or your wavelength to frequency.
            """,
            )
    parser.add_argument('-G', '--Ghz', type=float,
                        help="Input freqency is in Ghz.", required=False)
    parser.add_argument('-M', '--Mhz', type=float,
                        help="Input frequency is in Mhz.", required=False)
    parser.add_argument('-H', '--Hz', type=float,
                        help="Input frequency is in Hz.", required=False)
    parser.add_argument('-c', '--centimeters', type=float,
                        help="Input wavelength is in centimeters.", required=False)
    parser.add_argument('-i', '--inches', type=float,
                        help="Input wavelength is in inches.", required=False)
    parser.add_argument('-m', '--meters', type=float,
                        help="Input wavelength is in meters.", required=False)
    parser.add_argument('-f', '--feet', type=float,
                        help="Input wavelength is in feet.", required=False)

    args = parser.parse_args()

    hz_freq=0
    og_freq=0
    freq_type=""
    if args.Hz or args.Mhz or args.Ghz:
        if args.Hz:
            og_freq = args.Hz
            freq_type = "Hz"
            hz_freq = args.Hz
        if args.Mhz:
            og_freq = args.Mhz
            hz_freq, freq_type = freq_converter(args.Mhz,True)
        if args.Ghz:
            og_freq = args.Ghz
            hz_freq, freq_type = freq_converter(args.Ghz,False)

        full_meter = freq_calculator(hz_freq)
        full_centimeter, full_feet, full_inches = wave_converter(full_meter)
        full_list = [full_meter, full_centimeter, full_feet, full_inches]
        wave_printer(og_freq, freq_type, full_list)
        sys.exit()

    meter_length=0
    length_type=""
    og_length=0
    if args.meters or args.inches or args.centimeters or args.feet:
        if args.meters:
            length_type = "Meters"
            og_length = args.meters
        if args.centimeters:
            length_type = "Centimeters"
            og_length = args.centimeters
        if args.feet:
            length_type = "Feet"
            og_length = args.feet
        if args.inches:
            length_type = "Inches"
            og_length = args.inches

        meter_length = meter_lengther(og_length, length_type)
        print(meter_length)
        hz_freq = wave_calculator(meter_length)
        freq_printer(length_type, og_length, hz_freq)
        sys.exit()
parser.print_help()
sys.exit()
try:
    main()
except KeyboardInterrupt:
    sys.exit()
