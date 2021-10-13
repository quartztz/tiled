from PIL import Image
import math
import sys

class Extender: 
    
    def __init__(self): 
    
        self.END_WIDTH = 1920
        self.END_HEIGHT = 1080

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

    def main(self, inFile, outputPath): 
        
        inputFile = inFile
        output_path = outputPath
        print(inputFile)
        final = self.extendImage(inputFile, output_path)
        final.save(f"{outputPath}/stretched.jpg")

extender = Extender()

name = sys.argv[1]

try:
    outputPath = sys.argv[2]
except: 
    outputPath = "."
    print("No output path defined, using default ./{image name}")

print(name)

print(outputPath)

extender.main(name, outputPath)