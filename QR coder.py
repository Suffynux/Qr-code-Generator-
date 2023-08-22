
from segno import helpers
from segno import helpers\

qrcode = helpers.make_mecard(name=(input("Enter your name :")), email=(input("Enter your Email: ")), phone=(input("Enter your phone number: ")))
qrcode.designator
'5-L'
# Some params accept multiple values, like email, phone, url
qrcode = helpers.make_mecard(name='xyz', 
                             email=('xyz'),
                             phone=('xyz'))
Folder_Name = input("Enter your Folder name")
qrcode.save(Folder_Name, scale=5)