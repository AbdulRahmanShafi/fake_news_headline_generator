# Fake Headline Generator

> A lightweight Python CLI that generates random, humorous fake headlines by combining subjects, actions, and locations.

## Overview

Fake Headline Generator is an entertaining command-line utility designed to demonstrate core Python programming concepts including lists, random selection, loops, and user input handling. Perfect for learning or just having fun.

## Features

✨ **Key Capabilities:**

- Generates random, sentence-based headlines
- Interactive prompt for continuous generation
- No external dependencies—uses only Python standard library
- Minimal, maintainable codebase
- Easily extensible with custom subjects, actions, and locations

## Requirements

- **Python 3.x** (Python 3.6 or higher recommended)

No third-party packages required.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/fake_headline_generator.git
   cd fake_headline_generator
   ```

2. **Verify Python is installed:**
   ```bash
   python --version
   ```

## Usage

Run the script to start generating headlines:

```bash
python fake_headline_generator.py
```

### Example Session

```
Eagle flies in the sky

Do you want to generate another headline? (yes/no): yes

Prime Minister of Pakistan works in the office

Do you want to generate another headline? (yes/no): no
```

## How It Works

The program maintains three data lists:

| Component | Purpose |
|-----------|---------|
| **Subjects** | The main entity (Eagle, Tiger, Car driver, etc.) |
| **Actions** | What the subject does (flies, runs, jumps, etc.) |
| **Locations** | Where the action occurs (in the sky, at the zoo, etc.) |

Each iteration randomly selects one item from each list and formats them into a headline sentence.

## Project Structure

```
fake_headline_generator/
├── fake_headline_generator.py    # Main script
├── README.md                      # Documentation
├── LICENSE                        # MIT License
└── .gitignore                     # Git configuration
```

## Future Enhancements

- [ ] Add a non-interactive mode for batch generation
- [ ] Export generated headlines to a file
- [ ] Implement more sophisticated sentence structures
- [ ] Add headline filtering or search capabilities

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

**Created:** 2026 | **Author:** Abdul Rahman 
