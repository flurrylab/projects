import os
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from mock_llm import MockLLM, MockAgent

def get_llm(model=None, temperature=0.7):
    # Try Gemini first if key is present
    google_key = os.getenv("GOOGLE_API_KEY")
    if not google_key or google_key.startswith("your_"):
        google_key = os.getenv("GEMINI_API_KEY")
        
    if google_key and not google_key.startswith("your_") and not google_key.startswith("AIzaSy"):
        try:
            print(f"Using Gemini LLM (gemini-1.5-flash-latest)...")
            os.environ["GOOGLE_API_KEY"] = google_key
            return ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=temperature)
        except Exception as e:
            print(f"Error initializing Gemini: {e}")

    # Fallback to OpenAI
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key and not openai_key.startswith("sk-proj-svS49"):
        try:
            print(f"Using OpenAI LLM ({model or 'gpt-4o-mini'})...")
            return ChatOpenAI(model=model or "gpt-4o-mini", temperature=temperature)
        except Exception as e:
            print(f"Error initializing OpenAI: {e}")
    
    print(f"Using Mock LLM as fallback.")
    return MockLLM()

def get_agent(task, llm, browser=None):
    if isinstance(llm, MockLLM):
        return MockAgent(task, llm)
    
    try:
        from browser_use import Agent
        return Agent(task=task, llm=llm, browser=browser)
    except Exception as e:
        print(f"Error initializing real Agent: {e}. Falling back to MockAgent.")
        return MockAgent(task, llm)
