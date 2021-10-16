from PIL import Image
import math
import os
import argparse

# CODE BY quartztz :: hosted @ github.com/quartztz/tiled
# © 13/10/2021

class Extender: 
    
    def __init__(self, size=(1920, 1080)): 
    
        self.END_WIDTH = size[0]
        self.END_HEIGHT = size[1]

    def extendImage(self, input_file, output_path): 
        
        """extends the image to the specified END_WIDTH 
        and END_HEIGHT"""

        image = Image.open(input_file)
        path = output_path

        (original_width, original_height) = image.size

        hor_repetition = math.ceil(self.END_WIDTH / original_width)
        ver_repetition = math.ceil(self.END_HEIGHT / original_height)
        
        result_width = original_width * hor_repetition
        result_height = original_height * ver_repetition
        hor_temp = Image.new('RGB', (result_width, original_height))
        result = Image.new('RGB', (result_width, result_height))

        # populate temporary horizontal buffer

        for i in range(hor_repetition):
            hor_temp.paste(im=image.copy(), box=(original_width * i, 0))
        
        # hor_temp.save(f"{path}/hor_temp.jpg")

        # populate whole buffer

        for i in range(ver_repetition): 
            result.paste(im=hor_temp, box=(0, original_height*i))
        
        # trim image to final size

        result = result.crop((0, 0, self.END_WIDTH, self.END_HEIGHT))

        return result
      
    def createDefaultPath(self, name): 
        # ret = os.path.join(os.getcwd(), name.split('/')[-1].split('.')[0])
        
        # creates as default path a folder inside of a "wallpapers" folder 
        # whose name is the name of the input file without the extension.

        ret = os.path.join(os.path.expanduser('~'), "wallpapers", name.split('/')[-1].split('.')[0])
        return ret

    def main(self, inFile, outputPath): 
        
        inputFile = inFile
        output_path = outputPath
        if not os.path.exists(output_path): 
            os.makedirs(output_path)
        final = self.extendImage(inputFile, output_path)
        final.save(f"{outputPath}/stretched.jpg")

parser = argparse.ArgumentParser(description="Extend small image file to larger size by repeating it multiple times.")

parser.add_argument('input_file', type=str)
parser.add_argument('--output_path', type=str, required=False)
parser.add_argument('--size', type=str, required=False, help="output size, formatted as (1920x1080)")

args = parser.parse_args()

name = args.input_file

# usage is defined as "python3 tiled.py input_file_path [--output_path output_path] [--size (1080x1920)]"

if args.size: 
    size = tuple([ int(x) for x in args.size.split("x") ])
    extender = Extender(size)
else: 
    extender = Extender()

if not args.output_path: 
    outputPath = extender.createDefaultPath(name)
    print(f"No output path defined, creating directory with image file name {outputPath}")
else: 
    outputPath = args.output_path

# print(name)

# print(outputPath)

# print(size)

extender.main(name, outputPath)
