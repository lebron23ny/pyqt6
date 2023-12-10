import docx
doc = docx.Document()
doc.add_paragraph('Здравствуй, мир!')
doc.save('helloworld.docx')
