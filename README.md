Trivia Personality Quiz in Python

## Objective

In this project, you will build a **command-line trivia game** that fetches real trivia questions from an online API (Open Trivia DB).
Your program should quiz the user, keep track of their performance per category, and finally generate a **“personality-ish profile”** based on their strengths.

This assignment will help you practice:

* Fetching and parsing JSON data from an API using `requests`
* Handling **HTML-escaped text** safely (e.g., `&amp;` → `&`)
* Working with dictionaries and lists in Python
* Using **randomization** to make the program feel dynamic
* Designing a **fun “analysis step”** that interprets quiz results

---

## Requirements

1. **Fetch Trivia Questions**

   * Use the [Open Trivia DB API](https://opentdb.com/api_config.php) to get multiple-choice questions.
   * API endpoint:

     ```
     https://opentdb.com/api.php?amount=3&category=<ID>&type=multiple
     ```

     * `amount` = number of questions
     * `category` = category ID (see API docs)
     * `type=multiple` = multiple-choice questions

2. **Random Categories**

   * From a pool of 8–10 categories (Books, Music, Sports, Science & Nature, etc.), randomly select **3 categories per run**.
   * Each category should have **3 questions**.

3. **Game Flow**

   * Display each question and 4 shuffled options.
   * Ask the player for an answer (1–4).
   * Keep track of **score per category**.

4. **Results**

   * At the end, print the score for each category.
   * Interpret the best category into a **“personality type.”**
     Example:

     * Highest in *Books* → “You’re a storyteller at heart 📚”
     * Highest in *Science & Nature* → “You think like a scientist 🔬”
     * Balanced across categories → “All-round explorer 🌈”

5. **Robustness**

   * Handle invalid inputs (e.g., user types a letter instead of a number).
   * Escape HTML entities (hint: use Python’s `html.unescape`).

---

## Bonus (Optional)

* Let the player **choose their own categories** instead of random ones.
* Save results to a **CSV file** with timestamp.
* Give the player a chance to **play again** without restarting the program.

---

## Resources

* **Open Trivia DB API Documentation**:
  🔗 [https://opentdb.com/api\_config.php](https://opentdb.com/api_config.php)
  🔗 [API endpoint guide](https://opentdb.com/api.php)

* **Category List (IDs)**:
  🔗 [https://opentdb.com/api\_category.php](https://opentdb.com/api_category.php)

* **Python Docs**:

  * [requests library](https://docs.python-requests.org/en/latest/)
  * [html.unescape](https://docs.python.org/3/library/html.html)
  * [random module](https://docs.python.org/3/library/random.html)

---

## Deliverables

* A single Python script (`trivia_quiz.py`).
* Runs in the terminal with interactive input/output.
* Shows both **quiz performance** and **personality-ish results**.

---

✨ **Grading Idea:**

* API usage (20%)
* Correct logic for scoring per category (20%)
* Handling HTML escape + invalid input (20%)
* Fun “personality analysis” at the end (20%)
* Code readability & comments (20%)

---

Would you like me to also provide a **starter template** (like skeleton code with TODOs) that your students can fill in? That way they don’t start from scratch but still have to implement the main logic.
