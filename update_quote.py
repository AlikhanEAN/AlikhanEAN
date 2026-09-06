import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

prompt = "Dasturchilar uchun o'zbek tilida bitta juda qisqa, qiziqarli yoki motivatsion maslahat yoz (maksimal 2 ta gap). Hech qanday kirish so'zsiz, faqat maslahat matnining o'zi bo'lsin."
response = model.generate_content(prompt)
quote = response.text.strip()

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start_tag = "<!-- GEMINI_QUOTE_START -->"
end_tag = "<!-- GEMINI_QUOTE_END -->"

new_section = f"{start_tag}\n> 💡 **Kunning maslahati:** {quote}\n{end_tag}"

if start_tag in content and end_tag in content:
    parts = content.split(start_tag)
    after_end = parts[1].split(end_tag)[1]
    new_content = parts[0] + new_section + after_end
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
