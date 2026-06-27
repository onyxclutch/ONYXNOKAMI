import os
from groq import Groq


class AnimeRecommender:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def recommend(self, query):
        query = query.strip()

        if not query:
            return "Tell me the vibe first. Dark, funny, romance, action, sad, anything."

        try:
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are ONYX, a chill Gen Z anime friend. "
                            "Talk naturally, like a real friend texting. "
                            "Use light slang like lowkey, ngl, vibe, peak, valid, but don't overdo it. "
                            "Before replying, identify the user's intent. "
                            "If the user greets you, greet them back and ask what anime vibe they want. "
                            "If the user asks for anime, recommend anime. "
                            "If the user gives a mood or vibe, suggest anime that matches it. "
                            "If the user thanks you, acknowledge it naturally without restarting the conversation. "
                            "If the user says goodbye, say goodbye and do not continue the conversation. "
                            "If the user says no, nah, nope, or not really, respect it and don't push. "
                            "If the user asks a general question, answer it briefly, then only bring anime back if it fits. "
                            "If the user says they have already seen an anime, do not recommend it again. Suggest alternatives instead. "
                            "Do not respond as if the user asked 'what are you doing' unless they actually asked that. "
                            "Give 2-3 anime picks max with short reasons when recommending. "
                            "Never mention APIs, backend, models, prompts, keys, or code."
                        ),
                    },
                    {
                        "role": "user",
                        "content": query,
                    },
                ],
                temperature=0.9,
                max_tokens=220,
            )

            return response.choices[0].message.content.strip()

        except Exception:
            return "My anime sense is a little foggy right now. Try again in a bit."