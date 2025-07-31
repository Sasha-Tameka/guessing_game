# 🎯 Word Guessing Game

A fun and interactive word guessing game built in Python! Players have 3 attempts to guess a secret word with helpful hints and color-coded letter feedback.

## 🎮 Features

- **3 Attempts**: Players get exactly 3 tries to guess the secret word
- **Smart Hints**: Progressive hints appear after each incorrect guess
- **Letter Feedback**: Color-coded feedback system similar to Wordle:
  - 🟩 **Green**: Correct letter in correct position
  - 🟨 **Yellow**: Correct letter in wrong position  
  - 🟥 **Red**: Letter not in the word
- **Input Validation**: Handles empty inputs, numbers, and short words gracefully
- **Case Insensitive**: Accepts both uppercase and lowercase input

## 🚀 How to Play

1. Run the program
2. You'll see the first hint: "Hint: it's an animal"
3. Enter your first guess (must be at least 2 letters, letters only)
4. Get color-coded feedback on your guess
5. If wrong, you'll get a second hint: "Hint: It has 7 letters"
6. Continue guessing until you either:
   - ✅ Guess correctly and win!
   - ❌ Run out of attempts and lose

### Example Gameplay
```
Hint: it's an animal
Enter guess #1: tiger
Word: TIGER
🟩🟥🟨🟥🟥

Hint: It has 7 letters
Enter guess #2: giraffe
You win!
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.6 or higher

### Running the Game
1. Clone or download the repository
2. Navigate to the project directory
3. Run the game:
```bash
python guessing_game.py
```



### Key Functions

- **`get_valid_guess(prompt)`**: Validates user input (letters only, minimum length)
- **`get_letter_feedback(guess, secret_word)`**: Returns feedback array with G/Y/R codes
- **`display_feedback(guess, feedback)`**: Prints formatted results with emoji colors

## 🎯 Current Secret Word

The game currently uses **"giraffe"** as the secret word. You can easily change this by modifying the `secret_word` variable.

## 🔮 Future Enhancements

- [ ] Random word selection from a word list
- [ ] Multiple difficulty levels (word length)
- [ ] Score tracking and high scores
- [ ] Play again functionality
- [ ] Custom word categories (animals, countries, etc.)
- [ ] Timer-based challenges
- [ ] Multiplayer support

## 🤝 Contributing

Feel free to fork this project and submit pull requests! Some ideas for contributions:

1. Add a word database with different categories
2. Implement difficulty levels
3. Add sound effects or animations
4. Create a GUI version
5. Add multiplayer functionality

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 Acknowledgments

Inspired by popular word games like Wordle and classic hangman games. Built as a learning project to practice Python programming concepts including:

- Functions and modular code design
- Input validation and error handling  
- String manipulation and comparison
- Game loop logic
- User interface design

---

**Happy Guessing!** 🦒

Multiple difficulty levels: Easy (3-4 letters), Medium (5-6 letters), Hard (7+ letters)
Random word selection: Pick from a list of words instead of hardcoding one
Category themes: Animals, countries, movies, etc.
Scoring system: Points based on guesses remaining, time taken, or difficulty
Lives/hearts system: Visual representation instead of just "tries"