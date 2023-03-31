# -*- coding: utf-8 -*-
# Author : Dimitrios Zacharopoulos
# All copyrights to Obipixel Ltd
# 09 May February 2022

#!/usr/bin/env python3

import pdfx
import json
import os


# Print ASCII art
print("""
                 __        __________________  ___________
  _____   _____/  |______ \______   \______ \ \_   _____/
 /     \_/ __ \   __\__  \ |     ___/|    |  \ |    __)  
|  Y Y  \  ___/|  |  / __ \|    |    |    `   \|     \   
|__|_|  /\___  >__| (____  /____|   /_______  /\___  /   
      \/     \/          \/                 \/     \/    
""")


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