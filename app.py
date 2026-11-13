import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

question_types = {
    "MCQs": "Generate multiple-choice questions from the given content.",
    "Short Answer": "Generate short-answer questions from the given content.",
    "Interview": "Generate interview questions from the given content.",
}


def question_generator(content, q_type):
    system_instruction = question_types[q_type]
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=content,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.4,
            max_output_tokens=2000,
        ),
    )
    return response.text


if __name__ == "__main__":
    sample_content = (
        "Photosynthesis is the process used by plants to convert light energy into chemical energy."
    )
    selected_type = "MCQs"
    print(question_generator(sample_content, selected_type))