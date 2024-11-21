import random

def rand_key():
    keys = ["A", "Bb", "C", "C#", "Db", "D", "Eb", "D#", "E", "F", "F#", "Gb", "G", "Ab", "G#"]
    key = (random.choice(keys))

    return key

def rand_arp_position():
    strings = ["E", "A", "D"]
    string = (random.choice(strings))
    if string == "D":
        position = 1
    else:
        position = (random.randrange(1, 5,))

    key_pos = (string, position)
    
    return key_pos

def main():
    key = rand_key()
    key_pos = rand_arp_position()

    print(f"Key: {key}, String: {key_pos[0]}, Position: {key_pos[1]}")

main()
