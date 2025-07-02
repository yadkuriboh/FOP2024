"""
# bridge.py - a scene from The Holy Grail (Enhanced Edition!)
🎭 Fun Features Added:

Typewriter effect - Text appears letter by letter for drama
Random bridge keeper responses - He reacts differently each time
Smart judgment system - The bridge keeper actually evaluates your answers!
Emojis and formatting - Makes it more visually engaging
Multiple endings - Different outcomes based on your quest
Easter egg - Hidden reference to the "African or European swallow" joke

🎮 How it works:

Still asks the same three questions
Bridge keeper now responds with mysterious comments
Your answers actually matter - dangerous quests might get you thrown off!
Beautiful formatted summary at the end
Keeps the original spirit but adds suspense
"""

import random
import time

def dramatic_print(text, delay=0.03):
    """Print text with a typewriter effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def bridge_keeper_response():
    """Random responses from the bridge keeper"""
    responses = [
        "Hmm... interesting answer...",
        "*strokes beard thoughtfully*",
        "The bridge keeper nods slowly...",
        "*writing something down mysteriously*",
        "Most peculiar indeed..."
    ]
    return random.choice(responses)

def final_judgment(name, quest, colour):
    """Determine if the traveler may pass"""
    dangerous_quests = ["destroy", "conquer", "eliminate", "kill"]
    safe_colors = ["blue", "green", "yellow", "red", "purple", "orange"]
    
    # Check for dangerous intentions
    quest_dangerous = any(word in quest.lower() for word in dangerous_quests)
    
    # Bridge keeper is suspicious of certain colors
    suspicious_color = colour.lower() not in safe_colors
    
    if quest_dangerous:
        return "bridge_throw"
    elif suspicious_color and random.random() > 0.7:
        return "trick_question"
    else:
        return "pass"

# Dramatic opening
print("=" * 50)
dramatic_print("🏰 WELCOME TO THE BRIDGE OF DEATH 🏰")
print("=" * 50)
print()
dramatic_print("A mysterious figure emerges from the mist...")
dramatic_print("'STOP! Who would cross the Bridge of Death")
dramatic_print("must answer me these questions three,")
dramatic_print("ere the other side he see!'")
print()

# Question 1
dramatic_print("BRIDGE KEEPER: What... is your name?")
name = input("🗣️  ")
print(f"📝 {bridge_keeper_response()}")
print()

# Question 2
dramatic_print("BRIDGE KEEPER: What... is your quest?")
quest = input("⚔️  ")
print(f"📝 {bridge_keeper_response()}")
print()

# Question 3
dramatic_print("BRIDGE KEEPER: What... is your favourite colour?")
colour = input("🎨  ")
print(f"📝 {bridge_keeper_response()}")
print()

# Processing phase
dramatic_print("The Bridge Keeper studies your answers carefully...")
time.sleep(2)
print("🤔 Hmm...")
time.sleep(1)

# Final judgment
judgment = final_judgment(name, quest, colour)

print("=" * 30)
dramatic_print("THE VERDICT:")
print("=" * 30)

if judgment == "bridge_throw":
    dramatic_print("BRIDGE KEEPER: 'Your quest sounds rather... EVIL!'")
    dramatic_print("'AIIIEEEEEE!' *throws you off the bridge*")
    print("💀 You have been cast into the gorge!")
    print("🔄 Perhaps try a more noble quest next time...")
    
elif judgment == "trick_question":
    dramatic_print(f"BRIDGE KEEPER: '{colour.title()}? What do you mean?")
    dramatic_print("African or European blue?' (Just kidding!)")
    time.sleep(1)
    dramatic_print("*chuckles* 'Just testing you...'")
    print("✅ You may pass!")
    
else:
    dramatic_print("BRIDGE KEEPER: 'Right! Off you go!'")
    print("✅ You may cross the Bridge of Death!")

print()
print("=" * 50)
print("📊 YOUR ADVENTURE SUMMARY:")
print("=" * 50)
print(f"🏷️  Knight's Name: {name}")
print(f"🎯 Noble Quest: {quest}")
print(f"🌈 Favorite Color: {colour}")
print()

if judgment != "bridge_throw":
    print(f"✨ Congratulations, {name}!")
    print(f"🎉 Good luck with your {quest} quest!")
    print(f"👕 Perhaps wearing {colour} armor would help! :)")
    print()
    dramatic_print("🎵 *Coconut hooves clip-clop into the distance...*")
else:
    print("💡 TIP: Try a quest that doesn't involve harming others!")

print()
print("Thanks for playing! 🏰✨")