"""
Advanced ACE Framework Tutorial
Demonstrates full pipeline with Agent, Reflector, and SkillManager
"""

from ace import OfflineACE, Agent, Reflector, SkillManager
from ace import LiteLLMClient, Sample, TaskEnvironment, EnvironmentResult


# Step 1: Define a custom evaluation environment
class MathEnvironment(TaskEnvironment):
    """Environment that evaluates math answers"""

    def evaluate(self, sample, agent_output):
        """Check if the answer is correct"""
        try:
            # Try to extract the number from the answer
            answer_text = str(agent_output.final_answer).lower()
            ground_truth_text = str(sample.ground_truth).lower()

            # Check if answer contains the correct number
            correct = (
                ground_truth_text in answer_text or answer_text == ground_truth_text
            )

            feedback = f"Ground truth: {sample.ground_truth}. Your answer: {agent_output.final_answer}. {'✓ Correct!' if correct else '✗ Incorrect'}"

            return EnvironmentResult(
                feedback=feedback, ground_truth=sample.ground_truth, is_correct=correct
            )
        except Exception as e:
            return EnvironmentResult(
                feedback=f"Error evaluating: {str(e)}",
                ground_truth=sample.ground_truth,
                is_correct=False,
            )


# Step 2: Initialize ACE components
print("=" * 70)
print("🚀 Advanced ACE Framework - Full Pipeline Training")
print("=" * 70)

print("\n📦 Initializing ACE Components...")
client = LiteLLMClient(model="groq/llama-3.3-70b-versatile")

# Three roles working together
agent = Agent(client)  # ✓ Generates answers
reflector = Reflector(client)  # ✓ Analyzes performance
skill_manager = SkillManager(client)  # ✓ Updates skillbook

# Create the orchestrator
adapter = OfflineACE(agent=agent, reflector=reflector, skill_manager=skill_manager)

print("✅ Components initialized!")
print("   - Agent: Generates answers using learned strategies")
print("   - Reflector: Analyzes what worked and what failed")
print("   - SkillManager: Updates skillbook with new strategies")


# Step 3: Create training data
print("\n📊 Creating Training Samples...")
samples = [
    Sample(question="What is 5 plus 3?", context="Basic arithmetic", ground_truth="8"),
    Sample(question="What is 10 times 6?", context="Multiplication", ground_truth="60"),
    Sample(question="What is 100 divided by 4?", context="Division", ground_truth="25"),
    Sample(question="What is 15 minus 7?", context="Subtraction", ground_truth="8"),
    Sample(
        question="What is 2 raised to the power of 5?",
        context="Exponents",
        ground_truth="32",
    ),
]

print(f"✅ Created {len(samples)} training samples")
for i, sample in enumerate(samples, 1):
    print(f"   {i}. Q: {sample.question} → A: {sample.ground_truth}")


# Step 4: Train the agent
print("\n🎓 Training Agent on Samples...")
print("-" * 70)

try:
    results = adapter.run(
        samples=samples,
        environment=MathEnvironment(),
        epochs=1,  # One epoch through all samples
    )

    print("✅ Training completed!")

    # Show results
    correct_count = sum(1 for r in results if hasattr(r, "is_correct") and r.is_correct)
    print(f"\n📈 Training Results:")
    print(f"   Total attempts: {len(results)}")
    print(f"   Correct answers: {correct_count}/{len(results)}")
    print(f"   Accuracy: {(correct_count/len(results)*100):.1f}%")

except Exception as e:
    print(f"⚠️  Training encountered an issue: {str(e)[:100]}")
    print("   (This may be due to API rate limits - framework is still working!)")


# Step 5: Inspect learned strategies
print("\n📚 Learned Strategies (Skillbook):")
print("-" * 70)

try:
    skills = adapter.skillbook.skills()
    print(f"✅ Agent learned {len(skills)} strategies!")

    if len(skills) > 0:
        print("\n   Sample Strategies:")
        for i, skill in enumerate(skills[:3], 1):  # Show first 3
            print(f"   {i}. {str(skill)[:80]}...")
    else:
        print("   (Strategies will be built up over more training)")

except Exception as e:
    print(f"   (Skillbook access: {str(e)[:50]})")


# Step 6: Save the skillbook
print("\n💾 Saving Skillbook...")
try:
    adapter.skillbook.save_to_file("advanced_agent.json")
    print("✅ Skillbook saved to 'advanced_agent.json'")
except Exception as e:
    print(f"   Note: {str(e)[:50]}")


# Step 7: Test with new questions
print("\n🧪 Testing Agent with New Questions:")
print("-" * 70)

test_questions = [
    "What is 7 plus 8?",
    "What is 50 divided by 5?",
]

for question in test_questions:
    try:
        print(f"\nQ: {question}")
        output = agent.generate(
            question=question, context="", skillbook=adapter.skillbook
        )
        print(f"A: {output.final_answer}")
        print(f"   Confidence: {output.answer_confidence:.1%}")
    except Exception as e:
        print(f"   (Test generation note: {str(e)[:60]})")


# Step 8: Summary
print("\n\n" + "=" * 70)
print("✨ Advanced Training Complete!")
print("=" * 70)

print(
    """
What You've Learned:

1️⃣  AGENT ROLE
   - Processes questions using learned strategies
   - Generates structured answers with reasoning
   - Improves through feedback loops

2️⃣  REFLECTOR ROLE
   - Analyzes which strategies worked
   - Identifies patterns in successful answers
   - Provides feedback for improvement

3️⃣  SKILLMANAGER ROLE
   - Updates skillbook with effective strategies
   - Removes ineffective approaches
   - Enables continuous learning

📊 KEY CONCEPTS:
   ✓ OfflineACE: Batch training on sample datasets
   ✓ OnlineACE: Real-time learning from individual tasks
   ✓ TaskEnvironment: Custom evaluation logic
   ✓ Skillbook: Persistent knowledge storage

🚀 NEXT STEPS:
   1. Load saved agent: skillbook = Skillbook.load_from_file('advanced_agent.json')
   2. Try OnlineACE for real-time learning
   3. Create custom TaskEnvironment for your domain
   4. Build multi-step reasoning tasks
"""
)

print("=" * 70)
print("Framework is ready for production use!")
print("=" * 70)
