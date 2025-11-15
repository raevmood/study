import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

class LLMProvider:
  def __init__(self):
    #API key self check
    try:
      gemini_api_key = os.getenv("GOOGLE_API_KEY")
      if not gemini_api_key:
        print("Gemini API Key not set. Lock in twin 💀💔")
    except Exception as e:
      print(f"Error: {e}")
    try:
      groq_api_key = os.getenv("GROQ_API_KEY")
      if not groq_api_key:
        print("Groq API Key not set. Lock in twin 💀💔")
    except Exception as e:
      print(f"Error: {e}")

    # Model Initialisation for langchain Gemini and groq wrappers
    try:
        try:
          backup_model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=gemini_api_key,
            temperature=0.7,
            max_output_tokens=2048
          )
        except Exception as e:
          print(f"Error with main model initialisation. Tf did you do fn 😭? {e}")
        try:
          main_model = ChatGroq(
            model="llama-3.1-8b-instant",
            groq_api_key=groq_api_key,
            temperature=0.7,
            max_tokens=2048
          )
        except Exception as e:
          print(f"Error with backup model initialisation. How did you mess up this hard bro😭? {e}")
    except Exception as e:
      print(f"Total model initialisation failure. Pack it up twin🥀. {e}")
    # Class variable globalisation
    self.main_model=main_model
    self.backup_model=backup_model
    
  def generate(self, prompt):
    try:
      response = self.main_model.invoke(prompt)
      print("Using main llm. Rare Karanja W")
      print(response)
    except Exception as e: 
      print(f"Inference Error. Can't even talk to an LLM smh. Attempting vibe with backup {e}")
      try:
        response = self.backup_model.invoke(prompt)
        print("Using backup llm. As expected. Go sleep nyigguh")
        print(response)
      except Exception as e:
        print(f"Total inference failure. Check ur code lil bro😔. {e}")
  
if __name__ == "__main__":
  llm = LLMProvider()
  issue = "What is the moon? Answer in about 50 words."
  llm.generate(issue)


