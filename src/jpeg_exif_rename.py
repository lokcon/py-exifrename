import PIL.Image
import os
from time import strptime, strftime

for dirpath, dirnames, filenames in os.walk('./'):
    for filename in filenames:        
        try:
            img = PIL.Image.open(filename)
        except IOError:            
            pass # the file is not an image
        else:
            # extract exif date
            exif_data = img._getexif()
            date_taken = exif_data[36867] #36867 is the tag for generated time
            
            # Construct the filename components            
            filename_prefix = "IMG_"
            
            struct_date_taken = strptime(date_taken, "%Y:%m:%d %H:%M:%S")
            filename_date = strftime("%Y%m%d_%H%M%S", struct_date_taken)
            
            filename_extension = filename.split('.')[-1]            
            
            # Assemble the new filename
            new_filename = "%s%s.%s" % \
                (filename_prefix, filename_date, filename_extension)
            
            # rename the file on the filesystem
            os.rename(filename, new_filename)
            
            print('Renamed: %s to %s' % (filename, new_filename))
            
