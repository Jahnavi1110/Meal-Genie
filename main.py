import os
from google import genai
from google.genai.errors import APIError

# --- 1. Client Initialization ---
# !!! CRITICAL STEP: REPLACE THIS PLACEHOLDER WITH YOUR ACTUAL, SECRET API KEY !!!
# The key is the long string you copied from the Google AI Studio website.
# The quotes ("") MUST stay around your key.


try:
    # Pass the API key directly to the client to fix the PyCharm environment loading issue
    client = genai.Client(api_key=API_KEY)
    MODEL = "gemini-2.5-flash"
except Exception as e:
    print(f"Error initializing Gemini client: {e}")
    print("FATAL ERROR: The API key is likely invalid or missing. Please ensure the key in main.py is correct.")
    exit()


# --- 2. Recipe Generation Function ---
def generate_recipe(ingredients_list):
    """Generates a recipe based on a list of available ingredients."""

    ingredients_str = ", ".join(ingredients_list)

    # Prompting the AI Chef
    prompt = f"""
    You are an expert AI Chef specializing in quick and easy global cuisine.
    Your task is to create a simple, step-by-step recipe using as many of the following user-supplied ingredients as possible: {ingredients_str}.

    The recipe must include:
    1. Recipe Name (Creative and appetizing)
    2. Ingredients List with estimated quantities (e.g., 2 tbsp, 1 cup)
    3. Total Estimated Preparation Time (e.g., 25 minutes)
    4. Simple, numbered Cooking Instructions (no more than 6 steps)

    Present the output professionally, like an entry in a modern cookbook.
    """

    print("\n--- AI Chef is Thinking... ---\n")
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        return response.text
    except APIError as e:
        return f"An API Error occurred: {e}. If the key is correct, check your network or API quota."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# --- 3. Main Program Loop ---
def main():
    print("🍽 Welcome to the AI Cookbook 🤖")
    print("Let's create a recipe based on what you have.")

    # Get user input
    user_input = input("Enter your ingredients (separated by commas, e.g., 'chicken, tomatoes, cheese, pasta'): ")

    # Process the input into a clean list
    ingredients = [item.strip() for item in user_input.split(',') if item.strip()]

    if not ingredients:
        print("You didn't enter any ingredients. Exiting.")
        return

    # Call the AI function
    recipe_output = generate_recipe(ingredients)

    # Print the result
    print("\n==============================================")
    print("✨ Your Custom AI Recipe ✨")
    print("==============================================")
    print(recipe_output)
    print("==============================================")
if _name_ == "_main_":
    main()
