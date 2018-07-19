import sys

def convert_length(length):
    return int(length[0]) * 60 + int(length[1])

def sum_length(lengths):
    return sum([convert_length(l) for l in lengths])

def sec_to_min(sec):
    rem = sec % 60
    return str(int((sec - rem) / 60)) + ':' + str(int(rem))

def get_lengths():
    return [length.strip().split(':') for length in sys.argv[1].split('+')]

if len(sys.argv) > 1:
    print(sec_to_min(sum_length(get_lengths())))
