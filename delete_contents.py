import os

plangle_path = "/Users/plangle-08/Documents/GitHub/tkinter_player"
#pinto_path = ""
root_path = plangle_path

jpg_pwd = root_path+"/converted_images"
# directory for converted images
compress_pwd = root_path+"/compressed_images"

for filename in os.listdir(jpg_pwd):
    file_path = os.path.join(jpg_pwd, filename)
    # print(file_path)
    if(file_path.endswith(".jpg" or ".png" or ".jpeg")):
        os.unlink(file_path)
print("DELETED CONVERTED_IMAGES")

for filename in os.listdir(compress_pwd):
    file_path = os.path.join(compress_pwd, filename)
    #print(file_path)
    if (file_path.endswith(".jpg" or ".png" or ".jpeg")):
        os.unlink(file_path)
print("DELETED COMPRESSED_IMAGES")
