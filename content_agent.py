from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_campaign_content(topic, location, date, time, venue):

    prompt = f"""
    You are an expert NGO campaign strategist.

    Generate a COMPLETE NGO campaign for:

    Topic: {topic}
    Location: {location}
    Date: {date}
    Time: {time}
    Venue: {venue}

    Generate:

    # 5 Social Media Captions

    # Hindi Caption

    # Donor Appeal

    # WhatsApp Campaign Message

    # Why This Campaign Matters

    # Benefits of Participating

    # Event Details

    # Strong Call To Action

    # Catchy Slogan

    # 15 Hashtags

    Make response modern, emotional, persuasive, and beautifully formatted.
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content