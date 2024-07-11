import torch
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# classifier = pipeline('sentiment-analysis',device="cuda")
# print(classifier("I like to get it in the behind!"))

model_name = "deepset/roberta-base-squad2" 
# model = AutoModelForSequenceClassification.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline('question-answering', model=model_name, tokenizer=model_name,device="cuda")
QA_input = {'question':"What condition is needed to perform action 'PowerShell commands that acted as a stager'?",'context':"The threat actors sent the trojanized Microsoft Word documents, probably via email. Talos discovered a document namedMinutesofMeeting-2May19.docx. Once the victim opens the document, it fetches a remove template from the actor-controlled website, hxxp://droobox[.]online:80/luncher.doc. Once the luncher.doc was downloaded, it used CVE-2017-11882, to execute code on the victim's machine. After the exploit, the file would write a series of base64-encoded PowerShell commands that acted as a stager and set up persistence by adding it to the HKCU\Software\Microsoft\Windows\CurrentVersion\Run Registry key."}
print(classifier(QA_input))
# print(model)