#it contains main code
#i am trying to code llm meditaion app

import openai

def generate_meditation(mood, duration_minutes):
    client = openai.OpenAI(api_key="your-api-key-here")
    
    prompt = f"""
    Write a {duration_minutes}-minute guided meditation script for someone feeling {mood}.
    The tone should be calm, grounding, and rhythmic. 
    Include brief pauses indicated by [pause].
    Focus on sensory details and breathwork.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional meditation coach."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

# Example usage
print(generate_meditation("restless", 5))
