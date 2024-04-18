def triangle(size, file=None):
    center = size // 2 
    for i in range(size):
        for j in range(size):
            # top right
            if j > center:
                value = size - (size - i + j) // 2 - 1
            # top left
            if j <= center:
                value = (i + j) // 2 
            value = max(int((value*2 - size ** 0.5)),0)
            if value > size:
                value = size    
            print(value, end=" ", file=file)
        print(file=file)  
        
def diagonal(size, file=None):
    for i in range(size):
        for j in range(size):
            distance = int(((i - i)**2 + (j - i)**2)**0.5)
            value = max(int((distance*1.5 - size ** 0.5)),0)
            if value > size:
                value = size
            value = size - value
            print(value, end=" ", file=file)
        print(file=file)
        
def star(size, file=None):                
    for i in range(size):
        for j in range(size):
            center = size // 2            

            if i < center:
                # top right
                if j > center:
                    value = size - (size - i + j) // 2 - 1
                # top left
                if j < center:
                    value = (i + j) // 2
            if i > center:
                # bottom right
                if j > center:
                    value = size - (i + j) // 2 - 1
                #bottom left
                if j < center:
                    value = (size - i + j) // 2
            if i == center or j == center:
                value = (i+j)//2
                if j > center:
                    value = size - (i+j)//2 - 1
                if i > center:
                    value = size - (i+j)//2 - 1
            if value == center:
                value -= 1
            value = max(int((value - size ** 0.5)),0)
            if value > size:
                value = size    
            print(value, end=" ", file=file)  
        print(file=file)
    
def make_image(pattern, size, filename):
    if size < 100:
        size = 100
    file = open(filename, "w")
    file.write(f"P2 {size} {size} 200\n")
    file.write(str(pattern(size, file)))

def main():
    triangle(25)
    make_image(triangle, 100, "triangle.pgm")

if __name__ == "__main__":
    main()