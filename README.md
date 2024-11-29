# Quiz Generator System

An interactive quiz generation and management system built with Python. Create, manage, and take multiple-choice tests with ease.


## 🚀 Features

- **Multiple Categories**: Organize questions by topics
- **Interactive GUI**: User-friendly interface built with tkinter
- **Question Management**: Add, edit, and delete questions
- **Quiz Mode**: Take quizzes with randomized questions
- **Progress Tracking**: Monitor your quiz progress
- **Score Analysis**: Review your performance
- **Data Persistence**: Save all questions and categories locally

## 📋 Prerequisites

```bash
python 3.6+
tkinter (usually comes with Python)
cx-Freeze (for creating executable)
pillow
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/quiz-generator-system.git
cd quiz-generator-system
```

2. Install required packages:
```bash
pip install cx-Freeze pillow
```

## 💻 Usage

### Development Mode
Run the application directly:
```bash
python quiz_system.py
```

### Create Windows Executable
Build a standalone executable:
```bash
python build.py build
```

## 📖 How to Generate Questions

1. **Prepare Your Content**
   Create a text file with your learning material.

2. **Use the Question Generation Prompt**
   ```
   Given the previous file, create a series of questions that are 
   statistically and objectively relevant based on the content's 
   information structure. Determine the number of questions based 
   on the file's length and return them in the questions.json format.
   ```

3. **Expected JSON Format**
```json
{
    "default": [
        {
            "question": "What is the main concept of X?",
            "answers": [
                {
                    "text": "Answer 1",
                    "isCorrect": false
                },
                {
                    "text": "Answer 2",
                    "isCorrect": true
                },
                {
                    "text": "Answer 3",
                    "isCorrect": false
                },
                {
                    "text": "Answer 4",
                    "isCorrect": false
                }
            ]
        }
    ]
}
```

## 📁 Project Structure

```
quiz-generator/
├── src/
│   ├── quiz_system.py     # Main application
│   └── build.py          # Executable builder
├── data/
│   ├── categories.json   # Category definitions
│   └── questions.json    # Question database
├── build/               # Built executables
└── README.md
```

## 🎯 Features in Detail

### Category Management
- Create custom categories
- Delete unwanted categories
- Track questions per category

### Question Management
- Add multiple-choice questions
- Set correct answers
- Delete or modify questions
- Import/Export question sets

### Quiz Mode
- Select specific categories
- Randomized question order
- Real-time progress tracking
- Final score calculation
- Performance analysis

## 🔧 Customization

### Adding New Categories
1. Open the application
2. Click "Administrar"
3. Enter category name
4. Click "Añadir"

### Adding Questions
1. Select a category
2. Enter question text
3. Add four answer options
4. Select the correct answer
5. Click "Añadir Pregunta"

## 💡 Best Practices

1. **Content Preparation**
   - Use clear, concise text
   - Break down complex topics
   - Include key concepts

2. **Question Generation**
   - Ensure questions are relevant
   - Vary difficulty levels
   - Make answers distinct

3. **Quiz Administration**
   - Start with a test run
   - Monitor performance
   - Update question pool regularly

## 🙏 Acknowledgments

- Built with Python's tkinter
- Uses cx-Freeze for executable creation
- Inspired by educational testing systems

## 📬 Contact

Your Name - kikelamort

Project Link: [https://github.com/yourusername/quiz-generator-system](https://github.com/yourusername/quiz-generator-system)

---

Made with ❤️ by [Your Name] 
