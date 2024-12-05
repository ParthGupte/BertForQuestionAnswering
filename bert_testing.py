import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline, AutoModelForMaskedLM

# Load the pre-trained model and tokenizer
model_name = "deepset/bert-base-uncased-squad2" 
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Specify device to run inference on CUDA (GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


# Define the context for question answering
context = "The threat actors sent the trojanized Microsoft Word documents, probably via email. Talos discovered a document namedMinutesofMeeting-2May19.docx. Once the victim opens the document, it fetches a remove template from the actor-controlled website, hxxp://droobox[.]online:80/luncher.doc. Once the luncher.doc was downloaded, it used CVE-2017-11882, to execute code on the victim's machine. After the exploit, the file would write a series of base64-encoded PowerShell commands that acted as a stager and set up persistence by adding it to the HKCU\Software\Microsoft\Windows\CurrentVersion\Run Registry key."

# Define the question
question = "How was launcher.doc downloaded?"


# Print the result
# print(model.roberta)

cybert_tokenizer = AutoTokenizer.from_pretrained("markusbayer/CySecBERT")
cysecbert = AutoModelForMaskedLM.from_pretrained("markusbayer/CySecBERT")
print("CySecBERT")
# print(cysecbert)
model.roberta = cysecbert
# print(model)

# Perform question answering
classifier = pipeline('question-answering', model=model, tokenizer=cybert_tokenizer, device=0 if str(device)=="cuda" else -1)
QA_input = {'question': question, 'context': context}
result = classifier(QA_input)
print(result)
