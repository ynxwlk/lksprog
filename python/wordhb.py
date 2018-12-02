import win32com
from win32com.client import Dispatch, constants

num = 0
danwei = '曲靖市规划局麒麟分局'
biaodan = ''

#app='Word'  
#word=win32.gencache.EnsureDispatch('%s.Application' % app)  
word=win32com.client.Dispatch('Word.Application')
doc=word.Documents.Add()  
word.Visible=True    #False  
  
#Title begin     
sel =word.Selection    
sel.Font.Name = u"微软雅黑"  
sel.Font.Size = 24            
sel.Font.Bold = False     
sel.Font.Italic = False  
sel.Font.Underline = False  
sel.ParagraphFormat.Alignment = 1   
  
myRange = doc.Range(0,0)   
#myRange.InsertBefore(u'曲靖市规划局麒麟分局') # 使用样式   
myRange.InsertAfter( danwei ) # 使用样式     
myRange.InsertAfter( biaodan ) # 使用样式   
#Title end  
#Table Start  
sel.SetRange(12,4)  
tab = doc.Tables.Add(sel.Range, 12, 4)   
tab.Columns(1).SetWidth(4.35*6.35, 0)  
tab.Rows.Alignment = 1  
tab.Style = u"网格型"  
tabnow = doc.Tables(1)  
for num in range(0,6):
    cell1 = tabnow.Cell(num,1)
    cell2 = tabnow.Cell(num,2)
    cell3 = tabnow.Cell(num,1)  
    cell4 = tabnow.Cell(num,2)
    sel.SetRange(cell1.Range.Start, cell2.Range.End)   
    sel.Cells.Merge()
    if (num < 4):
        sel.SetRange(cell3.Range.Start, cell4.Range.End)   
        sel.Cells.Merge()   

cell1 = tabnow.Cell(4,1)
cell2 = tabnow.Cell(5,2) 
sel.SetRange(cell1.Range.Start, cell2.Range.End)   
sel.Cells.Merge()

cell1 = tabnow.Cell(4,3)
cell2 = tabnow.Cell(5,3) 
sel.SetRange(cell1.Range.Start, cell2.Range.End)   
sel.Cells.Merge()

for num in range(6,12):
    cell1 = tabnow.Cell(num,3)
    cell2 = tabnow.Cell(num,5)
    sel.SetRange(cell1.Range.Start, cell2.Range.End)   
    sel.Cells.Merge()


cell1 = tabnow.Cell(6,1)
cell2 = tabnow.Cell(11,1)
sel.SetRange(cell1.Range.Start, cell2.Range.End)   
sel.Cells.Merge()

cell1 = tabnow.Cell(12,2)
cell2 = tabnow.Cell(12,5)
sel.SetRange(cell1.Range.Start, cell2.Range.End)   
sel.Cells.Merge()
  
#myrange = doc.Range(cell1.Range.Start, cell2.Range.End)  
  
 

#doc.close()
#doc.SaveAs('12.doc')
#doc.Save()
#doc.Quit()