import numpy
from PIL import Image

I = numpy.asarray(Image.open('road2.jpg'))
I.setflags(write=1)

for x in range(0, len(I)):
    for y in range(0, len(I[x])):
        if((I[x][y][1]<100) and I[x][y][2]<200):
            #I = numpy.delete(I, 0)
            I[x][y][1] = 0
            I[x][y][2] = 0
        else:
            I[x][y]=0,0,0
im = Image.fromarray(numpy.uint8(I))
im.save("new.jpg")
