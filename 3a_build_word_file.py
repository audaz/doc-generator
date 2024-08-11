# -*- coding: utf-8 -*-
import time
from docx import Document
from docx.shared import Pt, Inches
from docx.shared import RGBColor
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH


import os, inspect
from win32com import client

from docx.oxml import OxmlElement as OE
from docx.oxml.ns import qn
import win32com

from generate_doc_02b import *
import re

def update_toc(docx_file):
    print(f"dispatch\n")
    word = win32com.client.DispatchEx("Word.Application")
    print(f"open {docx_file}\n")
    doc = word.Documents.Open(docx_file)
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


def add_list_of_table(run):
    fldChar = OE('w:fldChar')
    fldChar.set(qn('w:fldCharType'), 'begin')
    fldChar.set(qn('w:dirty'), 'true')
    instrText = OE('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    instrText.text = 'TOC \\h \\z \\c "Table"'  #"Table" of list of table and "Figure" for list of figure
    fldChar2 = OE('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'separate')
    fldChar3 = OE('w:t')
    fldChar3.text = "Right-click to update field."
    fldChar2.append(fldChar3)
    
    fldChar4 = OE('w:fldChar')
    fldChar4.set(qn('w:fldCharType'), 'end')
    
    run._r.append(fldChar)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(fldChar4)

def create_front_page(document):
    p = document.add_paragraph('')
    p = document.add_paragraph('')
    p = document.add_paragraph('')
    p = document.add_paragraph('')

    document.add_picture('assets\\imagem_capa.png', width=Inches(7))

    p = document.add_paragraph('')
    p = document.add_paragraph('')

    # paragraph_00 = document.add_paragraph('Documentação - Infraestrutura de TI')
    paragraph_00 = document.add_paragraph()
    logo_run = paragraph_00.add_run('Documentação - Infraestrutura de TI')
    logo_run.font.bold = True
    logo_run.font.size = Pt(16)
    paragraph_00.alignment = WD_ALIGN_PARAGRAPH.CENTER    

    p = document.add_paragraph('')
    p = document.add_paragraph('')

    # title_style = paragraph_00.style
    # title_style.font.name = "Arial"
    # # title_style.font.color.rgb = RGBColor(0xffffffff, 0x00, 0x00)
    # title_style.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
    # title_style.font.bold = True
    # title_style.font.size = Pt(49)
    # title_style.element.xml
    # rFonts = title_style.element.rPr.rFonts
    # rFonts.set(qn("w:asciiTheme"), "Arial")    

    # p = document.add_picture('assets\\logo_cliente.png', width=Inches(1.25))
    p2 = document.add_paragraph('')
    logo_run_02 = p2.add_run()
    logo_run_02.add_picture("assets\\logo_cliente.png", width=Inches(1.5)) 
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p = document.add_paragraph('')
    p = document.add_paragraph('')
    p = document.add_paragraph('')
    p = document.add_paragraph('')
    p = document.add_paragraph('')
    p  = document.add_paragraph('')

    # document.add_paragraph().add_run('www.audaztecnologia.com.br').font.bold = True  # Funciona
    p3 = document.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER    
    # logo_run_03 = p3.add_run('www.audaztecnologia.com.br').font.bold = True
    logo_run_03 = p3.add_run('www.audaztecnologia.com.br')
    logo_run_03.font.bold = True
    logo_run_03.font.size = Pt(14)
    

    document.add_page_break()


def create_header(document):

    section = document.sections[0]
    header = section.header
    paragraph = header.paragraphs[0]
    paragraph.text = "Left Text\tCenter Text\tRight Text"
    paragraph.style = document.styles["Header"]

def create_toc(doc):
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    paragraph_01 = document.add_paragraph('SUMÁRIO')
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

    # document.add_page_break()



def format_title_and_subtitles(document):
    # Set the font for the paragraphs
    document.styles['Normal'].font.name = 'Arial'
    document.styles['Normal'].font.size = Pt(10)
    document.styles['Normal'].font.bold = False
    document.styles['Normal'].font.color.rgb = RGBColor(0, 0, 0)
    # title.style.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    document.styles['Normal'].alignment = WD_ALIGN_PARAGRAPH.JUSTIFY


    # Set the font for the titles and subtitles
    document.styles['Title'].font.name = 'Arial'
    document.styles['Title'].font.size = Pt(20)
    document.styles['Title'].font.bold = True
    document.styles['Title'].font.color.rgb = RGBColor(0, 0, 0)
    document.styles['Title'].element.xml
    rFonts = document.styles['Title'].element.rPr.rFonts
    rFonts.set(qn("w:asciiTheme"), "Arial")

    # document.styles['Title 1'].font.name = 'Arial'
    # document.styles['Title 1'].font.size = Pt(19)
    # document.styles['Title 1'].font.bold = True
    # document.styles['Title 1'].font.color.rgb = RGBColor(0, 0, 0)

    document.styles['Heading 1'].font.name = 'Arial'
    document.styles['Heading 1'].font.size = Pt(12)
    document.styles['Heading 1'].font.bold = True
    document.styles['Heading 1'].font.color.rgb = RGBColor(0, 0, 0)

    document.styles['Heading 2'].font.name = 'Arial'
    document.styles['Heading 2'].font.size = Pt(12)
    document.styles['Heading 2'].font.bold = True
    document.styles['Heading 2'].font.color.rgb = RGBColor(0, 0, 0)

    document.styles['Heading 3'].font.name = 'Arial'
    document.styles['Heading 3'].font.size = Pt(12)
    document.styles['Heading 3'].font.bold = True
    document.styles['Heading 3'].font.color.rgb = RGBColor(0, 0, 0)



    document.styles['Heading 4'].font.name = 'Arial'
    document.styles['Heading 4'].font.size = Pt(12)
    document.styles['Heading 4'].font.bold = True
    document.styles['Heading 4'].font.color.rgb = RGBColor(0, 0, 0)



def add_content(document):
    # Add the title
    document.add_heading('As-built Document of XCorp\'s Cloud Infrastructure', 0)

    # Add the subtitle
    document.add_paragraph('This document provides an overview of XCorp\'s cloud infrastructure, which includes Kubernetes, KEDA, NGINX Ingress Controller, AWS CloudFront, AWS S3, AWS ECR, AWS Router53, Oracle Cloud Instance, RabbitMQ, Redis for caching, MySQL Heatwave, Postgres Database, ElasticSearch for logging and APM, and PRTG.' )

    # Add a new section
    document.add_heading('1. Architecture', level=1)

    # Add a new paragraph
    document.add_paragraph('XCorp\'s cloud infrastructure is designed to be highly available, scalable, and secure. The infrastructure is built on top of AWS and Oracle Cloud, with Kubernetes serving as the container orchestration platform.')

    # Add a new section
    document.add_heading('1.1 Kubernetes', level=2)
    document.add_paragraph('Kubernetes is used to manage and orchestrate containers across multiple nodes in the cluster. The cluster consists of multiple worker nodes, each running multiple pods, which are the smallest deployable units of computing in Kubernetes.')

    # Add a new section
    document.add_heading('1.2 KEDA', level=2)
    document.add_paragraph('KEDA (Kubernetes Event-driven Autoscaling) is used to automatically scale pods based on the number of events or messages received by the pod. This allows for fine-grained control over the scaling of applications and ensures that resources are used efficiently.')

    # Add a new section
    document.add_heading('1.3 NGINX Ingress Controller', level=2)
    document.add_paragraph('NGINX Ingress Controller is used to route traffic to the appropriate pods in the cluster. It acts as a reverse proxy and load balancer, ensuring that traffic is distributed evenly across the cluster.')

    # Add a new section
    document.add_heading('1.4 AWS CloudFront', level=2)
    document.add_paragraph('AWS CloudFront is used as a content delivery network (CDN) to cache static content and serve it to users from the nearest edge location. This helps to improve the performance of the application and reduce the load on the backend servers.')

    # Add a new section
    document.add_heading('1.5 AWS S3', level=2)
    document.add_paragraph('AWS S3 is used as a storage service for static content, such as images and videos. It provides high availability and durability, and can be used to store large amounts of data at a low cost.')

    # Add a new section
    document.add_heading('1.6 AWS ECR', level=2)
    document.add_paragraph('AWS ECR (Elastic Container Registry) is used as a container registry to store and manage container images. It provides secure and scalable storage for container images, and can be used to deploy containers to the cluster.')

    # Add a new section
    document.add_heading('1.7 AWS Router53', level=3)
    document.add_paragraph('AWS Router53 is used as a DNS service to route traffic to the appropriate IP address. It provides high availability and scalability, and can be used to manage DNS records for the application.')

    # Add a new section
    document.add_heading('2 Oracle Cloud Instance', level=1)
    document.add_paragraph('Oracle Cloud Instance is used as a compute service')


def add_arquitetura(document):
    with open("arquitetura.txt", "r", encoding="utf-8") as file:
        # user_message += file.read().replace("\n", "")
        content = file.read()

    paragraphs = content.split('\n')
    for paragraph in paragraphs:
        if paragraph.startswith('<<'):
            img = paragraph.replace('<<','').replace('>>','')
            print(f"{img}")
            p1 = document.add_picture(f'assets\\{img}', width=Inches(7))
        elif paragraph.startswith('1.') or paragraph.startswith('2.') or paragraph.startswith('3.') or paragraph.startswith('4.') or paragraph.startswith('5.') or paragraph.startswith('6.') or paragraph.startswith('7.') or paragraph.startswith('8.') or paragraph.startswith('9.') or paragraph.startswith('10.') or paragraph.startswith('11.') or paragraph.startswith('12.') or paragraph.startswith('13.') or paragraph.startswith('14.') or paragraph.startswith('15.') or paragraph.startswith('16.') or paragraph.startswith('17.') or paragraph.startswith('18.') or paragraph.startswith('19.') or paragraph.startswith('20.') or paragraph.startswith('21.') or paragraph.startswith('22.') or paragraph.startswith('23.'):
            document.add_heading(paragraph, level=1)
        else:
            p1 = document.add_paragraph(paragraph)
            logo_run = p1.add_run()
            p1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY   

def add_content_direct_from_asbuilt(document,file):
    with open(file, "r" , encoding="utf-8") as file:
        # user_message += file.read().replace("\n", "")
        content = file.read()

    paragraphs = content.split('\n')
    for paragraph in paragraphs:
        print(type(paragraph))
        print(paragraph)
        if paragraph.startswith('<<'):
            img = paragraph.replace('<<','').replace('>>','')
            print(f"{img}")
            p1 = document.add_picture(f'input\\{img}', width=Inches(7))
        # https://stackoverflow.com/questions/2554185/match-groups-in-python
        elif m := re.match(r'^\s*(\d\.\d\.\d.*)', paragraph):    
            document.add_heading(f"REGEX_03_{m.group(0)}", level=3)
        elif m := re.match(r'^\s*(\d\.\d\.*)', paragraph):    
            document.add_heading(f"REGEX_02_{m.group(0)}", level=2)
        elif m := re.match(r'^(\d\.*)', paragraph):    
            document.add_heading(f"REGEX_01_{m.group(0)}", level=1)
        # elif re.match(r'^\s*(\d\.\d\.\d.*)', paragraph):    
        #     document.add_heading(f"REGEX{paragraph}", level=3)
        elif paragraph.startswith('1.') or paragraph.startswith('2.') or paragraph.startswith('3.') or paragraph.startswith('4.') or paragraph.startswith('5.') or paragraph.startswith('6.') or paragraph.startswith('7.') or paragraph.startswith('8.') or paragraph.startswith('9.') or paragraph.startswith('10.') or paragraph.startswith('11.') or paragraph.startswith('12.') or paragraph.startswith('13.') or paragraph.startswith('14.') or paragraph.startswith('15.') or paragraph.startswith('16.') or paragraph.startswith('17.') or paragraph.startswith('18.') or paragraph.startswith('19.') or paragraph.startswith('20.') or paragraph.startswith('21.') or paragraph.startswith('22.') or paragraph.startswith('23.'):
            document.add_heading(f"{paragraph}", level=2)
        else:
            p1 = document.add_paragraph(paragraph)
            logo_run = p1.add_run()
            p1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY               

def generate_content(content_file):

    # Create a new document
    document = Document()

    create_front_page(document)

    section = document.sections[0]
    header = section.header
    paragraph = header.paragraphs[0]
    logo_run = paragraph.add_run()
    logo_run.add_picture("assets\\logo_audaz.png", width=Inches(1.5))    
    paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    text_run = paragraph.add_run()
    text_run.text = '\t' +  "_____________________________________________________________________________\n"
    text_run.style.font.color.rgb = RGBColor(58, 19, 19)

    text_rum_2 = paragraph.add_run()
    text_run_2 = '\t'

    create_toc(document)
    format_title_and_subtitles(document)
    # add_content(document)
    # add_content_ia(document)
    # add_content_ia_b(document)
    # add_arquitetura(document)
    document.add_page_break()
    # add_content_direct_from_asbuilt(document,"input\\arquitetura.txt")
    # document.add_heading('4. Infraestrutura', 1)
    # add_content_direct_from_asbuilt(document,"input\\as-built-02-ptbr.txt")
    # document.add_heading('5. Esteira de CI/CD', 1)
    # add_content_direct_from_asbuilt(document,"input\\esteira_ci_cd.txt")
    # document.add_heading('6. Manual de criação de novas aplicações', 1)
    # add_content_direct_from_asbuilt(document,"input\\manual.txt")

    add_content_direct_from_asbuilt(document,f"input\\{content_file}")


    script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    file_name = '_doc6.docx'
    file_path = os.path.join(script_dir, file_name)

    document.save(file_name)
    update_toc(file_path)

def main():
    generate_content("proposta_vxlan.txt")
    # generate_content("proposta_assembleia.txt")
    # generate_content("arquitetura.txt")
    # generate_content("as-built-02-ptbr.txt")
    # generate_content("esteira_ci_cd.txt")
    # generate_content("manual.txt")
if __name__ == "__main__":
    main()