from transformers import AutoModelWithLMHead, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("tuner007/t5_abs_qa")
model = AutoModelWithLMHead.from_pretrained("tuner007/t5_abs_qa")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

def get_answer(question, context):
    input_text = "context: %s <question for context: %s </s>" % (context,question)
    features = tokenizer([input_text], return_tensors='pt')
    out = model.generate(input_ids=features['input_ids'].to(device), attention_mask=features['attention_mask'].to(device))
    return tokenizer.decode(out[0])


context = "The threat actors sent the trojanized Microsoft Word documents, probably via email. Talos discovered a document namedMinutesofMeeting-2May19.docx. Once the victim opens the document, it fetches a remove template from the actor-controlled website, hxxp://droobox[.]online:80/luncher.doc. Once the luncher.doc was downloaded, it used CVE-2017-11882, to execute code on the victim's machine. After the exploit, the file would write a series of base64-encoded PowerShell commands that acted as a stager and set up persistence by adding it to the HKCU\Software\Microsoft\Windows\CurrentVersion\Run Registry key."
question = "What is final goal of the threat actors?"
answer = get_answer(question, context)

print(answer)