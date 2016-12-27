#-*-coding:gbk -*-
from PyPDF2 import PdfFileWriter, PdfFileReader
import os,copy

filename=os.listdir('./')

def two_col_to_one(filename):
    fileread=PdfFileReader(open('./'+filename,'rb'), strict=False)
    output=PdfFileWriter()
    for pageNum in range(0, fileread.getNumPages()):
        p=fileread.getPage(pageNum)
        q=copy.copy(p)
        lf = p.mediaBox.lowerLeft
        ur = p.mediaBox.upperRight

        p.mediaBox.upperRight=(ur[0]/2,ur[1])
        p.mediaBox.lowerLeft=lf
        output.addPage(p)

        q.mediaBox.upperRight = ur
        q.mediaBox.lowerLeft = (ur[0]/2,0)
        output.addPage(q)
    
    newpath = './output/' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    outputStream = file('./output/'+filename[0:-4]+'-2col.pdf', "wb")
    output.write(outputStream)
    outputStream.close()

for i in filename:
    filename= i.decode('gbk')
    print filename
    two_col_to_one(filename)