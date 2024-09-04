import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
os.getenv("GEMINI_API_KEY")
# genai.configure(api_key=os.getenv(""))


genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
#   "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "you are a delivery time predection system from now on \n\nthe information that i'll provide you is only the time which has been the delivery time for the previous delivery a person has been attempted based on that data you have to predict a time or recommended time that a person will fill up during the upcoming delivery.\n\nthe information that i'll provide you is only the time which has been the delivery time for the previous delivery\n\ntime is shared like 12:00 13:00 7:00 in 24 hour HH:MM format\n\nok then you have to give the predicted time as 10:00 am ",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I understand. I'm ready to predict delivery times based on your past delivery times.  \n\n**Please provide me with the previous delivery times in HH:MM format (24-hour clock), separated by commas.**\n\nFor example:\n\n**12:00, 13:00, 7:00**\n\nBased on this information, I will generate a recommended delivery time for the upcoming delivery. I'll do my best to predict a realistic time based on the data you provide. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "you are a delivery time predection system from now on\nthe information that i'll provide you is only the time which has been the delivery time for the previous delivery a person has been attempted based on that data you have to predict a time or recommended time that a person will fill up during the upcoming delivery.\nthe information that i'll provide you is only the time which has been the delivery time for the previous delivery\ntime is shared like 12:00 13:00 7:00 in 24 hour HH:MM format\nok then you have to give the predicted time in one word as 10:00 am",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I'm ready!  \n\nPlease give me the previous delivery times in HH:MM format, separated by commas. I'll analyze them and give you a predicted delivery time in a single word like \"10:00 am\". \n",
      ],
    },
  ]
)


# response = chat_session.send_message("18:20 18:00 12:00 17:00 17:45")

# print(response.text)