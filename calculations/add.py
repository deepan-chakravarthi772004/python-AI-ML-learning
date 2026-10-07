import re

text = """"
Hi,I am Deepan.
Email   : deepan123@gmail.com
Website : https://example.com
Phone no : 8248864629
DOB : 07-07-2004
Contact me at hellodeepz77@yahoo.com
or call 7639162162"""

masked_PHnNo = re.sub(r"\d{8}(?=\d{2}\b)","********",text)
masked_Email = re.sub(r"[\w.-]+(?=@+[\w.-]+\.\w+)","********",text)

print(masked_Email)
print(masked_PHnNo)