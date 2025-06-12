import pandas as pd

def get_ranking(user_id: str) -> list:
    if user_id == "test":
        # Placeholder for the actual ranking logic
        return ["Item A", "Item B", "Item C"]


def get_ranking_score(user_id: str) -> dict:
    # Placeholder for the actual ranking score logic
    if user_id == "test":
        score_dict = {"A": 90, "B": 80, "C": 70}
        data = pd.DataFrame(score_dict.items(), columns=["Category", "Values"])
        return data

def get_analysis(user_id: str) -> dict:
    # Placeholder for the actual analysis logic
    if user_id == "test":
        return "Data analysis results for user ID: test"