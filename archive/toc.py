from win32com import client
import win32com


def update_toc(docx_file):
    word = win32com.client.DispatchEx("Word.Application")
    # doc = word.Documents.Open(input_file_name_v2)
    print('open\n')
    doc = word.Documents.Open('c:\\Dev\\ia\\_doc2.docx')
    toc_count = doc.TablesOfContents.Count
    print(f'toc count={toc_count}')
    print('update_toc\n')
    doc.TablesOfContents(1).Update()
    print('save\n')
    doc.Close(SaveChanges=True)
    print('quit\n')
    word.Quit()

#update_toc('c:\\Dev\\ia\\_doc3.docx')



import win32com.client
import inspect, os

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

def main():
    script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    file_name = '_doc4.docx'
    file_path = os.path.join(script_dir, file_name)
    update_toc(file_path)

if __name__ == "__main__":
    main()