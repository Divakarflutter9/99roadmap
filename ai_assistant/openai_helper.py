"""
OpenAI Integration for AI Assistant
"""

import openai
import json
from django.conf import settings


class AIAssistant:
    """AI Assistant using OpenAI API"""
    
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY
        if settings.OPENAI_BASE_URL:
            openai.base_url = settings.OPENAI_BASE_URL
        self.model = settings.OPENAI_MODEL_NAME
    
    def get_response(self, user_message, context=None):
        """
        Get AI response based on user message and context
        
        Args:
            user_message: User's question
            context: Dict with roadmap, stage, topic, user info
        
        Returns:
            AI response string
        """
        
        # Build system prompt with context
        system_prompt = self._build_system_prompt(context)
        
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=500,
                temperature=0.7,
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
    
    def _build_system_prompt(self, context):
        """Build context-aware system prompt"""
        
        base_prompt = """You are an intelligent learning assistant for 99Roadmap, a platform that helps students master skills through structured roadmaps.
        
Your role is to:
- Explain topics in simple, student-friendly language
- Answer doubts and questions
- Suggest next steps in learning
- Motivate and encourage students
- Keep answers concise and practical

"""
        
        if not context:
            return base_prompt
        
        # Add roadmap context
        if context.get('roadmap'):
            base_prompt += f"\nCurrent Roadmap: {context['roadmap']}"
        
        if context.get('stage'):
            base_prompt += f"\nCurrent Stage: {context['stage']}"
        
        if context.get('topic'):
            base_prompt += f"\nCurrent Topic: {context['topic']}"
        
        # Add user context
        if context.get('user'):
            base_prompt += f"\n\nUser Info:"
            base_prompt += f"\n- Study: {context['user'].get('study_type', 'N/A')}"
            base_prompt += f"\n- Branch: {context['user'].get('branch', 'N/A')}"
        
        base_prompt += "\n\nProvide helpful, encouraging answers tailored to this context."
        
        return base_prompt
    
    def explain_topic(self, topic_title, topic_content):
        """Generate a simpler explanation of a topic"""
        
        prompt = f"Explain this topic in simple terms for students:\n\nTopic: {topic_title}\n\n{topic_content[:500]}"
        
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful tutor. Explain complex topics in simple language."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            return f"Error generating explanation: {str(e)}"
    
    def generate_quiz_hint(self, question, user_answer):
        """Generate a hint for a quiz question"""
        
        prompt = f"A student is stuck on this question:\n\n{question}\n\nTheir answer was: {user_answer}\n\nProvide a helpful hint without revealing the answer."
        
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a supportive tutor helping students learn."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            return "Think about the key concepts and try again!"

    def generate_quiz_for_stage(self, stage_title, topic_summaries):
        """
        Generate a quiz for a stage based on its topics
        
        Args:
            stage_title: Title of the stage
            topic_summaries: List of strings (title + brief content) for context
            
        Returns:
            JSON object or None
        """
        
        context_str = "\n\n".join(topic_summaries[:15]) # Increased limit to capture more context
        
        prompt = f"""Create a quiz for the stage: "{stage_title}".
        
        Here is the context of topics covered:
        {context_str}
        
        Generate 5 multiple-choice questions.
        IMPORTANT RULES:
        1. Questions must be STRICTLY based on the provided context only.
        2. Do NOT ask about concepts not mentioned in the context.
        3. If the context is about 'HTML', do not ask about 'Python'.
        4. Make questions specific to the provided content.
        
        Return ONLY a raw JSON array. Do not wrap in markdown code blocks.
        
        Format:
        [
            {{
                "question": "Question text here?",
                "type": "multiple",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_index": 0,
                "explanation": "Why this is correct (based on context)."
            }}
        ]
        """
        
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a quiz generator. Output only valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
            )
            
            content = response.choices[0].message.content.strip()
            # Clean up potential markdown wrappers
            if content.startswith("```json"):
                content = content[7:]
            if content.startswith("```"):
                content = content[3:]
            if content.endswith("```"):
                content = content[:-3]
                
            return json.loads(content)
            
        except Exception as e:
            print(f"Quiz generation error: {e}")
            return None
