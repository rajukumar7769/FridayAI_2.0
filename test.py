import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyBj5KoEEfFyAWprezf735DDRkMArztnHUE"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("tell me about today wheather")

print(response.text)