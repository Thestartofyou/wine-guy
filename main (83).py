import random

# Define lists of descriptors for wine
colors = ["deep", "dark", "ruby", "garnet", "crimson", "purple"]
aromas = ["rich", "fruity", "earthy", "spicy", "floral", "smoky"]
flavors = ["bold", "complex", "smooth", "velvety", "balanced", "elegant"]

# Define a function to generate a wine description
def describe_wine():
    # Choose a random descriptor from each list
    color = random.choice(colors)
    aroma = random.choice(aromas)
    flavor = random.choice(flavors)
    
    # Combine the descriptors into a sentence
    sentence = "This wine is a " + color + " wine with " + aroma + " aromas and " + flavor + " flavors."
    return sentence

# Generate and print a wine description
print(describe_wine())
