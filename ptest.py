import requests
import html
import random

# Map Open Trivia categories to "personality-ish" traits
CATEGORY_TRAITS = {
    "Entertainment: Books": "Storyteller at heart 📚",
    "Entertainment: Film": "Cinematic dreamer 🎬",
    "Entertainment: Music": "Rhythmic soul 🎶",
    "Entertainment: Video Games": "Strategic gamer 🎮",
    "Science: Computers": "Tech thinker 💻",
    "Science: Gadgets": "Innovative tinkerer 🔧",
    "Science & Nature": "Curious scientist 🔬",
    "Sports": "Energetic competitor 🏆",
    "General Knowledge": "Curious explorer 🌍"
}

def fetch_questions(category_id, amount=5):
    """Fetch trivia questions from Open Trivia DB API."""
    url = f"https://opentdb.com/api.php?amount={amount}&category={category_id}&type=multiple"
    response = requests.get(url)
    data = response.json()
    questions = []
    for q in data["results"]:
        question = html.unescape(q["question"])
        correct = html.unescape(q["correct_answer"])
        options = [html.unescape(opt) for opt in q["incorrect_answers"]]
        options.append(correct)
        random.shuffle(options)

        category_name = html.unescape(q["category"])  # fix HTML escaping

        questions.append({
            "question": question,
            "options": options,
            "answer": correct,
            "category": category_name
        })
    return questions

def play_quiz():
    # All categories we care about (Open Trivia DB IDs)
    all_categories = {
        "Entertainment: Books": 10,
        "Entertainment: Film": 11,
        "Entertainment: Music": 12,
        "Entertainment: Video Games": 15,
        "Science: Computers": 18,
        "Science: Gadgets": 30,
        "Science & Nature": 17,
        "Sports": 21,
        "General Knowledge": 9
    }

    # Randomly pick 3 categories each run
    chosen = dict(random.sample(list(all_categories.items()), 3))

    score_per_category = {cat: 0 for cat in chosen}

    print("🎲 Welcome to the Trivia + Personality Quiz!\n")
    print(f"Today’s categories: {', '.join(chosen.keys())}\n")

    for cat_name, cat_id in chosen.items():
        print(f"\n--- {cat_name} ---")
        questions = fetch_questions(cat_id, amount=3)
        for q in questions:
            print("\n" + q["question"])
            for i, opt in enumerate(q["options"], 1):
                print(f"{i}. {opt}")
            try:
                choice = int(input("Your answer (1-4): "))
                if q["options"][choice - 1] == q["answer"]:
                    print("✅ Correct!")
                    score_per_category[q["category"]] += 1
                else:
                    print(f"❌ Wrong! Correct: {q['answer']}")
            except (ValueError, IndexError):
                print("Invalid input, skipping...")

    return score_per_category

def personality_results(scores):
    print("\n✨ Personality-ish Results ✨")
    for cat, score in scores.items():
        print(f"{cat}: {score} points")

    # Find top scoring category
    best_category = max(scores, key=scores.get)
    trait = CATEGORY_TRAITS.get(best_category, "Unique mind 🌟")
    print(f"\nYour personality type: {trait}")

    # Special cases
    if len(set(scores.values())) == 1:
        print("👉 Balanced across all! You’re an All-round Explorer 🌈")
    elif max(scores.values()) - min(scores.values()) >= 3:
        print("👉 Strong preference detected — you’re a Specialist 🔥")

if __name__ == "__main__":
    scores = play_quiz()
    personality_results(scores)
