from enum import Enum

import PIL.Image

import sort.quicksort


class Pixel:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b
        self._set_luminance()

    def __repr__(self) -> str:
        return f'R {self.r}, G {self.g}, B {self.b}, Luminance {self.luminance}'

    def _set_luminance(self) -> None:
        """
        This function sets the integer approximation of the luminance of this pixel (calculated using the average)
        """
        self.luminance = int((self.r + self.g + self.b) / 3)


class SortingChoice(Enum):
    COLUMNS = 'columns'
    ROWS = 'rows'
    CONTINUOUSLY = 'continuously'


class SortingKey(Enum):
    RED = 'r'
    GREEN = 'g'
    BLUE = 'b'
    LUMINANCE = 'luminance'


class Image:
    def __init__(self, source_image_path: str):
        self.image = PIL.Image.open(source_image_path).convert('RGB')

    def sort(self, sorting_choice: SortingChoice, sorting_key: SortingKey) -> None:
        """
        This method sorts this image. It can either sort each row, each column or sort the image continuously.
        :param sorting_choice: row, column or continuously (see SortingChoice)
        :param sorting_key: The attribute by which you want to sort, i.e. red, green, blue or luminance (see
                            SortingKey).
        """

        # Sorting each column works by rotating the image, sorting each row and then rotating it back.
        if sorting_choice == SortingChoice.COLUMNS:
            self.image = self.image.rotate(90, expand=True)

        # get pixels from this image
        pixels = self._get_pixels()

        # sort the pixels
        if sorting_choice == SortingChoice.CONTINUOUSLY:
            sort.quicksort.sort_continuously(pixels, sorting_key)
        else:
            sort.quicksort.sort_rows(pixels, sorting_key, self.image.width, self.image.height)

        # write pixels to this image
        self._set_pixels(pixels)

        if sorting_choice == SortingChoice.COLUMNS:
            self.image = self.image.rotate(-90, expand=True)

    def save(self, destination_filename: str) -> None:
        """
        Saves the image under the provided destination filename.
        :param destination_filename: The path where the image should be saved.
        """
        self.image.save(destination_filename)

    def _get_pixels(self) -> list[Pixel]:
        """
        Gets the pixels from this image.
        :return: A list of Pixel objects.
        """
        image_data = self.image.load()
        pixels: list[Pixel] = []

        for y in range(self.image.height):
            for x in range(self.image.width):
                px_tuple = image_data[x, y]
                pixels.append(Pixel(px_tuple[0], px_tuple[1], px_tuple[2]))
        return pixels

    def _set_pixels(self, pixels: list[Pixel]) -> None:
        """
        Sets the pixels for this image.
        :param pixels: A list of Pixel objects. The list has to be the exact same size as the amount of pixels in the
                       image.
        """
        for y in range(self.image.height):
            for x in range(self.image.width):
                index = y * self.image.width + x
                self.image.putpixel((x, y), (pixels[index].r, pixels[index].g, pixels[index].b))
