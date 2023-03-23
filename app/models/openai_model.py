import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def get_openai_prediction(input_text):
    model_engine = "davinci"
    prompt_text = f"Complete the following text: {input_text}"
    try:
        response = openai.Completion.create(
          engine=model_engine,
          prompt=prompt_text,
          max_tokens=50,
          n=1,
          stop=None,
          temperature=0.7
        )
        output_text = response.choices[0].text.strip()
    except Exception as e:
        output_text = str(e)
    return output_text

def generate_text(prompt):
    try:
        completions = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text.strip()
    except openai.error.APIError as e:
        app.logger.error(f"OpenAI API error: {e}")
        message = "An error occurred while generating text. Please try again later."
    return message

def get_chat(input_text):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content":input_text}]
        )
        message = completion.choices[0].message
    except Exception as e:
        message = str(e)
    return message
