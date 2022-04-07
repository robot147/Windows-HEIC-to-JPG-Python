#HEIC to JPG image format batch conversion script for Python 3. Tested on Windows 10.
#You will need to have ImageMagick installed: https://www.imagemagick.org/

import os, subprocess

directory = "D:\test\heic"

for filename in os.listdir(directory):
    if filename.lower().endswith(".heic"):
        print('Converting %s' % os.path.join(directory, filename))
        subprocess.run(["magick", "%s" % os.path.join(directory, filename), "%s" % os.path.join(directory, filename[0:-5] + '.jpg')])
