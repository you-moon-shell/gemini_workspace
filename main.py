import os
import google.generativeai as genai
from PIL import Image

# 環境変数に GOOGLE_API_KEY が設定されていれば不要
# GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
# genai.configure(api_key=GOOGLE_API_KEY)

# 使えるモデル一覧
# for model in genai.list_models():
#   if 'generateContent' in model.supported_generation_methods:
#     print(model.name)

# テキストのみ処理可能
# gemini_pro = genai.GenerativeModel('gemini-pro')
# prompt='What is the meaning of life?'
# response = gemini_pro.generate_content(prompt)
# print(response.text)

# 画像も処理可能
gemini_pro_vision = genai.GenerativeModel('gemini-pro-vision')
images = [Image.open('images/cat_1.jpg'), Image.open('images/cat_2.jpg')]
# 与えた2つの画像の共通点を生成
response = gemini_pro_vision.generate_content(['Explain what the following images have in common.', *images])
print(response.text)
