"""
# Program by Yadhav Ramsahye Sharma
# bruces_ultimate.py - The Most Ridiculously Fun Bruce Experience Ever!
#

🍺 Full Australian Experience:

Aussie slang everywhere - "Fair dinkum!", "Stone the crows!", "Ripper!"
Typewriter effects with Australian timing
Random greetings that change every time
Epic ASCII banner for Bruce's Philosophy Department

🤔 Advanced Confusion System:

Confusion Meter - calculates exactly how confusing your name is!
Multiple confused responses - different reactions each time
Alternative Bruce names - "Big Bruce-o", "Tiny Brucey", "Mad Bruce-meister"
Choice system - pick your preferred Bruce variant!

🧠 Interactive Elements:

Bruce Quiz with 3 questions about department rules
Bruce counter - see how many Bruces are in the department
Australian "facts" - hilarious made-up trivia
Session summary with stats and beer consumption!

🎭 Theatrical Flair:

Dramatic pauses with beer-drinking and hat-adjusting
Progressive confusion alerts with percentage meters
Multiple ending paths based on your choices
Bonus points for already being named Bruce

🎮 What Happens:

Epic welcome to the University of Woolloomooloo
Smart confusion analysis of your actual name
Choice of Bruce variants if you want something fancy
Optional quiz to test your Bruce knowledge
Fun facts about Australia and Bruces
Complete statistics of your Bruce transformation

🏆 Special Features:

Name analysis - checks if your name starts with 'B', has 'R' or 'U', etc.
Dynamic responses - reacts differently based on your actual name
Multiple Bruce options - not just plain "Bruce"!
Australian cultural immersion - feels like you're really there!

Try it with different names to see how the confusion meter works! Names like "Brian" get less confused than "Zachariah"! 🤣Ya
"""

import random
import time
import os

# Australian slang and expressions
AUSSIE_GREETINGS = [
    "G'day", "How ya goin'", "How's it hangin'", "What's the word", 
    "How ya been", "Crikey", "Stone the flamin' crows", "Fair dinkum"
]

AUSSIE_REACTIONS = [
    "Fair dinkum!", "Stone the crows!", "Crikey!", "Blimey!", 
    "Too right mate!", "Beauty!", "Ripper!", "Bonzer!", 
    "She'll be right!", "No worries!", "Sweet as!"
]

CONFUSED_RESPONSES = [
    "That's goin' to cause a right mess!",
    "Bloody hell, that's confusing!",
    "This is gonna be a real dog's breakfast!",
    "That'll put the cat among the pigeons!",
    "Fair dinkum, that's a head-scratcher!",
    "Stone the crows, what a pickle!"
]

BRUCE_COMPLIMENTS = [
    "Too right! A proper Bruce!",
    "Beauty mate! Classic Bruce material!",
    "Ripper choice! Bruce is bonkers good!",
    "Fair dinkum legend, that's what you are!",
    "She'll be right with a name like Bruce!",
    "No worries mate, Bruce is the way to go!"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def aussie_typewriter(text, delay=0.04):
    """Print text with Australian flair"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def dramatic_pause():
    """Add some dramatic Australian suspense"""
    pauses = ["...", "... *drinks beer* ...", "... *adjusts hat* ...", "... *thinks hard* ..."]
    aussie_typewriter(random.choice(pauses), 0.1)
    time.sleep(1)

def bruce_banner():
    """Epic ASCII banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║        🇦🇺 BRUCE'S PHILOSOPHY DEPARTMENT 🇦🇺                  ║
    ║                                                              ║
    ║           "Where everyone's a Bruce, mate!"                  ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    
    🍺 Welcome to the University of Woolloomooloo! 🍺
    
    """
    print(banner)

def count_bruces():
    """Count how many Bruces are in the department"""
    num_bruces = random.randint(15, 25)
    print(f"📊 Current Bruce count in the department: {num_bruces}")
    print("   (All named Bruce, obviously)")
    return num_bruces

def bruce_quiz():
    """Fun Australian quiz"""
    questions = [
        {
            "question": "What's the most important rule at Bruce's Philosophy Department?",
            "options": ["A) No poofters", "B) Everyone's called Bruce", "C) Drink beer", "D) All of the above"],
            "answer": "D",
            "response": "Too right mate! You've got the spirit of Bruce!"
        },
        {
            "question": "What's the proper way to greet a fellow Bruce?",
            "options": ["A) G'day Bruce!", "B) 'Ello Bruce!", "C) How ya goin' Bruce?", "D) All sound good, Bruce!"],
            "answer": "D", 
            "response": "Beauty! You're a natural Bruce!"
        },
        {
            "question": "If someone's not called Bruce, what do we do?",
            "options": ["A) Call 'em Bruce anyway", "B) Get confused", "C) Have a beer about it", "D) All of the above"],
            "answer": "D",
            "response": "Ripper! You understand the Bruce philosophy!"
        }
    ]
    
    score = 0
    for i, q in enumerate(questions):
        print(f"\n🤔 Bruce Question {i+1}:")
        aussie_typewriter(q["question"])
        for option in q["options"]:
            print(f"   {option}")
        
        answer = input("\nYour answer, Bruce: ").upper().strip()
        
        if answer == q["answer"]:
            aussie_typewriter(f"🎉 {q['response']}")
            score += 1
        else:
            aussie_typewriter(f"😅 Nah mate, but no worries! {random.choice(AUSSIE_REACTIONS)}")
        
        dramatic_pause()
    
    return score

def bruce_name_generator():
    """Generate ridiculous Bruce variations"""
    prefixes = ["Big", "Little", "Tiny", "Huge", "Mad", "Wild", "Crikey", "Fair Dinkum"]
    suffixes = ["Bruce", "Brucey", "Bruce-o", "Brucearoo", "Bruce-meister"]
    
    return f"{random.choice(prefixes)} {random.choice(suffixes)}"

def australian_facts():
    """Share some fun 'facts' about Australia"""
    facts = [
        "🦘 Did you know? 73% of all Australians are named Bruce!",
        "🍺 Beer was actually invented by a bloke named Bruce in 1847!",
        "🐨 Koalas can only understand you if you call them Bruce!",
        "🏄‍♂️ The first person to surf was definitely a Bruce!",
        "🎣 Crocodile Dundee's real name? You guessed it... Bruce!",
        "🇦🇺 Australia was originally going to be called 'Bruceland'!"
    ]
    
    fact = random.choice(facts)
    aussie_typewriter(f"\n🧠 Bruce Fact: {fact}")

def confusion_meter(name):
    """Calculate confusion level"""
    if name.lower() == "bruce":
        return 0
    
    # More confusing if name is very different from Bruce
    confusion_factors = {
        'starts_with_b': -20 if name.lower().startswith('b') else 10,
        'has_r': -10 if 'r' in name.lower() else 5,
        'has_u': -10 if 'u' in name.lower() else 5,
        'length': abs(len(name) - 5) * 3,
        'complexity': len(set(name.lower())) * 2
    }
    
    base_confusion = 50
    total_confusion = base_confusion + sum(confusion_factors.values())
    return max(0, min(100, total_confusion))

def main():
    """The ultimate Bruce experience"""
    clear_screen()
    bruce_banner()
    
    # Count the Bruces
    num_bruces = count_bruces()
    time.sleep(1)
    
    # The greeting with more Australian flair
    greeting = random.choice(AUSSIE_GREETINGS)
    aussie_typewriter(f"\n{greeting} cobber! Welcome to our humble department!")
    time.sleep(0.5)
    
    # Get the name with style
    print("\n" + "="*60)
    aussie_typewriter("🎤 Now then, let's sort out this name business...")
    name = input("\n🇦🇺 Hey mate, what's your name? ")
    
    if not name.strip():
        aussie_typewriter("😅 Bit shy, eh? No worries, we'll call ya Bruce!")
        name = "Bruce"
    
    # Calculate confusion meter
    confusion_level = confusion_meter(name)
    
    if name.lower() != "bruce":
        print(f"\n⚠️  CONFUSION ALERT! ⚠️")
        print(f"Confusion Level: {confusion_level}% 📊")
        
        # Dramatic confusion sequence
        confused_response = random.choice(CONFUSED_RESPONSES)
        aussie_typewriter(f"\nBruce: {confused_response}")
        dramatic_pause()
        
        aussie_typewriter(f"Sorry {name} - your name's not Bruce?")
        aussie_typewriter("That's goin' to cause a little confusion.")
        
        # More dramatic effect
        print("\n🤔 Let me think about this...")
        for i in range(3):
            print("." * (i + 1), end='', flush=True)
            time.sleep(0.8)
        print()
        
        aussie_typewriter("Mind if we call you 'Bruce' to keep it clear?")
        
        # Offer alternative Bruce names
        alt_bruce = bruce_name_generator()
        aussie_typewriter(f"Or how about '{alt_bruce}'? That's got a nice ring to it!")
        
        choice = input(f"\nDo you want to be 'Bruce' or '{alt_bruce}'? ").strip()
        
        if alt_bruce.lower() in choice.lower():
            name = alt_bruce
            aussie_typewriter(f"🎉 {random.choice(BRUCE_COMPLIMENTS)}")
        else:
            name = "Bruce"
            aussie_typewriter("🍺 Classic choice! Bruce it is!")
            
    else:
        # They're already Bruce!
        compliment = random.choice(BRUCE_COMPLIMENTS)
        aussie_typewriter(f"🎊 Excellent! {compliment}")
        aussie_typewriter("That saves a lot of confusion!")
        
        # Bonus points for being Bruce
        aussie_typewriter(f"🏆 You're Bruce number {num_bruces + 1} in our department!")
    
    # The grand finale
    print("\n" + "🍺" * 20)
    final_greeting = random.choice(AUSSIE_GREETINGS)
    aussie_typewriter(f"\n🎉 {final_greeting} {name}!!!")
    
    # Share a fun fact
    australian_facts()
    
    # Optional quiz for extra fun
    print(f"\n{'='*60}")
    quiz_choice = input("🧠 Want to take the Official Bruce Quiz, mate? (y/n): ").lower()
    
    if quiz_choice in ['y', 'yes', 'yeah', 'too right']:
        print(f"\n🎓 Welcome to Bruce University, {name}!")
        score = bruce_quiz()
        
        if score == 3:
            aussie_typewriter(f"🏆 Perfect score! You're a true blue Bruce, {name}!")
        elif score == 2:
            aussie_typewriter(f"🥈 Good on ya! You're definitely Bruce material!")
        else:
            aussie_typewriter(f"🍺 No worries mate, you'll get the hang of being Bruce!")
    
    # Final statistics
    print(f"\n📈 SESSION SUMMARY:")
    print(f"Original name: {input('What was your original name again? ') if name == 'Bruce' else 'Not Bruce'}")
    print(f"Current Bruce status: {name}")
    print(f"Confusion eliminated: {100 - confusion_level}%")
    print(f"Beers virtually consumed: {random.randint(1, 5)} 🍺")
    print(f"Bruce level: Maximum 🇦🇺")
    
    aussie_typewriter(f"\n🎊 Thanks for visiting Bruce's Philosophy Department!")
    aussie_typewriter("Remember: No matter what your name is, you're always a Bruce to us!")
    aussie_typewriter("She'll be right, mate! 🇦🇺🍺")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n🍺 No worries Bruce, catch ya later! 🇦🇺")
    except Exception as e:
        print(f"\n😅 Crikey! Something went a bit wonky: {e}")
        print("But she'll be right, mate! 🍺")