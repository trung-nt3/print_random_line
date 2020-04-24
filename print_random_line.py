#Nguyen Thanh Trung     20200422
#Using python 3.7 environment
import random, os, sys

#Make sure that CHUNK_SIZE is much larger than size of every single line.
CHUNK_SIZE = 5000 #bytes

#Handle very large input file in reasonable time
def get_random_line(file, length):
    offset = random.randint(0, length)
    file.seek(offset)
    chunk = file.read(CHUNK_SIZE)
    lines = chunk.splitlines()

    #Get the 1st line case
    if offset == 0:
        return str(lines[0]).strip()

    #Get the last line case
    if len(lines) == 1:
        file.seek(length - CHUNK_SIZE)
        chunk = file.read(CHUNK_SIZE)
        lines = chunk.splitlines()
        return str(lines[-1]).strip()

    return str(lines[1]).strip()


def get_random_line_small_file(file):
    #Storing whole file in memory approach
    #return random.choice(file.readlines())

    #Waterman's "Reservoir Algorithm" approach
    line = next(file)
    for num, aline in enumerate(file, 2):
        if random.randrange(num):
            continue
        line = aline
    return str(line).strip()


def print_random_line(path):
    try:
        length = os.stat(path).st_size
        if not length:
            print(path + ": is empty file!")
            return
        with open(path, errors='ignore') as file:
            #Assume that file with size < 100mb is small file
            if length < 100000000:
                print(get_random_line_small_file(file))
            else:
                print(get_random_line(file, length))
    except Exception as e:
        print("Error: ", str(e))


if __name__ == "__main__":
    print_random_line(sys.argv[1])
