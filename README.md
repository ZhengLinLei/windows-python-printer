# Windows Python Printer Software

UNIX (MacOS, Linux) users [https://github.com/ZhengLinLei/cups-python-printer](https://github.com/ZhengLinLei/cups-python-printer)

## Installation

Clone the project and:

    1. Extract the two requirement project in `./asset/`. (gsprint, gsscript)
    2. Install the executable [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html) in `./asset`

## Configuration

Change the routes lines to your extraction path and change **wkhtmltopdf** installation path

`./src/__main__.py  [line:22-26]`
```python
GHOSTSCRIPT_PATH = "../bin/gsscript/bin/gswin32.exe" # Change it if you want to extract the script in another path
GSPRINT_PATH = "../bin/gsprint/gsprint.exe" # Same process

WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe' # If you have installed the program in another route, please expecificate here
WKHTML_CONFIG = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
```

Import the source code to your project, and read the examples.
```python

# aa = PrintFile()

# aa.addFile('./test/test.pdf', 'Test', options = {
#      'page-height': '210mm',
#      'page-width': '80mm',
# })

aa = PrintHTML('./tmp', options = {
    'page-height': '210mm',
    'page-width': '72mm',
    'margin-right': '1mm',
    'margin-left': '1mm',
   'encoding': "UTF-8",

})

aa.addFile('./test/test.html', 'Test', {})

print(aa.options)

aa.choosePrinter(0)


print(aa.printAll())
```
