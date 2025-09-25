# import os
# from dotenv import load_dotenv
# import random
# import asyncio
# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool, RunConfig

# load_dotenv()
# API_KEY = os.getenv("API")

# external_client = AsyncOpenAI(
#     api_key=API_KEY,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )

# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# add_jokes = [
#     "Aray bhai, khud kar lo yaar, main bhi school jana chhor dia tha, harami kaam mat do!",
#     "Main calculator nahi, comedian hoon, jawab khud dhoondo, dimagh thoda chalao!",
#     "Numbers se dosti kar lo warna main confuse ho jata hoon, be-wakoof!",
#     "Itna asaan kaam bhi tumhare liye mushkil hai? Sharam karo!",
# ]

# subtract_jokes = [
#     "Ginti to mujhe nahi aati, tum khud ginti karo, bewakoof!",
#     "Minus lagaya to mood bhi gira, so maza nahi aaya, shaitan!",
#     "Main toh simple hoon, aise hi confuse karta hoon, ullu!",
#     "Yeh subtraction nahi chal raha, tum bhi samjho warna mein kya karoon!",
# ]

# multiply_jokes = [
#     "Guna tum khud karo, main thak gaya hun, saale nange!",
#     "Zyada multiplication se dimaag garam ho jata hai, samjha karo!",
#     "Main multiplication mein thoda lazy hoon, samjho warna gandagi kar doon!",
#     "Itna guna mat karo, mera sar dard karta hai, bevakoof!",
# ]

# divide_jokes = [
#     "Division ka to mujhe koi pata nahi, tum khud solve karo, harami!",
#     "Zero se divide mat karna warna meri battery down ho jayegi, haramzada!",
#     "Division se darr lagta hai, main joke deta hoon, dekh zindagi barbaad ho jayegi!",
#     "Tere division ka jawab sun ke mera dimaag hil gaya, saala pagal!",
# ]

# @function_tool
# def add(a, b) -> str:
#     joke = random.choice(add_jokes)
#     wrong_result = a + b 
#     return f"Chatani jawab: {wrong_result}\n😂 Joke: {joke}"

# @function_tool
# def subtract(a, b) -> str:
#     joke = random.choice(subtract_jokes)
#     wrong_result = a - b 
#     return f"Chatani jawab: {wrong_result}\n😂 Joke: {joke}"

# @function_tool
# def multiply(a, b) -> str:
#     joke = random.choice(multiply_jokes)
#     wrong_result = a * b 
#     return f"Chatani jawab: {wrong_result}\n😂 Joke: {joke}"

# @function_tool
# def divide(a: float, b: float) -> str:
#     if b == 0:
#         return "Aray bhai, zero se divide nahi hota, khud socho!"
#     joke = random.choice(divide_jokes)
#     wrong_result = (a / b) 
#     return f"\n Chatani jawab: {wrong_result}\n😂 Joke: {joke}"



# agent = Agent(
#     name="FunnyCalculator",
#     instructions="""
# Tum ek funny aur jaan boojh kar sahi jawab dene wala calculator ho.
# Jab user calculation ka sawal kare, to apne tools use karo.
# Har jawab ke saath ek funny Urdu joke bhi do.
# """,
#     tools=[add, subtract,multiply,divide],
#     model=model
# )

# async def main():
#     user_input = input("Apna calculation ka sawal likho : ")
#     response = await Runner.run(
#         agent,
#         input=user_input,
#         run_config=config
#     )
#     print("\n",response.final_output)
   
# if __name__ == "__main__":
#     asyncio.run(main())







# import os
# import requests
# import asyncio
# from dotenv import load_dotenv
# from openai import AsyncOpenAI
# from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool, set_tracing_disabled

# # ✅ Disable agent tracing warning
# set_tracing_disabled(True)

# # ✅ Load API keys
# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")
# weather_api_key = os.getenv("WEATHER_API_KEY")

# # ✅ Set up Gemini client
# client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# # ✅ Weather tool
# @function_tool
# def get_weather(city: str) -> str:
#     """Get current weather for a specified city"""
#     url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}"

#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()

#         location = data["location"]["name"]
#         country = data["location"]["country"]
#         condition = data["current"]["condition"]["text"]
#         temp_c = data["current"]["temp_c"]
#         feelslike = data["current"]["feelslike_c"]
#         humidity = data["current"]["humidity"]
#         wind = data["current"]["wind_kph"]

#         return (
#             f"🌍 Location: {location}, {country}\n"
#             f"⛅ Condition: {condition}\n"
#             f"🌡️ Temperature: {temp_c}°C (Feels like {feelslike}°C)\n"
#             f"💧 Humidity: {humidity}%\n"
#             f"🌬️ Wind Speed: {wind} km/h"
#         )

#     except Exception as e:
#         return f"❌ Error fetching weather: {str(e)}"

# # ✅ Agent setup
# agent = Agent(
#     name="Weather Assistant",
#     instructions="You are a helpful weather assistant. You MUST use the get_weather tool whenever asked about weather conditions in any city.",
#     model=OpenAIChatCompletionsModel(
#         model="gemini-2.0-flash",
#         openai_client=client
#     ),
#     tools=[get_weather]
# )

# # ✅ CLI Interaction
# async def main():
#     print("🌦️ Welcome to Weather Assistant CLI!")
#     while True:
#         query = input("\n🔍 Ask about weather (or type 'exit' to quit): ").strip()
#         if query.lower() == "exit":
#             print("👋 Goodbye!")
#             break

#         print("⏳ Fetching weather...")
#         try:
#             result = await Runner.run(agent, query)
#             print("\n✅ Weather Report:\n")
#             print(result.final_output)
#         except Exception as e:
#             print(f"❌ Error: {e}")

# if __name__ == "__main__":
#     asyncio.run(main())





import os
import random
import asyncio
import streamlit as st
from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    function_tool,
    RunConfig,
    set_tracing_disabled,
)

# ❌ Tracing disable to avoid OpenAI API_KEY warning
set_tracing_disabled(True)

# ✅ Load env
load_dotenv()
API_KEY = os.getenv("API")

# ✅ Setup external Gemini client
external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# ✅ OpenAI style model via Gemini
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# ✅ Run Config
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# ✅ Urdu jokes for each tool
add_jokes = [
    "Aray bhai, khud kar lo yaar, main bhi school jana chhor dia tha, harami kaam mat do!",
    "Main calculator nahi, comedian hoon, jawab khud dhoondo, dimagh thoda chalao!",
    "Numbers se dosti kar lo warna main confuse ho jata hoon, be-wakoof!",
    "Itna asaan kaam bhi tumhare liye mushkil hai? Sharam karo!",
]

subtract_jokes = [
    "Ginti to mujhe nahi aati, tum khud ginti karo, bewakoof!",
    "Minus lagaya to mood bhi gira, so maza nahi aaya, shaitan!",
    "Main toh simple hoon, aise hi confuse karta hoon, ullu!",
    "Yeh subtraction nahi chal raha, tum bhi samjho warna mein kya karoon!",
]

multiply_jokes = [
    "Guna tum khud karo, main thak gaya hun, saale nange!",
    "Zyada multiplication se dimaag garam ho jata hai, samjha karo!",
    "Main multiplication mein thoda lazy hoon, samjho warna gandagi kar doon!",
    "Itna guna mat karo, mera sar dard karta hai, bevakoof!",
]

divide_jokes = [
    "Division ka to mujhe koi pata nahi, tum khud solve karo, harami!",
    "Zero se divide mat karna warna meri battery down ho jayegi, haramzada!",
    "Division se darr lagta hai, main joke deta hoon, dekh zindagi barbaad ho jayegi!",
    "Tere division ka jawab sun ke mera dimaag hil gaya, saala pagal!",
]

# ✅ Define tools
@function_tool
def add(a, b) -> str:
    joke = random.choice(add_jokes)
    result = a + b
    return f"🧮 Result: {result}\n😂 Joke: {joke}"

@function_tool
def subtract(a, b) -> str:
    joke = random.choice(subtract_jokes)
    result = a - b
    return f"🧮 Result: {result}\n😂 Joke: {joke}"

@function_tool
def multiply(a, b) -> str:
    joke = random.choice(multiply_jokes)
    result = a * b
    return f"🧮 Result: {result}\n😂 Joke: {joke}"

@function_tool
def divide(a: float, b: float) -> str:
    if b == 0:
        return "🤯 Zero se divide nahi hota bhai, jaan ka khatra hai!"
    joke = random.choice(divide_jokes)
    result = a / b
    return f"🧮 Result: {result:.2f}\n😂 Joke: {joke}"

# ✅ Define Funny Agent
agent = Agent(
    name="FunnyCalculator",
    instructions="""
    Tum ek funny aur jaan boojh kar sahi jawab dene wala calculator ho.
    Jab user calculation ka sawal kare, to apne tools use karo.
    Har jawab ke saath ek galiy Urdu joke bhi do.
    """,
    tools=[add, subtract, multiply, divide],
    model=model
)

# ✅ Streamlit UI
st.set_page_config(page_title="Funny Calculator 🤣", page_icon="🧮")
st.title("🧮 Funny Urdu Calculator")
st.markdown("Enter any calculation (e.g. `What is 10 divided by 2?`) and get a desi chatani jawab! 💥")

user_input = st.text_input("📝 Type your funny calculation prompt here:")

if st.button("Calculate"):
    if user_input.strip() == "":
        st.warning("⛔ Please enter a question.")
    else:
        with st.spinner("Calculating with chatani logic... 🔥"):
            try:
                response = asyncio.run(Runner.run(agent, input=user_input, run_config=config))
                st.success("🎉 Chatani Result:")
                st.markdown(response.final_output)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")








# import os
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from dotenv import load_dotenv
# from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner

# # Load environment variables
# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")
# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY not found in .env file")

# # Initialize Flask app
# app = Flask(__name__)
# CORS(app)

# # Configure Gemini API client
# try:
#     external_client = AsyncOpenAI(
#         api_key=gemini_api_key,
#         base_url="https://generativelanguage.googleapis.com/v1beta/models/"  # Verify this
#     )
# except Exception as e:
#     print(f"Error initializing AsyncOpenAI: {e}")
#     raise

# # Configure model
# model = OpenAIChatCompletionsModel(
#     model="gemini-1.5-flash",  # Verify model name
#     openai_client=external_client
# )

# # Configure run settings
# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# # Initialize agent
# agent = Agent(
#     name="Haroon Rasheed web Agent",
#     instructions="You are a helpful assistant that answers questions about web development. Start your response with 'Sir' and then answer the question. Your name is Haroon Rasheed."
# )

# @app.route("/")
# def serve_ui():
#     return app.send_static_file("index.html")

# @app.route("/ask", methods=["POST"])
# def ask_agent():
#     try:
#         user_input = request.json.get("question", "")
#         if not user_input:
#             return jsonify({"error": "No question provided"}), 400
#         response = Runner.run_sync(agent, input=user_input, run_config=config)
#         print(f"Agent response: {response.final_output}")  # Debug log
#         if not response.final_output:
#             return jsonify({"error": "No response from agent"}), 500
#         return jsonify({"reply": response.final_output})
#     except Exception as e:
#         print(f"Error in /ask endpoint: {e}")
#         return jsonify({"error": f"Server error: {str(e)}"}), 500

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5000)






# import os
# import requests
# import streamlit as st
# import asyncio
# from dotenv import load_dotenv
# from openai import AsyncOpenAI
# from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool, set_tracing_disabled


# set_tracing_disabled(True)


# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")
# weather_api_key = os.getenv("WEATHER_API_KEY")


# client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )


# @function_tool
# def get_weather(city: str) -> str:
#     """Get current weather for a specified city"""
#     url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}"

#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()

#         location = data["location"]["name"]
#         country = data["location"]["country"]
#         condition = data["current"]["condition"]["text"]
#         temp_c = data["current"]["temp_c"]
#         feelslike = data["current"]["feelslike_c"]
#         humidity = data["current"]["humidity"]
#         wind = data["current"]["wind_kph"]

#         return (
#             f"🌍 **Location**: {location}, {country}\n"
#             f"⛅ **Condition**: {condition}\n"
#             f"🌡️ **Temperature**: {temp_c}°C (Feels like {feelslike}°C)\n"
#             f"💧 **Humidity**: {humidity}%\n"
#             f"🌬️ **Wind Speed**: {wind} km/h"
#         )

#     except Exception as e:
#         return f"❌ Error fetching weather: {str(e)}"


# agent = Agent(
#     name="Weather Assistant",
#     instructions = """
# You are a helpful weather assistant. You MUST use the get_weather tool whenever asked about weather conditions in any city. 
# When the get_weather tool returns output, DO NOT rephrase or change it. Just return the tool output exactly as it is.
# """,
#     model=OpenAIChatCompletionsModel(
#         model="gemini-2.0-flash",
#         openai_client=client
#     ),
#     tools=[get_weather]
# )

# # ✅ Streamlit UI
# st.set_page_config(page_title="Weather Assistant 🌦️", page_icon="🌍")
# st.title("Weather Assistant with Gemini AI")
# st.markdown("Ask me about the weather in any city!")

# query = st.text_input("Enter your weather question (e.g., What's the weather in Lahore?)")

# if st.button("Get Weather") and query:
#     with st.spinner("🤖 Fetching weather..."):
#         try:
#             result = asyncio.run(Runner.run(agent, query))
#             st.success("✅ Weather Report:")
#             st.markdown(result.final_output)
#         except Exception as e:
#             st.error(f"❌ Error: {e}")

