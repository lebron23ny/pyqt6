from spire.doc import *
outputFile = "Formula.docx"

latexMathFormula = "x^{2}"

doc = Document()
section = doc.AddSection()
textPara = section.AddParagraph()
textPara.AppendText("Creating Equations from LaTeX Code")
textPara.ApplyStyle(BuiltinStyle.Heading1)
textPara.Format.HorizontalAlignment = HorizontalAlignment.Center

officeMath = OfficeMath(doc)
officeMath.FromLatexMathCode(latexMathFormula)
paragraph = section.AddParagraph()
paragraph.Items.Add(officeMath)
section.AddParagraph()

doc.SaveToFile(outputFile, FileFormat.Docx)
doc.Close()