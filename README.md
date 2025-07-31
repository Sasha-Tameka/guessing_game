# 🎯 Advanced Word Guessing Game

A sophisticated word guessing game built in Python featuring multiple difficulty levels, advanced scoring system, performance tracking, and Wordle-style letter feedback!

## 🎮 Features

### **Core Gameplay**
- **3 Attempts**: Players get exactly 3 tries to guess the secret word
- **Difficulty Levels**: Choose from Easy (3-4 letters), Medium (5-6 letters), or Hard (7+ letters)
- **Smart Hints**: Progressive hints appear after each incorrect guess
- **Wordle-Style Feedback**: Color-coded letter feedback system:
  - 🟩 **Green**: Correct letter in correct position
  - 🟨 **Yellow**: Correct letter in wrong position  
  - 🟥 **Red**: Letter not in the word

### **Advanced Features**
- **Multi-Factor Scoring System**: Points based on efficiency, difficulty, word length, and speed
- **Performance Tracking**: Win rate and game statistics
- **Time Tracking**: Bonus points for quick solving
- **Input Validation**: Handles empty inputs, numbers, and invalid entries
- **Random Word Selection**: Different word each game from curated lists

## 🚀 How to Play

### **Getting Started**
1. Run the program to see the welcome screen with game rules
2. Choose your difficulty level (easy/medium/hard) or press Enter for random
3. The game will show your current score and difficulty mode

### **Gameplay**
1. **First Guess**: You'll see a hint about the difficulty level
2. **Second Guess**: If wrong, you'll get a hint about the word length
3. **Third Guess**: Your final chance to guess correctly
4. **Feedback**: After each wrong guess, see color-coded letter feedback
5. **Results**: Win or lose, see your performance stats!

### **Example Gameplay**
```
🎯 Welcome to the Word Guessing Game! 🎯
You have 3 tries to guess the secret word.
🟩 = Right letter, right spot
🟨 = Right letter, wrong spot
🟥 = Letter not in word
----------------------------------------

Choose difficulty (easy/medium/hard) or Enter for random: hard
Playing on hard mode!
Current Score : 0

Hint: it's a hard word
Enter guess #1: tiger
Word: TIGER
🟥🟥🟥🟥🟩

Hint: It has 8 letters
Enter guess #2: elephant
🎉 Correct! The word was 'elephant'
⏱️  Time: 15.3 seconds
🎯 Points earned: 370
📊 Total Score: 370
🏆 Win Rate: 100.0% (1/1)
```

## 🏆 Scoring System

Your score is calculated based on four factors:

### **1. Guess Efficiency (0-150 points)**
- 1st try: 150 points
- 2nd try: 100 points  
- 3rd try: 50 points
- Failed: 0 points

### **2. Difficulty Multiplier (100-200 points)**
- Easy: 100 points (×1.0)
- Medium: 150 points (×1.5)
- Hard: 200 points (×2.0)

### **3. Word Length Bonus (10 points per letter)**
- "cat" (3 letters): 30 points
- "elephant" (8 letters): 80 points

### **4. Speed Bonus (0-120 points)**
- Under 60 seconds: Bonus points for remaining time
- Formula: `(60 - seconds_used) × 2`
- Example: 30 seconds = 60 bonus points

**Minimum Score**: Every correct guess earns at least 10 points

## 🛠️ Installation & Setup

### **Prerequisites**
- Python 3.6 or higher

### **Running the Game**
1. Save the code as `word_game.py`
2. Open terminal/command prompt
3. Navigate to the file location
4. Run the game:
```bash
python word_game.py
```

## 📁 Code Structure

```
word_game.py
├── Game Variables & Setup
├── introduction() - Welcome screen and rules
├── Word Lists - Difficulty-based word collections
├── calculate_score() - Multi-factor scoring algorithm
├── get_valid_guess() - Input validation
├── get_letter_feedback() - Letter analysis (G/Y/R system)
├── display_feedback() - Color-coded output
└── Main Game Loop - Core gameplay logic
```

### **Key Functions**

#### **`calculate_score(tries_used, word_length, difficulty, time_taken)`**
Calculates points based on performance factors:
- **tries_used**: Number of guesses used (1-3)
- **word_length**: Letters in the secret word
- **difficulty**: Game difficulty level
- **time_taken**: Seconds to solve

#### **`get_letter_feedback(guess, secret_word)`**
Returns feedback array analyzing each letter:
- **G**: Green (correct position)
- **Y**: Yellow (wrong position)  
- **R**: Red (not in word)

#### **`display_feedback(guess, feedback)`**
Shows formatted results with emoji colors

## 📊 Game Statistics

The game tracks your performance across sessions:
- **Total Score**: Cumulative points earned
- **Games Played**: Total number of games
- **Games Won**: Number of successful guesses
- **Win Rate**: Percentage of games won

## 🎯 Word Lists

### **Easy Words (3-4 letters)**
cat, dog, sun, car, book

### **Medium Words (5-6 letters)**  
apple, piano, garden, bridge

### **Hard Words (7+ letters)**
elephant, butterfly, crocodile

## 🔮 Future Enhancements

- [ ] Persistent score saving between sessions
- [ ] Expanded word databases with themes
- [ ] Multiplayer competitive mode
- [ ] Daily challenge words
- [ ] Achievement system
- [ ] Leaderboard functionality
- [ ] Custom word list import
- [ ] Sound effects and animations

## 🎨 Technical Highlights

- **Defensive Programming**: Robust input validation
- **Modular Design**: Clean function separation
- **Real-time Feedback**: Instant visual responses
- **Performance Metrics**: Multi-dimensional scoring
- **User Experience**: Clear instructions and feedback

## 🤝 Contributing

Contributions welcome! Areas for improvement:

1. **Word Database Expansion**: Add themed categories
2. **UI Enhancements**: Better visual design
3. **Persistence**: Save/load high scores
4. **Multiplayer**: Turn-based or competitive modes
5. **Mobile Version**: Touch-friendly interface


## 🎉 Acknowledgments

Inspired by Wordle and classic word games. Built to demonstrate Python programming concepts:

- **Object-oriented design** with functions and modules
- **Real-time data processing** with feedback systems
- **User input handling** and validation
- **Mathematical calculations** for scoring algorithms
- **Performance tracking** and statistics

Perfect for Python learners and word game enthusiasts!

---

**Challenge yourself and improve your vocabulary!** 🧠✨