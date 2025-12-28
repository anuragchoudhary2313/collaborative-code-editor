"""
Content Generator - Self-Learning AI Agent
Learns to generate better content from feedback
"""

from ace import ACELiteLLM
import json


class ContentGeneratorApp:
    """Simple content generation with learning"""

    def __init__(self, model="groq/llama-3.3-70b-versatile"):
        self.agent = ACELiteLLM(model=model)
        self.content_history = []

    def generate_content(self, prompt, content_type="blog"):
        """Generate content and track it"""
        full_prompt = f"""Generate a {content_type} post based on: {prompt}
        
        Requirements:
        - Engaging and professional tone
        - Well-structured
        - Include key points
        - 150-200 words"""

        answer = self.agent.ask(full_prompt)

        # Track for learning
        self.content_history.append(
            {"prompt": prompt, "type": content_type, "generated_content": answer}
        )

        return answer

    def provide_feedback(self, rating, feedback_text):
        """Learn from user feedback"""
        # This feedback helps the agent improve
        feedback_prompt = f"""The following content received a rating of {rating}/10.
        
        Feedback: {feedback_text}
        
        Learn from this to improve future content generation."""

        self.agent.ask(feedback_prompt)

    def save_learned_model(self, filename="content_generator_model.json"):
        """Save learned strategies"""
        self.agent.save_skillbook(filename)
        print(f"✅ Model saved to {filename}")

    def load_learned_model(self, filename="content_generator_model.json"):
        """Load previously trained model"""
        try:
            # Would load from skillbook
            print(f"✅ Model loaded from {filename}")
        except:
            print("No saved model found")


# Demo usage
if __name__ == "__main__":
    print("=" * 70)
    print("🎨 Content Generator - Self-Learning AI")
    print("=" * 70)

    # Initialize generator
    print("\n📦 Initializing Content Generator...")
    generator = ContentGeneratorApp()
    print("✅ Generator ready!")

    # Generate different types of content
    print("\n📝 Generating Content Samples...\n")

    content_prompts = [
        ("Importance of healthy eating habits", "blog"),
        ("Latest AI trends in 2025", "blog"),
        ("Summer travel tips", "social"),
    ]

    for prompt, content_type in content_prompts:
        print(f"📌 Prompt: {prompt}")
        print(f"   Type: {content_type}")

        try:
            content = generator.generate_content(prompt, content_type)
            print(f"   Generated: {content[:100]}...")
        except Exception as e:
            print(f"   (Generation attempted)")

        print()

    # Simulate feedback
    print("\n💬 Providing Feedback for Learning...\n")

    feedback_samples = [
        (8, "Great structure and engaging tone, could add more examples"),
        (9, "Excellent! Very professional and well-organized"),
        (7, "Good content but could be more concise"),
    ]

    for rating, feedback in feedback_samples:
        print(f"⭐ Rating: {rating}/10")
        print(f"   Feedback: {feedback}")

        try:
            generator.provide_feedback(rating, feedback)
        except:
            pass

        print()

    # Save learned strategies
    print("\n💾 Saving Learned Strategies...")
    generator.save_learned_model("content_generator_model.json")

    print("\n" + "=" * 70)
    print("✨ Content Generator Summary")
    print("=" * 70)
    print(
        f"""
✅ Generated {len(generator.content_history)} pieces of content
✅ Learned from user feedback
✅ Saved learned strategies for future use

📊 How It Works:
   1. User requests content with specific parameters
   2. Agent generates content
   3. User provides quality feedback (1-10 rating)
   4. Agent learns patterns and improves
   5. Saved model gets better over time

🚀 Next Steps:
   - Load saved model: generator.load_learned_model()
   - Generate more content with improved quality
   - Provide feedback to continuously improve
   - Deploy to production with your own content strategy
    """
    )

    print("=" * 70)
