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
By default, the scripts sorts each row of pixels by luminance.
#### Options
| Argument | Values | Default | Explanation |
| -------- | ------ | ------- | ----------- |
| `--sort` | `rows`, `columns`, `continuously` | `rows` | Specifies how the image will be sorted. You can sort each row, each column or sort the image continuously. |
| `--sort-by` | `red`, `green`, `blue`, `luminance` | `luminance` | Specifies which value will be the sorting key. |




