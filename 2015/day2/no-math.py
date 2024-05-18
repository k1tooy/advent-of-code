import sys

def surface_area(path: str) -> None:
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
        total = 0
        for line in data:
            x,y,z = map(int, line.split('x'))
            surface = 2 * (x*y + y*z + z*x)
            slack = min(x*y,y*z,x*z)
            paper = surface + slack
            total += paper
        print(total)
def ribbon(path: str) -> None:
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
        total = 0
        for line in data:
            x,y,z = map(int, line.split('x'))
            ribbon_wrap = 2 * min(x+y, y+z, x+z)
            ribbon_bow = x*y*z
            ribbon = ribbon_wrap + ribbon_bow
            total += ribbon
        print(total)
    

if __name__ == '__main__':
    n = int(sys.argv[1])
    path = str(sys.argv[2])

    if n == 1:
        surface_area(path)
    if n == 2:
        ribbon(path)


