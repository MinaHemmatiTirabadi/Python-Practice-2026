
import pandas as pd

b={"Physics":[18,12,19],"Chemistry":[16.25,15,20],"Mathematics":[14,13,18],
   "Literature":[17,15,17]}
y=pd.DataFrame(b,index=["Ali","Mohammad","Reza"])
print(y)

writer=pd.ExcelWriter("py33-DataFrame-write excel.xlsx",engine="xlsxwriter")
y.to_excel(writer,sheet_name="Sheet1")
writer.close()
