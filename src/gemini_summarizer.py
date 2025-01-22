from openai import OpenAI
import os

class GeminiSummarizer:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/"
        )
    
    def summarize(self, text):
        prompt = f"""
以下の論文のアブストラクトを日本語で3-4個の箇条書きにまとめてください。
専門用語は英語のまま記載してください。

{text}
"""
        response = self.client.chat.completions.create(
            model="gemini-1.5-flash",
            messages=[
                {"role": "system", "content": "あなたは論文要約の専門家です。"},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content 