# metaPDF
metaPDF analyzes PDF files in the current directory and extracts their metadata using the pdfx library, a great OSINT tool.

## How the script works?

- This is a Python 3 script that analyzes PDF files in the current directory and extracts their metadata using the pdfx library.
- The script first gets the current working directory and creates a list of PDF files in that directory.
- It then prompts the user to select a PDF file from the list and analyzes the selected file using the pdfx library.
- The script extracts the metadata and any URLs in the PDF file and prints them to the console.
- It also writes the extracted metadata to a file named "metaPDF-metadata.txt" in the current directory.
- The script uses a while loop to handle user input and ensure that the user selects a valid PDF file from the list.
- It also uses exception handling to handle invalid input from the user.

## Requirements
```bash
pip3 install pdfx, json
```

## Permissions

Ensure you give the script permissions to execute. Do the following from the terminal:
```bash
sudo chmod +x metaPDF.py
```

## Example Usage
```
sudo python3 metaPDF.py
Password:

                 __        __________________  ___________
  _____   _____/  |______ \______   \______ \ \_   _____/
 /     \_/ __ \   __\__  \ |     ___/|    |  \ |    __)
|  Y Y  \  ___/|  |  / __ \|    |    |    `   \|     \
|__|_|  /\___  >__| (____  /____|   /_______  /\___  /
      \/     \/          \/                 \/     \/


PDF files in current directory:

1. metaPDF-sample1.pdf
2. metaPDF-sample2.pdf
3. metaPDF-sample3.pdf

Enter the number of the PDF file to analyze (press 0 to exit):
```

## Example script
```python
import pdfx
import json
import os

# get the current working directory
current_dir = os.getcwd()

# get a list of all the PDF files in the current directory
pdf_files = [f for f in os.listdir(current_dir) if f.endswith('.pdf')]

if not pdf_files:
    print('No PDF files found in current directory.')
else:
    # print the list of PDF files
    print('\nPDF files in current directory:\n')
    for i, file in enumerate(pdf_files):
        print(f'{i+1}. {file}')
    
    # prompt the user to select a PDF file to analyze
    while True:
        try:
            choice = input('\nEnter the number of the PDF file to analyze (press 0 to exit): ')
            if choice in ['0', 'ZERO']:
                print('Exiting...')
                break
            else:
                choice = int(choice)
                if 1 <= choice <= len(pdf_files):
                    break
                else:
                    print('Invalid choice. Please enter a number between 1 and', len(pdf_files))
        except ValueError:
            print('Invalid input. Please enter a number or "ZERO".')
    
    if choice not in ['0', 'ZERO']:
        # analyze the selected PDF file
        user_pdf = pdf_files[choice-1]
        pdf = pdfx.PDFx(user_pdf)
        print('\nAnalyzing PDF...')
        meta = pdf.get_metadata()
        url = pdf.get_references_as_dict()
        
        # print the extracted metadata
        print('\nMetadata:')
        print(json.dumps(meta, indent=4))
        
        # write the extracted metadata to a file
        with open('metaPDF-metadata.txt', 'w') as pdf_data:
            pdf_data.write('\nPDF Metadata \t')
            pdf_data.write(json.dumps(meta))
            pdf_data.write('\n')
            if len(url) == 0:
                pdf_data.close()
            else:
                for reference in url:
                    pdf_data.write(reference)
                pdf_data.close()
        
        print('\nAnalysis complete.\nResults written to metaPDF-metadata.txt')
```

## License Information

This library is released under the [Creative Commons ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/). You are welcome to use this library for commercial purposes. For attribution, we ask that when you begin to use our code, you email us with a link to the product being created and/or sold. We want bragging rights that we helped (in a very small part) to create your 9th world wonder. We would like the opportunity to feature your work on our homepage.
