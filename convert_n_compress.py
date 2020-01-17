import fnmatch
import os
import re
import sys

from PIL import Image


def compressMe(file, verbose=False):
    filepath = jpg_pwd + '/' + file
    oldsize = os.stat(filepath).st_size
    picture = Image.open(filepath)

    picture.save(compress_pwd + '/' + "Compressed_" + file, "JPEG", optimize=True, quality=85)

    newsize = os.stat(compress_pwd + '/' + "Compressed_" + file).st_size
    percent = (oldsize - newsize) / float(oldsize) * 100
    if verbose:
        print("File compressed from {0} to {1} or {2}%".format(oldsize, newsize, percent))
    return percent


verbose = False
# checks for verbose flag
if len(sys.argv) > 1:
    if sys.argv[1].lower() == "-v":
        verbose = True

#pwd = "/Users/plangle-08/Documents/GitHub/tkinter_player/100_jpg_images"           # jpeg images
pwd = "/Users/plangle-08/Documents/GitHub/tkinter_player/50_png_images"                    # small png set
jpg_pwd = "/Users/plangle-08/Documents/GitHub/tkinter_player/converted_images"         # directory for converted images
compress_pwd = "/Users/plangle-08/Documents/GitHub/tkinter_player/compressed_images"   # directory for compressed images

# ------------- FINDING FIRST FILE WITH JPEG OR PNG EXTENSION -----------------------------------------------------------
for file in os.listdir(pwd):
    if fnmatch.fnmatch(file, '*.jpg') or fnmatch.fnmatch(file, '*.png'):
        filename = os.path.splitext(file)[0]
        break
regex = r'[0-9]+$'  # regex to find the trailing digits
ending_string = re.findall(regex, filename)[0]
padding = len(ending_string)  # keeping track of prefixed 0's
loop_variable = int(ending_string)
# -----------------------------------------------------------------------------------------------------------------------

# ----------------------- JPG CONVERSION --------------------------------------------------------------------------------
while os.path.exists(pwd + '/' + file):
    img = Image.open(pwd + '/' + file)
    if file.endswith(".jpg" or "jpeg"):
        imag = img.resize((960, 540))
    else:
        imag = img.convert('RGB')  # converting to jpeg
        imag = imag.resize((960, 540))
    imag.save(jpg_pwd + '/' + file.replace(".png" or ".jpeg", ".jpg"), quality=95)
    file = file.replace((str(loop_variable)).zfill(padding), (str(loop_variable + 1)).zfill(padding))  # next image
    loop_variable += 1  # update of image no
    print("converting ", loop_variable)
print("conversion done...")
# -----------------------------------------------------------------------------------------------------------------------

# ------------------------ COMPRESSION ----------------------------------------------------------------------------------
num = 0
tot = 0
for new_file in os.listdir(jpg_pwd):
    if new_file.endswith(".jpg"):
        print("compressing ", num + 1)
        num += 1
        tot += compressMe(new_file, verbose)

print("Average Compression: %d" % (float(tot) / num))
print("Done")
# -----------------------------------------------------------------------------------------------------------------------
