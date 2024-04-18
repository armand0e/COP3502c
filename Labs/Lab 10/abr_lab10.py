def gradient(n, file=None):
    for i in range(n):
        for j in range(n):
            print((i + j) // 2, end=' ', file=file)
        print(file=file)


def square(n, file=None):
    for i in range(n):
        for j in range(n):
            print(min(i, j, n - i - 1, n - j - 1) * 2, end=" ", file=file)
        print(file=file)


def circle(n, file=None):
    for i in range(n):
        for j in range(n):
            distance = ((i - n/2) ** 2 + (j-n/2) ** 2) ** 0.5
            print(max(int(distance - n ** 0.5), 0),
                  end=" ", file=file)
        print(file=file)

def star(size, file=None):
    starlst = []
    for i in range(size):
        for j in range(size):
            distance = (size - i) // 2
            
            starlst.append()
            print()

def stripes(size, file=None):
    for i in range(size):
        for j in range(size):
            if j == 0 and i != 0:
                potential_newline = "\n"
            else:
                potential_newline = ""
            if j % 2 == 0:
                print(f"{potential_newline}0", end=" ", file=file)
            else:
                print(f"{potential_newline}{size}", end=" ", file=file)
    print(file=file)
    
def make_image(pattern, size, filename):
    if size < 100:
        size = 100
    file = open(filename, "w")
    file.write(f"P2 {size} {size} 200\n")
    file.write(str(pattern(size, file)))

def main():
    make_image(circle, 100, "circle.pgm")

if __name__ == "__main__":
    main()