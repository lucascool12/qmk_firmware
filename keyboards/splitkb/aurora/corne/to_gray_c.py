from PIL import Image
from statistics import mean
import sys
import os

for file_name in sys.argv[1:]:
    # print(file_name, file=sys.stderr)
    with Image.open(file_name) as im:
        # im = im.rotate(90, expand=True)
        # px = im.load()
        print(im, file=sys.stderr)
        name, _ = os.path.splitext(os.path.split(file_name)[1])
        print(f"char {name}[] = {{")
        for i in range(im.width):
            for j in range(im.height):
                val = (mean(im.getpixel((i, j))))
                # if i + 1 < im.width:
                    # val += (mean(px[i + 1, j])) >> 4
                print("%3d, " % val, end="")
            print()
        print("};")
