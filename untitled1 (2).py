# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1829Zbl_YchAGvwumT-UT2Xevsu3WSkKi
"""

import pandas as pd
baza={
    "FISH": ["Jo'raboyev Behruzbek", "Ibrohimov Ismidiyorbek" , 'Tolibjonov Akmaljon' , 'Tolibjonov Pahlavon', 'Rustamova Shaxlo','Abduraxmonova Nargiz' ,"Turg'unobyeva Muhtasar",'Yusubjonov Yaxyobek','Abduvohidov Yodgorbek','Mirzahamidov Jalolddin'] ,

    "Yoshi":[  '19',    '19', '13','16','18','20','17','14','12', '21'],
    "Maktabi":['32-maktab', 'kollej', 'litsey','musiqa maktab','12-maktab','34-maktab','Prezident maktabi', 'TATU','Akademik litsey','23-maktab'] ,
    "Jinsi":[ 'erkak' , 'erkak'  , 'erkak', 'erkak', 'ayol', 'ayol','ayol', 'erkak','erkak','erkak',] ,
     "Manzili": ['Namangan shaxri' ,  "Farg'ona shaxri" , ';Andijon shaxri', 'Buxoro shaxri' , 'Samarqand shaxri', 'Xorazim shaxri', 'Surxandaryo shaxri', 'Jizzax shaxri', 'Sirdaryo shaxri', 'Guliston shaxri'],
}
db=pd.DataFrame(baza)
print(db)

filtr=db[(db['Maktabi'] =='Prezident maktabi')  & (db['Jinsi']=='ayol') ]
print(filtr)