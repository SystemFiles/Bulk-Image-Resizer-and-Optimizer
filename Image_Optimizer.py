##    IMAGE OPTIMIZER    ##
##     BY: BEN SYKES     ##

#MIT License

#Copyright (c) 2017 Benjamin David Sykes

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from PIL import Image
from io import FileIO
import os

path_list = []
file_list = []
num_images = 0

def optimize(im_file_list, num_images, width, height, extention_fmt):
    '''(list of Image, int, int, int, str) -> bool
    
    Optimizes and saves images in im_file_list up to and including num_images.
    Returns True iff the optimization was successful.
    
    '''
    
    # Save image as a new file with same filename as before, but with '-optimized' at the end.
    
    size = width,height
    for i in range(num_images):
        try:
            im_resized = im_file_list[i].resize(size, Image.BILINEAR)
            
            # Check if directory exists...if not create it.
            os.chmod('/Optimized-Images/', 0777) # Force permission to create dir.
            ensure_dir('/Optimized-Images/')
            
            im_resized.save('/Optimized-Images/' + path_list[i][:-4]+'-optimized.' + extention_fmt, dpi=(72,72))
        except IOError:
            return False # Image save not successful.

    return True # Image save successful.
    

def populate_file_list(path_list):
    '''(list of str) -> NoneType
    
    Populates the file_list with image files.
    '''
    
    for path in path_list:
        im = Image.open(path)
        file_list.append(im)
        

def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

if __name__ == '__main__':
    
    print('#######################--IMAGE OPTIMIZER--################################' + "\n######################--BY:BEN SYKES--###############################")
    if str(raw_input("Would you like to A) Type in File Paths or B) import a list of file paths in a [.txt] file?")) == 'A':
        while str(raw_input("Add Image File? [Y/N]")) != 'N':
            path_list.append(str(raw_input("Enter the image Path now: ")))
            # Open each image and add it to file_list for optimzing
            populate_file_list(path_list)
    else:
        path_file = str(raw_input('Please enter the path of the text file containing the paths to each image: '))
        # Run through text file and extract paths. (Seperated by Line)
        try:
            temp_file = file(path_file, 'r')
        except IOError:
            print("Error finding File: Either DNE or input was invalid..")

        # Read file
        for line in temp_file:
            if  line[-1] != '\n':
                path_list.append(line[:len(line)])
            else:
                path_list.append(line[:len(line)-1])
            
        # Open each image and add it to file_list for optimizing
        populate_file_list(path_list)
        
    num_images = input("How many images are input? ")
    width = input("Width to save as: ")
    height = input("Height to save as: ")
    ext = raw_input("File Extention (ie: PNG, JPEG, etc): ")
    if optimize(file_list, num_images, width, height, ext) == True:
        print("Optimization Successful!")
    else:
        print("Problem Optimizing! Try again...")