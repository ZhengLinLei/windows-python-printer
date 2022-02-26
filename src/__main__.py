
#                       GHOSTPRINT - Python - HTML to PDF
#                   
#
#                       Zheng Lin Lei - Apache 2.0
#
#
#          https://github.com/ZhengLinLei/windows-python-printer

import pdfkit # HTML to PDF
# ! Remmenber to install wkhtmltopdf 
# ../asset/wkhtmltox/README.md
#

import uuid # TMP filename

import os, win32print, win32api

from time import sleep


GHOSTSCRIPT_PATH = "../bin/gsscript/bin/gswin32.exe" # Change it if you want to extract the script in another path
GSPRINT_PATH = "../bin/gsprint/gsprint.exe" # Same process

WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe' # If you have installed the program in another route, please expecificate here
WKHTML_CONFIG = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)


class PrintFile():

    files = []
    printer = 0

    def __init__(self) -> None:

        self.printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)
        self.printer = win32print.GetDefaultPrinter()

    def addFile(self, filepath, name, options):

        self.files.append([filepath, name, options])

    def choosePrinter(self, indexNum):

        for index, printer in enumerate(self.printers):

            print(index, printer[2])

        self.printer = self.printers[indexNum][2] # GET NAME


    def printAll(self):

        if self.files:
            # Get the default or choosed printer
            printer_name = self.printer


            # Foreach the files array
            for file in self.files:
                # self.conn.printFile (printer_name, file[0], file[1], file[2] if file[2] else {})  Example in CUPS for linux devices
                win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+printer_name+'" "'+file[0]+'"', '.', 0)


            return True
        else:
            print('ERROR: Nothing to print in the List')
            return False






# Print HTML with styles
# Special for receipt thermal printer

class PrintHTML():
    
    def __init__(self, temp, options) -> None:
        
        self.PrintRoot = PrintFile()
        self.temp = temp

        defaultOptions = {
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'encoding': "UTF-8",
        }


        self.options = options if options else defaultOptions

    def convertFile(self, filename, name, option):

        pdfkit.from_file(f'{filename}.html', f'{filename}.pdf', self.options, configuration=WKHTML_CONFIG)

        self.PrintRoot.addFile(f'{filename}.pdf', name, option)



    def removeFile(self, arrFile):

        for file in arrFile:

            os.remove(file)


    def addHTML(self, text, name, option):
        
        filename = f"{self.temp}/{str(uuid.uuid4())}"

        # Add html text
        file = open(f"{filename}.html","w", encoding="utf-8")

        file.write(text)

        file.close()


        # Convert
        self.convertFile(filename, name, option)

        # Remove file
        self.removeFile([f'{filename}.html'])

    def choosePrinter(self, indexNum):

        self.PrintRoot.choosePrinter(indexNum)

    def addFile(self, filepath, name, option):

        filename = filepath.replace('.html', '')

        # Convert
        self.convertFile(filename, name, option)

    def addUrl(self, url, name, option):

        filename = f"{self.temp}/{str(uuid.uuid4())}"

        pdfkit.from_url(url, f'{filename}.pdf')

        self.PrintRoot.addFile(f'{filename}.pdf', name, option)


    def printAll(self):

        res = self.PrintRoot.printAll()

        sleep(10)
        # delete all tmp pdf file
        rFiles = [x[0] for x in self.PrintRoot.files]
        self.removeFile(rFiles)

        return res




# aa = PrintFile()

# aa.addFile('./test/test.pdf', 'Test', options = {
#     'page-height': '210mm',
#     'page-width': '80mm',
# })

#aa = PrintHTML('./tmp', options = {
#    'page-height': '210mm',
#    'page-width': '72mm',
#    'margin-right': '1mm',
#    'margin-left': '1mm',
#   'encoding': "UTF-8",
#
#})

# aa.addFile('./test/test.html', 'Test', {})

# print(aa.options)

# aa.choosePrinter(1)


#print(aa.printAll())
    

