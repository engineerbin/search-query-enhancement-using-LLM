import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models

def generate(query):
  vertexai.init(project="flash-griffin-421422", location="us-central1")
  model = GenerativeModel("gemini-1.0-pro-002")
  responses = model.generate_content(
      ["""Based on the following search query, provide the better queries example directly one by one:""" + query],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
  )
  response_texts = []
  for response in responses:
    response_texts.append(response.text)
    print(response.text, end="")
  return ' '.join(response_texts)




generation_config = {
    "max_output_tokens": 2048,
    "temperature": 1,
    "top_p": 1,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}



