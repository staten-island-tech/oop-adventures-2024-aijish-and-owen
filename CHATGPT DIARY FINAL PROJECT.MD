ChatGPT Coding Diary
Project Name: RPG [aijish + owen]
Date: 12/10/24

1. Task/Problem Description
Briefly describe the problem you're trying to solve or the task you're working on.
Example:
I need to make a game utilizing classes.

2. Initial Approach/Code
Describe the initial approach you took to solving the problem. If you started writing code, include it here.
# Example: Initial sorting function
def sort_numbers(numbers):
    return sorted(numbers)
What was your plan for solving the problem?
We decided to make a class for the merchant, the monsters, the final boss, the user and the game itself.
Did you have any initial thoughts or strategies before using ChatGPT?
The merchant class would be able to buy items, display the inventory of the player etc. The monster class would show how the monsters act, (name/health/damage/flee_rate). The final boss would be similar to the monster class but instead one big monster as the final boss. The user class would give the player properties (health, damage, coins, and an inventory). And then the game class would be what actually makes the game run.

3. Interaction with ChatGPT
Questions/Requests to ChatGPT
Write down the questions or requests you made to ChatGPT. Also include what code from ChatGPT you are unsure of and craft a question that asks for further clarification. For example:
"How do I reverse a list in Python?"
"Can you suggest a more efficient way to sort a list?"
Why did ChatGPT opt to create an element when my teacher suggested insertAdjacentHTML?
How do I add a flee rate to the monsters?
How do I import my json files into main.py?
How do I make weapons deteriorate over time instead of being removed from the player's inventory immediately after one use?


# Example prompt to ChatGPT:
How can I optimize this sorting function for large datasets?


4. ChatGPT's Suggestions/Code Changes
Record the code or suggestions ChatGPT provided. Include any changes or improvements ChatGPT suggested and how it influenced your approach.
# ChatGPT suggested using a custom sorting algorithm to improve efficiency
def optimized_sort(numbers):
    # Implementation of a more efficient sorting algorithm
    pass
What was ChatGPT's solution or suggestion?
Make the flee rate a property of the monster class–self.flee_rate.
import random import json from user import User from monsters import GreekMonster, FinalBoss from unifiedmerchant import UnifiedMerchant
Add a durability property into the json file of the weapons, and make it slowly go down with every attack.
How did it differ from your original approach?

5. Reflection on Changes
Reflect on the changes made to your code after ChatGPT's suggestions. Answer the following questions:
Why do you think ChatGPT's suggestions are helpful or relevant?
ChatGPT’s suggestions were helpful/relevant because they allowed me to import my files/jsons into main.py 
Did the suggestions improve your code? How?
Yes, they made the code actually run instead of having missing properties from when they were not imported.
Did you understand why the changes were made, or are you still uncertain about some parts?
I did understand why the changes were made.

6. Testing and Results
After making the changes, did you test your code? What were the results?
Did you run any tests (e.g., unit tests, edge cases)?
Did the code work as expected after incorporating ChatGPT's changes?
# Example: Testing the updated sorting function
numbers = [5, 2, 9, 1]
print(optimized_sort(numbers))  # Expected output: [1, 2, 5, 9]
Did you encounter any bugs or issues during testing?


After we made the changes, we ran the code again and there were still some issues. We found out that the code was trying to use the json as a list not a dictionary which is not possible. We changed the code so that it runs the json as a dictionary. After that there were still some problems which we identified as a problem in the weapon json file. We found out that the format was in a list form which we changed into dictionary format which allowed us to run the merchant class.

7. What Did You Learn?
In this section, reflect on what you learned from this coding session. Did you gain any new insights, or were there areas you still struggled with?
Example:
I learned how to implement classes into my code, and how to bring different properties to things in my code (user, merchants, monsters).
