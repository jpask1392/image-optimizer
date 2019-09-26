import os
import sys
import os.path
import tinify

tinify.key = 'D4XsMGTfYX45KT96K5zrzQjgrgLW8phD'

# '-3x' - phone size image
# '-2x' - tablet size image
# '-1x' - desktop size image

# optimize full size image
def desktopConversion(filename, filetype):
    newFileName = filename + "-1x" + filetype
    source = tinify.from_file("./convert-images/" + filename + filetype)
    source.to_file("./convert-images/" + newFileName)

# optimize full size image and scale down
def tabletConversion(filename, filetype):
    newFileName = filename + "-2x" + filetype
    source = tinify.from_file("./convert-images/" + filename + filetype)
    resized = source.resize(
        method="scale",
        width=1000
    )
    resized.to_file("./convert-images/" + newFileName)

# optimize full size image and scale down
def mobileConversion(filename, filetype):
    newFileName = filename + "-3x" + filetype
    source = tinify.from_file("./convert-images/" + filename + filetype)
    resized = source.resize(
        method="scale",
        width=600
    )
    resized.to_file("./convert-images/" + newFileName)

imagesCompleted = 0 
# loop through and produce 3 images using the suffixs above
allFiles = os.listdir('./convert-images')
for file in allFiles:
    filename = file.rsplit('.')[0]
    filetype = "." + file.rsplit('.')[1]
    if file != ".DS_Store" and filetype != ".gif":
        print("Images Optimized: {} / {}".format(imagesCompleted, len(allFiles)))
        desktopConversion(filename, filetype)
        tabletConversion(filename, filetype)
        mobileConversion(filename, filetype)
        imagesCompleted += 1






