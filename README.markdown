Random Names Generator

Welcome to the Random Names Generator, a lightweight Python script crafted by dziduchm to create unique, pseudo-random names of customizable length. This project demonstrates clean code principles, leveraging NumPy for randomization and offering a flexible, class-based design. Perfect for developers, game designers, or anyone needing placeholder names, this tool is both efficient and easy to extend.
Overview
The Random Names Generator produces random names by alternating between vowels and consonants, allowing users to specify the number of names and their length. Names are generated using a deterministic pseudo-random process, ensuring reproducibility with different seeds. The script saves results to a random-names.txt file in the current directory, making it ideal for local use without external dependencies beyond Python.
Features

Generate a customizable number of random names.
Define the length of each name (default: 5 characters).
Option to save names to a file or print to console.
Clean, object-oriented code structure for maintainability.
Compatible with Windows, macOS, and Linux.

Requirements

Python 3.x
NumPy: For random number generation (pip install numpy)
argparse: Included with Python standard library

Installation

Clone the repository:git clone https://github.com/dziduchm/random_names_generator.git
cd random_names_generator


Install the required dependency:pip install numpy



Usage
Run the script with command-line arguments to generate names:
python name_generator.py --num_names 10 --name_len 6 --save_file yes

Arguments

--num_names: Number of names to generate (default: 10).
--name_len: Length of each name (default: 5).
--save_file: Save to file (yes/no, default: no). If "yes", names are saved to random-names.txt.

Example Output
Without saving:
hloita
cvyysi
dqirll
efqsab
hmjiem
sygeno
pyebii
eynmya
qdlkdu
ylpoku

With --save_file yes:

A random-names directory is created in the current directory.
Names are saved to random-names/random-names.txt, with a message indicating the save location (e.g., Names saved to: C:\path\to\random-names\random-names.txt).

Development
This project is open for contributions! Follow these guidelines:

Fork the Repository: Create your own fork on GitHub.
Create a Branch: Use a descriptive name (e.g., feature/enhance-output).
Commit Changes: Write clear, concise commit messages.
Submit a Pull Request: Include details of your changes and pass existing tests.
Code Standards: Adhere to PEP 8 and include type hints where applicable.

Testing

Run tests locally (add test files as needed in the future).
Ensure compatibility with the specified requirements.

License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements

Built with inspiration from clean code practices and NumPy’s robust random utilities.
Thanks to the Python community for tools like argparse and os.

Contact
For questions or collaboration, reach out to [Marcin](https://github.com/dziduchm) via GitHub or X.com [@MarcinDziduch](https://x.com/MarcinDziduch).