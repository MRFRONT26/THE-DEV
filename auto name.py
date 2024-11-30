import random

def generate_random_name():
    first_names = ["Aria", "Liam", "Maya", "Noah", "Zara", "Ethan", "Sofia", "Lucas", "Ava", "Mason"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return f"{first_name} {last_name}"

# Generate a random name
random_name = generate_random_name()
print(f"Randomly generated name: {random_name}")
