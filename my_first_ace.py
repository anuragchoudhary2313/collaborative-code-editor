from ace import ACELiteLLM

# Create agent that learns automatically (using local Ollama - 1B model for lower RAM usage)
agent = ACELiteLLM(model="ollama/llama3.2:1b")

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
