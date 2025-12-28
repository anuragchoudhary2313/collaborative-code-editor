from ace import ACELiteLLM

# Create agent that learns automatically (using Groq API - latest model)
agent = ACELiteLLM(model="groq/llama-3.3-70b-versatile")

# Ask questions - it learns from each interaction
answer1 = agent.ask("What is 2+2?")
print(f"Answer: {answer1}")

answer2 = agent.ask("What is the capital of France?")
print(f"Answer: {answer2}")

# Agent now has learned strategies!
print(f"✅ Learned {len(agent.skillbook.skills())} strategies")

# Save for later
agent.save_skillbook("my_agent.json")
print("✅ Skillbook saved to my_agent.json")
