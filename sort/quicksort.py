def sort_continuously(pixels, sorting_key) -> None:
    """
    This function sorts a list of pixels continuously, meaning from left to right and top to bottom. Sorting is done by
    reference, hence why this function returns None.
    :param pixels: A list of Pixel objects
    :param sorting_key: The SortingKey by which you want to sort the image (red, green, blue, luminance)
    """
    _quicksort(pixels, sorting_key, 0, len(pixels) - 1)


def sort_rows(pixels, sorting_key, image_width: int, image_height: int):
    """
    This function sorts a list of pixels per row. Sorting is done by reference, hence why this function returns None.
    :param pixels: A list of Pixel objects
    :param sorting_key: The SortingKey by which you want to sort the image (red, green, blue, luminance)
    """
    for i in range(image_height):
        _quicksort(pixels, sorting_key, i * image_width, ((i + 1) * image_width - 1))


def _quicksort(pixels, sorting_key, start: int, end: int) -> None:
    """
    This function implements Quicksort for Pixels.
    :param pixels: A list of Pixels
    :param sorting_key: The SortingKey by which you want to sort (red, green, blue, luminance)
    :param start: The starting index (lower boundary)
    :param end: The end index (upper boundary)
    :return: None. Sorting is done by reference, meaning the original list is being modified.
    """
    if end <= start:
        return
    if not pixels:
        return

    pivot_index = _sort_partition(pixels, sorting_key, start, end)
    # sort the right side
    _quicksort(pixels, sorting_key, pivot_index + 1, end)
    # sort the left side
    _quicksort(pixels, sorting_key, start, pivot_index - 1)


def _sort_partition(pixels, sorting_key, start: int, end: int) -> int:
    """
    This function sorts the partition and returns the index of the pivot element.
    :param pixels: The list of pixels
    :param sorting_key: The SortingKey by which you want to sort (red, green, blue, luminance)
    :param start: The starting index (lower boundary)
    :param end: The end index (upper boundary)
    :return: The new index of the pivot element.
    """
    # This gets the value of the pivot which each element will be compared against. This implementation always chooses
    # the last element as the pivot.
    pivot_value = getattr(pixels[end], sorting_key.value)

    # i will later be the index of the pivot
    i = start - 1
    for j in range(start, end):
        # If the currently looked at element is less than the pivot, we know that it should be moved to the left side of
        # the pivot. Hence, we increment i by one and swap the current element (pixels[j]) with the element at index i.
        if getattr(pixels[j], sorting_key.value) < pivot_value:
            i += 1
            (pixels[i], pixels[j]) = (pixels[j], pixels[i])

    # i currently corresponds to the index of the last element that is smaller than the pivot (i.e. the last element
    # that should be left of the pivot). Therefore, we have to increment i by one to get the actual new index of the
    # pivot.
    i += 1
    # Lastly, we have to put the pivot in its correct place by swapping it with the element at index i.
    (pixels[end], pixels[i]) = (pixels[i], pixels[end])

    return i
