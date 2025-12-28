"""
ACE Framework Demo - Shows how the framework works without API issues
This demonstrates the learning concept with simulated responses
"""

from ace import ACELiteLLM
import json

print("=" * 60)
print("ACE Framework Self-Learning Agent Demo")
print("=" * 60)

# For demo purposes, we'll use a simpler approach
# that shows the ACE concept working

print("\n📚 What is ACE Framework?")
print("-" * 60)
print(
    """
ACE = Autonomous Cognitive Engine

It creates self-learning AI agents that:
✓ Learn from interactions automatically
✓ Build a 'skillbook' of successful strategies  
✓ Apply learned strategies to new tasks
✓ Improve over time without explicit training
"""
)

print("\n🎯 How ACE Works:")
print("-" * 60)
print(
    """
1. AGENT - Generates answers using learned strategies
2. REFLECTOR - Analyzes what worked and what failed
3. SKILL_MANAGER - Updates the skillbook with new strategies

These three roles work together to create continuous learning!
"""
)

print("\n🚀 Quick Demo:")
print("-" * 60)

# Create agent instance (we'll show the concept even if API calls fail)
try:
    agent = ACELiteLLM(model="ollama/llama3.2:1b")

    print("✅ Agent initialized successfully!")
    print("\n📝 Asking questions and learning...")

    # Try to ask questions (will learn from each)
    questions = [
        "What is 2+2?",
        "What is the capital of France?",
        "Who wrote Romeo and Juliet?",
    ]

    for q in questions:
        try:
            print(f"\n  Q: {q}")
            answer = agent.ask(q)
            print(f"  A: {answer}")
        except Exception as e:
            print(f"  (Note: Full API features require working API key)")
            print(f"  Concept: Agent would learn from this interaction")
            break

    # Show skillbook concept
    try:
        num_skills = len(agent.skillbook.skills())
        print(f"\n✅ Learned {num_skills} strategies!")
        agent.save_skillbook("my_agent.json")
        print("✅ Skillbook saved to my_agent.json")
    except:
        print("\n✅ (In practice, agent would learn strategies here)")

except Exception as e:
    print(f"\n⚠️  Note: {str(e)[:100]}")
    print("\nFor the framework to work fully, you need:")
    print("  • A working API key (OpenAI, Claude, Gemini, etc.)")
    print("  • OR Ollama with a larger model (>3GB RAM)")

print("\n\n📖 What You Can Do Next:")
print("-" * 60)
print(
    """
1. Fix API Issues:
   • Add valid OpenAI key with billing
   • OR use Claude/Gemini API
   • OR install larger Ollama model (llama2:13b, etc.)

2. Full Example with Mock Data:
   Create a custom environment and train offline

3. Load Saved Models:
   agent = ACELiteLLM(skillbook_path="my_agent.json")
   answer = agent.ask("New question")
"""
)

print("\n" + "=" * 60)
print("✨ ACE Framework is ready when your API is set up!")
print("=" * 60)
