from src.recommender import AnimeRecommender


class ONYXNOKAMI:
    def __init__(self):
        self.recommender = AnimeRecommender()

    def handle(self, user_text):
        user_text = user_text.strip()

        if not user_text:
            return "Gimme a vibe first."

        return self.recommender.recommend(user_text)