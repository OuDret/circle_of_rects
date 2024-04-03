import math
from PIL import Image, ImageDraw

output_file = "out.lef"
RADIUS = 25
NUM_OF_RECTANGLES = 20

if NUM_OF_RECTANGLES%2 != 0:
    print("error")
    exit(1)

DISTANCE_X = RADIUS*2/NUM_OF_RECTANGLES

image = Image.new("RGB", (RADIUS*2, RADIUS*2), color="white")

def pitagoras(c1, h):
    return math.sqrt(h**2 - c1 **2)

def draw_rectangle(x1, y1, x2, y2, image):
    draw = ImageDraw.Draw(image)
    draw.rectangle([x1, y1, x2, y2], outline='red')

def write_lef(rectangles, output_file):
    f = open(output_file, "w")
    for rect in rectangles:
        x1, x2 = rect[0]
        y1, y2 = rect[1]
        f.write(f"RECT {round(x1,2)} {round(y1,2)} {round(x2,2)} {round(y2,2)} ;\n")
    f.close()

rectangles = []

for rect in range(int(NUM_OF_RECTANGLES/2)):
    height = pitagoras((rect+1)*DISTANCE_X,RADIUS)
    rectangles.append([(rect*DISTANCE_X, (rect+1)*DISTANCE_X), (-height,height)])

# at the moment we have half circle done
other_half = rectangles.copy()
for rect in other_half:
    x1, x2 = rect[0]
    y1, y2 = rect[1]
    rectangles.append([(-x2,-x1),(y1,y2)])

for rect in rectangles:
    x1, x2 = rect[0]
    y1, y2 = rect[1]
    draw_rectangle(x1+RADIUS,y1+RADIUS,x2+RADIUS,y2+RADIUS, image)

write_lef(rectangles, output_file)

image.show()