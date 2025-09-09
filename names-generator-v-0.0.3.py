import numpy as np
import os
import argparse

class NameGenerator:
    """A class to generate random names of specified length using vowels and consonants."""
    
    def __init__(self, num_names: int = 10, name_len: int = 5, save_file: bool = False):
        """Initialize the NameGenerator with configuration parameters.
        
        Args:
            num_names (int): Number of names to generate (default: 10).
            name_len (int): Length of each name (default: 5).
            save_file (bool): Whether to save names to a file (default: False).
        """
        self.num_names = num_names
        self.name_len = name_len
        self.save_file = save_file
        self.vowels, self.consonants = self._initialize_alphabet()

    def _initialize_alphabet(self) -> tuple[dict, dict]:
        """Initialize dictionaries for vowels and consonants.
        
        Returns:
            tuple: (vowels_dict, consonants_dict) for random name generation.
        """
        vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u', 6: 'y'}
        consonants = {1: 'b', 2: 'c', 3: 'd', 4: 'f', 5: 'g', 6: 'h', 7: 'j', 8: 'k', 9: 'l',
                      10: 'm', 11: 'n', 12: 'p', 13: 'q', 14: 'r', 15: 's', 16: 't', 17: 'v',
                      18: 'w', 19: 'x', 20: 'y'}
        return vowels, consonants

    def _generate_name(self) -> str:
        """Generate a single random name of the specified length.
        
        Returns:
            str: A randomly generated name.
        """
        generated_name = ""
        for _ in range(1, self.name_len + 1):
            v_c = np.random.randint(1, 9)
            if v_c in (1, 2, 8):  # Rough heuristic for vowel selection
                v = np.random.randint(1, 7)
                generated_name += self.vowels[v]
            else:
                c = np.random.randint(1, len(self.consonants) + 1)
                generated_name += self.consonants[c]
        return generated_name

    def generate_names(self) -> list[str]:
        """Generate a list of random names.
        
        Returns:
            list[str]: List of generated names.
        """
        names = []
        for i in range(1, self.num_names + 1):
            np.random.seed(i * np.random.randint(2, 10000))  # 'Randomize' seed per name
            names.append(self._generate_name())
        return names

    def save_names(self, names: list[str]) -> None:
        """Save the generated names to a file in the current directory.
        
        Args:
            names (list[str]): List of names to save.
        """
        output_dir = os.path.join(os.getcwd(), "random-names")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "random-names.txt")
        with open(output_path, 'w', encoding='utf-8') as f:
            for name in names:
                f.write(f"{name}\n")
        print(f"Names saved to: {os.path.abspath(output_path)}")

def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments for the name generator.
    
    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Random names generator")
    parser.add_argument('--num_names', type=int, default=10, help='Number of names to generate (default: 10)')
    parser.add_argument('--name_len', type=int, default=5, help='Length of each name (default: 5)')
    parser.add_argument('--save_file', type=str, default='no', help='Save names to file (yes/no, default: no)')
    return parser.parse_args()

def main():
    """Main function to run the name generator."""
    args = parse_arguments()
    save_file = args.save_file.lower() == 'yes'
    generator = NameGenerator(args.num_names, args.name_len, save_file)
    names = generator.generate_names()
    
    if not save_file:
        for name in names:
            print(name)
    else:
        generator.save_names(names)

if __name__ == "__main__":
    main()