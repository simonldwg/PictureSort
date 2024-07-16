# PictureSort
This is a Python script that sorts the pixels in an image. It implements Quicksort as its sorting algorithm. I wrote it
as part of my algorithm class in university. The program requires a recent version of Python 3.

## Getting started
1. Create a new environment using _venv_:
   ```shell
   python -m venv venv
   ```
2. Activate the environment:<br>
   Linux:
   ```shell
   source venv/bin/activate
   ```
   Windows (PowerShell)
   ```powershell
   .\venv\Scripts\activate.ps1
   ```
3. Install requirements:
   ```shell
   pip install -r requirements.txt
   ```

### Usage
To use this script, you have to provide it with a source and destination filename:
```shell
python main.py source_file.jpg destination_file.jpg
```
By default, the scripts sorts each row of pixels by luminance. The script has been verified to work with JPEG and PNG.
For a list of supported file formats, take a look at the [Pillow image library wiki.](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html)
Please note: Sorting a high-resolution image can take a long time, especially sorting it continuously.
#### Examples
The original image:<br>
![The original example image](https://github.com/simonldwg/PictureSort/blob/main/images/example-original.jpg?raw=true)<br>
Each row sorted by luminance:<br>
![Each row sorted by luminance](https://github.com/simonldwg/PictureSort/blob/main/images/example-rows.jpg?raw=true)<br>
Each column sorted by luminance:<br>
![Each column sorted by luminance](https://github.com/simonldwg/PictureSort/blob/main/images/example-columns.jpg?raw=true)<br>
The whole image sorted by luminance continuously:<br>
![The whole image sorted by luminance continuously](https://github.com/simonldwg/PictureSort/blob/main/images/example-continuous.jpg?raw=true)<br>
Each row sorted by the red value:<br>
![Each row sorted by the red value](https://github.com/simonldwg/PictureSort/blob/main/images/example-rows-red.jpg?raw=true)<br>
#### Options
| Argument | Values | Default | Explanation |
| -------- | ------ | ------- | ----------- |
| `--sort` | `rows`, `columns`, `continuously` | `rows` | Specifies how the image will be sorted. You can sort each row, each column or sort the image continuously. |
| `--sort-by` | `red`, `green`, `blue`, `luminance` | `luminance` | Specifies which value will be the sorting key. |



