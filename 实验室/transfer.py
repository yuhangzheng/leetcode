import os
from win32com.client import Dispatch, constants, gencache

path = os.getcwd()
files = os.listdir(path)
wd = gencache.EnsureDispatch('Word.Application')
for file in files:
    print(file)
    if file.split('.')[-1] in ['docx', 'doc']:
        word_path = path + '\\' + file
        pdf_path = word_path.replace('docx', 'pdf')
        print(pdf_path)
        print(word_path)
        doc = wd.Documents.Open(word_path, ReadOnly=1)
        # doc.ExportAsFixedFormat(pdf_path, constants.wdExportFormatPDF)
        doc.ExportAsFixedFormat(pdf_path,
                                constants.wdExportFormatPDF,
                                Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
        print("{}转换完成".format(file))
wd.Quit(constants.wdDoNotSaveChanges)