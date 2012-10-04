from PIL import Image
import sys
html = """<!DOCTYPE html>
<html>
<head>
<style>
body {
  background: black;  
}
#picture {
    position: absolute;
    top: 0px;
    left: 10%%;
    margin-left: -200px;
    width: 0;
    height: 0;
    box-shadow:
        %s
    ;
}
</style>
</head>
<body>
<div id="picture">
</div>
</body>
</html>"""

img = Image.open(sys.argv[1])
pix = img.load()
width, height = img.size
bsstr = "%spx %spx 3px 4px rgb(%s,%s,%s)" 
bsarr = []
for y in xrange(0, height, 3):
    for x in xrange(0, width, 3):
        r, g, b = pix[x,y]
        bsarr.append(bsstr % ( x, y, r, g, b ))

with open("pictocss.html","w") as fp:
    fp.write(html%",\n".join(bsarr))
