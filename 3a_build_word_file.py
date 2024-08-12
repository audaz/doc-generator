# -*- coding: utf-8 -*-
import time
from docx import Document
from docx.shared import Pt, Inches, Cm, Mm
from docx.shared import RGBColor
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx2pdf import convert


import re
import os, inspect
from win32com import client
import win32com
from pathlib import Path

from docx.oxml import OxmlElement as OE
from docx.oxml.ns import qn


dbg = 0


def update_toc(docx_file):
    print(f"funcion update_toc - dispatch\n")
    word = win32com.client.DispatchEx("Word.Application")
    print(f"open        {docx_file}\n")
    doc = word.Documents.Open(f"{docx_file}")
    toc_count = doc.TablesOfContents.Count
    print(f'toc count={toc_count}')
    if int(toc_count) == 1:
        print(f"update\n")
        doc.TablesOfContents(1).Update()
    elif int(toc_count) == 1:
        print(f"Create\n")
        doc.TablesOfContents().Create()
    else:
        print('Error: não existe apenas 1 indice')
    print(f"close\n")
    doc.Close(SaveChanges=True)
    print(f"quit\n")
    word.Quit()


def create_front_page(title, directory, document):
    p = document.add_paragraph('')
    p = document.add_paragraph('')
    p = document.add_paragraph('')
    p = document.add_paragraph('')

    document.add_picture('assets\\imagem_capa.png', width=Mm(210))

    p = document.add_paragraph('')
    p = document.add_paragraph('')

    paragraph_00 = document.add_paragraph()
    logo_run = paragraph_00.add_run(title)
    logo_run.font.bold = True
    logo_run.font.size = Pt(16)
    paragraph_00.alignment = WD_ALIGN_PARAGRAPH.CENTER    

    p = document.add_paragraph('')
    p = document.add_paragraph('')

    p2 = document.add_paragraph('')
    logo_run_02 = p2.add_run()
    l_file = Path(f"{directory}\\logo.png")
    if l_file.is_file():
        logo_run_02.add_picture(f"{directory}\\logo.png", width=Inches(1.5)) 
    else:
        p = document.add_paragraph('')
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p = document.add_paragraph('')
    p = document.add_paragraph('')
    p = document.add_paragraph('')
    p = document.add_paragraph('')
    p = document.add_paragraph('')
    p  = document.add_paragraph('')

    p3 = document.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER    
    logo_run_03 = p3.add_run('www.audaztecnologia.com.br')
    logo_run_03.font.bold = True
    logo_run_03.font.size = Pt(14)

    document.add_page_break()


def create_blank_toc(doc):
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    paragraph_01 = doc.add_paragraph('SUMÁRIO')
    title_style = paragraph_01.style
    title_style.font.name = "Arial"
    title_style.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
    title_style.font.bold = True
    title_style.font.size = Pt(11)
    title_style.element.xml
    rFonts = title_style.element.rPr.rFonts
    rFonts.set(qn("w:asciiTheme"), "Arial")    

    paragraph = doc.add_paragraph()
    run = paragraph.add_run()
    fldChar = OxmlElement('w:fldChar')  # creates a new element
    fldChar.set(qn('w:fldCharType'), 'begin')  # sets attribute on element
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')  # sets attribute on element
    instrText.text = 'TOC \\o "1-4" \\h \\z \\u'   # change 1-3 depending on heading levels you need

    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'separate')
    fldChar3 = OxmlElement('w:t')
    fldChar3.text = "Right-click to update field."
    fldChar2.append(fldChar3)

    fldChar4 = OxmlElement('w:fldChar')
    fldChar4.set(qn('w:fldCharType'), 'end')

    r_element = run._r
    r_element.append(fldChar)
    r_element.append(instrText)
    r_element.append(fldChar2)
    r_element.append(fldChar4)
    p_element = paragraph._p

    doc.add_page_break()



def format_title_and_subtitles(document):
    # Set the font for the paragraphs
    document.styles['Normal'].font.name = 'Arial'
    document.styles['Normal'].font.size = Pt(10)
    document.styles['Normal'].font.bold = False
    document.styles['Normal'].font.color.rgb = RGBColor(0, 0, 0)
    document.styles['Normal'].alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # Set the font for the titles and subtitles
    document.styles['Title'].font.name = 'Arial'
    document.styles['Title'].font.size = Pt(20)
    document.styles['Title'].font.bold = True
    document.styles['Title'].font.color.rgb = RGBColor(0, 0, 0)
    document.styles['Title'].element.xml
    rFonts = document.styles['Title'].element.rPr.rFonts
    rFonts.set(qn("w:asciiTheme"), "Arial")

    document.styles['Heading 1'].font.name = 'Arial'
    document.styles['Heading 1'].font.size = Pt(12)
    document.styles['Heading 1'].font.bold = True
    document.styles['Heading 1'].font.color.rgb = RGBColor(0, 0, 0)
    document.styles['Heading 1'].element.xml
    rFonts = document.styles['Heading 1'].element.rPr.rFonts
    rFonts.set(qn("w:asciiTheme"), "Arial")    

    document.styles['Heading 2'].font.name = 'Arial'
    document.styles['Heading 2'].font.size = Pt(12)
    document.styles['Heading 2'].font.bold = True
    document.styles['Heading 2'].font.color.rgb = RGBColor(0, 0, 0)
    document.styles['Heading 2'].element.xml
    rFonts = document.styles['Heading 2'].element.rPr.rFonts
    rFonts.set(qn("w:asciiTheme"), "Arial")     

    document.styles['Heading 3'].font.name = 'Arial'
    document.styles['Heading 3'].font.size = Pt(12)
    document.styles['Heading 3'].font.bold = True
    document.styles['Heading 3'].font.color.rgb = RGBColor(0, 0, 0)
    document.styles['Heading 3'].element.xml
    rFonts = document.styles['Heading 3'].element.rPr.rFonts
    rFonts.set(qn("w:asciiTheme"), "Arial") 

    document.styles['Heading 4'].font.name = 'Arial'
    document.styles['Heading 4'].font.size = Pt(12)
    document.styles['Heading 4'].font.bold = True
    document.styles['Heading 4'].font.color.rgb = RGBColor(0, 0, 0)
    document.styles['Heading 4'].element.xml
    rFonts = document.styles['Heading 4'].element.rPr.rFonts
    rFonts.set(qn("w:asciiTheme"), "Arial")     



def add_content_direct_from_markdown(document,directory, file):
    with open(file, "r" , encoding="utf-8") as file:
        # user_message += file.read().replace("\n", "")
        content = file.read()
    paragraphs = content.split('\n')
    inside_table = False
    table_created = False
    table_columns_total = 0
    table_items = ()

    for paragraph in paragraphs:
        if dbg>0 :print(type(paragraph))
        if dbg>0: print(paragraph)

        if paragraph.startswith('!['):
            img = paragraph.replace('[','').replace(']','').replace(r'!','')
            img = img.split('(')[0]
            print(f"IMG: {img}")
            pi1 = document.add_paragraph('')
            pi1.alignment = WD_ALIGN_PARAGRAPH.CENTER            
            run_pi1 = pi1.add_run()
            run_pi1.add_picture(f'{directory}\\{img}' )
        # https://stackoverflow.com/questions/2554185/match-groups-in-python
        elif m := re.search(r'^\s*([0-9]+\.[0-9]+\.[0-9]+.*)$', paragraph):    
            print(f"REGEX_03b_{m.group(0)}")
            print(f"REGEX_03b_{m.group(1)}")
            # print(f"REGEX_03b_{m.group(2)}")
            document.add_heading(f"{m.group(1)}", level=3)
        elif m := re.search(r'^([0-9]+\.[0-9]+\.[0-9]+.*)', paragraph):    
            document.add_heading(f"{m.group(1)}", level=3)
        elif m := re.search(r'^\s*([0-9]+\.[0-9]+.*)',    paragraph):    
            document.add_heading(f"{m.group(1)}", level=2)
        elif m := re.search(r'^\s*([0-9]+\.\s+.*)',      paragraph):    
            document.add_heading(f"{m.group(1)}", level=1)
        elif m := re.search(r'^---\s*$',      paragraph):    
            print('add page break')
            document.add_page_break()
        elif m := re.search(r'^######\s(.*)',      paragraph):    
            document.add_heading(f"{m.group(1)}", level=6)
        elif m := re.search(r'^#####\s(.*)',      paragraph):    
            document.add_heading(f"{m.group(1)}", level=5)
        elif m := re.search(r'^####\s(.*)',      paragraph):    
            document.add_heading(f"{m.group(1)}", level=4)
        elif m := re.search(r'^###\s(.*)',      paragraph):    
            document.add_heading(f"{m.group(1)}", level=3)
        elif m := re.search(r'^##\s(.*)',      paragraph):    
            document.add_heading(f"{m.group(1)}", level=2)
        elif m := re.search(r'^#\s(.*)',      paragraph):    
            document.add_heading(f"{m.group(1)}", level=1)
        elif m := re.search(r'^<!--',      paragraph):    
            next
        elif m := re.search(r'^\|---+(.*)',      paragraph):    
            print('TABLE HEADER DETECTED...')
            print(f"{m.group(1)}")
            inside_table = True
            if table_created:
                print('Tabela já existe...')
            else:
                table = document.add_table(rows=1, cols=len(re.findall(r'\|', m.group(1))))
                table.style = 'Table Grid'
                table.allow_autofit = True
                table_created = True
        elif m := re.search(r'^\|(.*)',      paragraph):    
            print('TABLE DETECTED...')
            print(f"{m.group(1)}")
            inside_table = True
            table_columns_total = len(re.findall(r'\|', m.group(1)))
            if table_created:
                print('Tabela já existe...')
            else:
                table = document.add_table(rows=0, cols=table_columns_total)
                table.style = 'Table Grid'
                table.allow_autofit = True
                table_created = True
            print(f"table_columns_total:{table_columns_total}")
            print(f"col_count = {len(table.columns)}")
            row_itens = m.group(1).split('|')
            cells = table.add_row().cells
            for i in range(table_columns_total):
                print(i)
                cells[i].text = row_itens[i]
        else:
            p1 = document.add_paragraph(paragraph)
            logo_run = p1.add_run()
            p1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY               
            p1.paragraph_format.space_after = Pt(2)

def generate_content(content_file, directory, title='' , convert_to_pdf=True, create_cover=True, create_toc=True):
    script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    file_name = f"{content_file[:-3]}.docx"
    file_path = os.path.join(script_dir, f"{directory}\\{file_name}")
    print(f"\\generating file {file_path}...")

    # Create a new document
    document = Document()

    import docx 
    styles_element = document.styles.element
    rpr_default = styles_element.xpath('./w:docDefaults/w:rPrDefault/w:rPr')[0]
    lang_default = rpr_default.xpath('w:lang')[0]
    lang_default.set(docx.oxml.shared.qn('w:val'),'pt-BR')

    if create_cover :
        create_front_page(title, directory, document)

    section = document.sections[0]
    # Page A4 - https://stackoverflow.com/questions/43724030/how-to-change-page-size-to-a4-in-python-docx
    section.page_height = Mm(297)
    section.page_width = Mm(210)

    sections = document.sections
    for section in sections:
        section.top_margin = Cm(4)
        section.bottom_margin = Cm(2)
        section.left_margin = Cm(2)
        section.right_margin = Cm(2)    

    header = section.header
    pH = header.paragraphs[0]
    logo_run = pH.add_run()
    logo_run.add_picture("assets\\logo_audaz.png", width=Inches(1.5))    
    pH.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    text_run = pH.add_run()
    text_run.text = '\t' +  "__________________________________________________________________________________\n"
    text_run.style.font.color.rgb = RGBColor(58, 19, 19)

    text_rum_2 = pH.add_run()
    text_run_2 = '\t'

    if create_toc:
        create_blank_toc(document)

    format_title_and_subtitles(document)

    add_content_direct_from_markdown(document,directory,f"{directory}\\{content_file}")

    print(f"file_path: {file_path}")
    document.save(file_path)

    if create_toc:
        update_toc(file_path)

    if convert_to_pdf:
        print("convert to pdf")
        pdf_file = f"{file_path[:-5]}.pdf"
        print(f"pdf_file = {pdf_file}")
        convert(file_path, f"{pdf_file}")

def main():
    # generate_content("proposta_assembleia.md", directory='input\\ten_meetings_modelo_proposta',  title='Software como Serviço (SaaS) para assembléia digital' , 
                    #  convert_to_pdf=False, create_cover=True, create_toc=False)
    generate_content("manual.md", title='Manual para criação de novos ambientes (DevOps)', directory='input\\metatron_manual',  convert_to_pdf=False)
    # generate_content("arquitetura.md", directory='input\\metatron_arquitetura',  convert_to_pdf=True)
    # generate_content("as-built-02-ptbr.md", directory='input\\metatron_infraestrutura',  convert_to_pdf=False)
    # generate_content("esteira_ci_cd.md", directory='input\\metratron_cid',  convert_to_pdf=True)
    # generate_content("proposta_vxlan.md", directory='input\\audaz_modelo_proposta',  convert_to_pdf=True)
if __name__ == "__main__":
    main()