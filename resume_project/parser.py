from pyresparser import ResumeParser
data = ResumeParser('Soham_resume.docx').get_extracted_data()
print(data)