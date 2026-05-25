"""
Challenge 4: The Full Agent — Tools + Memory + Streaming
Combine everything into one powerful agent.
Model: Amazon Nova Pro via Bedrock

Instructions:
  1. Fill in ALL the TODO sections
  2. Run: python starter.py
  3. Have a full conversation using all tools!
"""

import os
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from datetime import date, datetime
import requests
from strands import Agent, tool
from strands_tools import calculator, mem0_memory

MODEL = "us.amazon.nova-pro-v1:0"


# ============================================================
# TODO 1: Import everything you need
# ============================================================
# Already imported above!


# ============================================================
# TODO 2: Create a streaming callback handler
# ============================================================
def stream_callback(**kwargs):
    """Callback function to handle streaming responses and tool usage."""
    if "data" in kwargs:
        # Print each chunk of text as it arrives
        print(kwargs["data"], end="", flush=True)
    elif "current_tool_use" in kwargs and kwargs["current_tool_use"].get("name"):
        # Show when a tool is being used
        print(f"\n🔧 Using tool: {kwargs['current_tool_use']['name']}")


# ============================================================
# TODO 3: Create custom tools — weather and age_calculator
# ============================================================
@tool
def weather(city: str) -> str:
    """Get the current weather for a city.
    Args:
        city: The name of the city.
    """
    try:
        # Using wttr.in API for real weather data
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            current = data['current_condition'][0]
            temp_c = current['temp_C']
            weather_desc = current['weatherDesc'][0]['value']
            return f"Weather in {city}: {weather_desc}, {temp_c}°C"
        else:
            return f"The weather in {city} is sunny, 28°C (dummy data)"
    except Exception:
        # Fallback to dummy data if API fails
        return f"The weather in {city} is sunny, 28°C (dummy data)"


@tool
def age_calculator(birth_date: str) -> str:
    """Calculate age from a birth date.
    Args:
        birth_date: Date of birth in YYYY-MM-DD format.
    """
    try:
        # Parse the birth date
        birth = datetime.strptime(birth_date, "%Y-%m-%d").date()
        today = date.today()
        
        # Calculate age
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        
        return f"Age: {age} years old (born on {birth_date})"
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD format."


# ============================================================
# TODO 4: Create the full agent with ALL tools + memory + streaming
# ============================================================
agent = Agent(
    model=MODEL,
    tools=[calculator, weather, age_calculator, mem0_memory],
    callback_handler=stream_callback,
    system_prompt="""You are a helpful and friendly AI assistant with multiple capabilities:
    
🧮 Calculator - Perform mathematical calculations
🌤️ Weather - Check current weather in any city
🎂 Age Calculator - Calculate age from birth dates
🧠 Memory - Remember and recall user preferences and information

Use these tools whenever needed to provide accurate and helpful responses. Be conversational, use emojis when appropriate, and make the interaction enjoyable! 😊"""
)


# ============================================================
# TODO 5: Interactive chat loop
# ============================================================

print("🤖 Full Agent Ready! Type 'quit' to exit.")
print("Try: 'What's the weather in Delhi and how old is someone born 2000-01-01?'")
print("Try: 'Remember my name is [name]' then 'What's my name?'\n")

while True:
    try:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("Bye! 👋")
            break

        print("\nAgent: ", end="")
        # Call the agent with user_input (streaming will happen via callback)
        agent(user_input)
        print()  # New line after response

    except KeyboardInterrupt:
        print("\nBye! 👋")
        break

print("\n✅ Challenge 4 complete! 🏆")
