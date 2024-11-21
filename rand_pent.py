import random

def rand_key():
    keys = ["A", "Bb", "C", "C#", "Db", "D", "Eb", "D#", "E", "F", "F#", "Gb", "G", "Ab", "G#"]
    key = (random.choice(keys))

    return key

def rand_pent_position():
    pent_position = (random.randrange(1, 5,))

    return pent_position

def main():
    key = rand_key()
    pent_position = rand_pent_position()

    print("Key:", key, ",", "Pentatonic Position:", pent_position)

main()
