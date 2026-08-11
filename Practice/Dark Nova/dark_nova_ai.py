import pandas as pd
import google.generativeai as genai

df = pd.read_excel("dark_nova.xlsx")
data_summary = df.to_string()

genai.configure(api_key="AIzaSyDao7w_fyOYwmwRT5oaghwcLkZoWDXzNNQ")
model = genai.GenerativeModel("gemini-1.5-flash")

question = "Which troup has the highest average Power stat?"

response = model.generate_content(
    f"Here is my Dark Nova character data:\n{data_summary}\n\nQuestion: {question}"
)

print(response.text)