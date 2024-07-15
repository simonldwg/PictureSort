import sys
import argparse

from image_handler import Image, SortingChoice, SortingKey

parser = argparse.ArgumentParser(
    prog='ImageSort',
    description='This program sorts the pixels in an image by their red, green or blue value, or by their luminance. '
                'It can either sort each row, each column or the whole image continuously.'
)
parser.add_argument('source_image', type=str)
parser.add_argument('output_filename', type=str)
parser.add_argument('--sort', type=str, choices=['rows', 'columns', 'continuously'], default='rows')
parser.add_argument('--sort-by', type=str, choices=['red', 'green', 'blue', 'luminance'], default='luminance')

args = parser.parse_args()

# Because we are using Quicksort, the recursion will exceed the maximum recursion depth allowed by the Python
# interpreter by default. Hence, increasing it is necessary.
sys.setrecursionlimit(100000)

image = Image(args.source_image)

# We need to parse the sorting choice (rows, columns, continuously) and sorting key (red, green, blue, luminance)
# provided by the console arguments
sorting_choice = SortingChoice[args.sort.upper()]
sorting_key = SortingKey[args.sort_by.upper()]

# Now we can sort the image
image.sort(sorting_choice, sorting_key)

# And save the newly generated image
image.save(args.output_filename)
