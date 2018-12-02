# -*- coding: utf-8 -*-  
# 功能:python连接access2010数据库(.accdb)  


#import win32com.client   


# conn = win32com.client.Dispatch(r'ADODB.Connection')   
# DSN = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=d:\mt.mdb;'   
# conn.Open(DSN)

# rs = win32com.client.Dispatch(r'ADODB.Recordset')   
# rs_name = '表1'         #表名   
# rs.Open('[' + rs_name + ']', conn, 1, 3) 

# rs.AddNew()   
# rs.Fields.Item(1).Value = 'data'   
# rs.Update() 

# conn = win32com.client.Dispatch(r'ADODB.Connection')   
# DSN = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=C:/MyDB.mdb;'   
# sql_statement = "Insert INTO [Table_Name] ([Field_1],[Field_2]) VALUES ('data1', 'data2')"   
# conn.Open(DSN)   
# conn.Execute(sql_statement)   
# conn.Close() 
 

import pypyodbc  
 
 
#以下为pypyodbc方法，自己没有办法通过调试
DBfile = r"d:\mt.mdb"  # 数据库文件
#conn = pypyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;charset='utf-8';")
conn = pypyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb,)};DBQ=" + DBfile + ";Uid=;Pwd=;charset='utf-8';")
# str = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=d:\\mt.mdb'
# conn = pyodbc.connect(str)           #win_connect_mdb(str)
# 用charset设置字符集 
  
cursor = conn.cursor()  
SQL = '''insert into 表1 (申请单位,施工单位,) values ('通知','通知公告')'''  
# 注意：在SQL语句中必须用单引号'，使用双引号"pyodbc会提示错误，整个语句可以用三引号。

cursor.execute(SQL)
conn.commit()

cursor.close()  
conn.close()  
