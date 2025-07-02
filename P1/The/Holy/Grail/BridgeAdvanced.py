#
# bridge_advanced.py - The Holy Grail Bridge Scene (ULTIMATE EDITION!)
#

import random
import time
import os
import sys
from datetime import datetime
import threading

class Colors:
    """ANSI color codes for terminal styling"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'

class BridgeKeeper:
    def __init__(self):
        self.responses = [
            "🤔 Hmm... interesting answer...",
            "📝 *strokes beard thoughtfully*",
            "👁️ The bridge keeper's eyes narrow...",
            "📜 *writing something down mysteriously*",
            "⚡ Most peculiar indeed...",
            "🧙‍♂️ *nods slowly while muttering*",
            "🔮 The crystal ball glows faintly...",
            "⚖️ *weighs your words carefully*"
        ]
        
        self.dramatic_pauses = [
            "The mist swirls ominously...",
            "Ravens caw in the distance...",
            "The bridge creaks under an unseen weight...",
            "A cold wind whistles through the gorge...",
            "Ancient stones whisper secrets...",
            "Thunder rumbles far away..."
        ]

    def respond(self):
        return random.choice(self.responses)
    
    def dramatic_pause(self):
        return random.choice(self.dramatic_pauses)

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_print(text, delay=0.03, color=""):
    """Print text with typewriter effect and optional color"""
    print(color, end='')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(Colors.ENDC)

def animated_print(text, style="normal"):
    """Print with different animation styles"""
    if style == "dramatic":
        typewriter_print(text, 0.05, Colors.BOLD + Colors.HEADER)
    elif style == "keeper":
        typewriter_print(text, 0.04, Colors.WARNING + Colors.BOLD)
    elif style == "success":
        typewriter_print(text, 0.03, Colors.OKGREEN + Colors.BOLD)
    elif style == "danger":
        typewriter_print(text, 0.03, Colors.FAIL + Colors.BOLD)
    elif style == "mystical":
        typewriter_print(text, 0.06, Colors.OKCYAN + Colors.BOLD)
    else:
        typewriter_print(text, 0.03)

def create_border(text, char="=", color=Colors.HEADER):
    """Create a decorative border around text"""
    width = len(text) + 4
    border = char * width
    
    print(color + border + Colors.ENDC)
    print(color + char + " " + text + " " + char + Colors.ENDC)
    print(color + border + Colors.ENDC)

def progress_bar(current, total, length=30):
    """Display a progress bar"""
    percent = current / total
    filled = int(length * percent)
    bar = "█" * filled + "░" * (length - filled)
    print(f"\r{Colors.OKCYAN}Progress: [{bar}] {percent:.0%}{Colors.ENDC}", end='', flush=True)
    time.sleep(0.5)
    print()

def loading_animation(text, duration=2):
    """Show a loading animation"""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    
    while time.time() < end_time:
        for char in chars:
            print(f"\r{Colors.OKCYAN}{char} {text}...{Colors.ENDC}", end='', flush=True)
            time.sleep(0.1)
            if time.time() >= end_time:
                break
    print(f"\r{Colors.OKGREEN}✓ {text} complete!{Colors.ENDC}")

def ascii_art_castle():
    """Display ASCII art castle"""
    castle = f"""{Colors.HEADER}
        🏰 THE BRIDGE OF DEATH 🏰
    
    ⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⢰⣶⣶⡆⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀
    ⠀⣰⣶⣶⣶⣶⣾⣿⣿⣿⣷⣶⣶⣾⣿⣿⣷⣶⣶⣾⣿⣿⣿⣷⣶⣶⣶⣶⡆
    ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⠀⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋
    
        "None shall pass without answering truly!"
    {Colors.ENDC}"""
    
    print(castle)

def get_stylized_input(prompt, emoji=""):
    """Get input with stylized prompt"""
    full_prompt = f"{Colors.BOLD}{Colors.OKCYAN}{emoji} {prompt}: {Colors.ENDC}"
    return input(full_prompt).strip()

def dramatic_evaluation(name, quest, color):
    """Dramatically evaluate the answers with multiple criteria"""
    print("\n" + "="*60)
    animated_print("🔮 THE BRIDGE KEEPER CONTEMPLATES YOUR FATE...", "mystical")
    print("="*60)
    
    # Analysis categories
    categories = {
        "Name Worthiness": 0,
        "Quest Nobility": 0,
        "Color Mysticism": 0,
        "Overall Aura": 0
    }
    
    # Analyze name
    loading_animation("Analyzing your name's power")
    noble_names = ["sir", "lady", "knight", "lord", "dame", "arthur", "lancelot", "galahad"]
    if any(noble in name.lower() for noble in noble_names):
        categories["Name Worthiness"] = 85 + random.randint(0, 15)
        animated_print(f"✨ '{name}' carries the weight of nobility!", "success")
    elif len(name) > 15:
        categories["Name Worthiness"] = 70 + random.randint(0, 20)
        animated_print(f"🎭 Such an elaborate name shows character!", "keeper")
    else:
        categories["Name Worthiness"] = 50 + random.randint(0, 30)
        animated_print(f"🤔 '{name}' is... adequate.", "keeper")
    
    progress_bar(1, 4)
    
    # Analyze quest
    loading_animation("Weighing your quest's righteousness")
    evil_words = ["destroy", "kill", "conquer", "eliminate", "murder", "harm", "steal", "revenge"]
    noble_words = ["help", "save", "protect", "heal", "find", "seek", "grail", "peace", "love"]
    
    if any(evil in quest.lower() for evil in evil_words):
        categories["Quest Nobility"] = 10 + random.randint(0, 20)
        animated_print(f"⚔️ Your quest reeks of darkness and malice!", "danger")
    elif any(noble in quest.lower() for noble in noble_words):
        categories["Quest Nobility"] = 80 + random.randint(0, 20)
        animated_print(f"🌟 Your quest shines with pure intentions!", "success")
    else:
        categories["Quest Nobility"] = 60 + random.randint(0, 25)
        animated_print(f"⚖️ Your quest is... curious.", "keeper")
    
    progress_bar(2, 4)
    
    # Analyze color
    loading_animation("Reading the mystical properties of your color")
    mystical_colors = ["purple", "violet", "gold", "silver", "azure", "crimson"]
    common_colors = ["red", "blue", "green", "yellow", "orange", "black", "white"]
    
    if any(mystical in color.lower() for mystical in mystical_colors):
        categories["Color Mysticism"] = 90 + random.randint(0, 10)
        animated_print(f"🔮 {color.title()} resonates with ancient magic!", "mystical")
    elif any(common in color.lower() for common in common_colors):
        categories["Color Mysticism"] = 60 + random.randint(0, 25)
        animated_print(f"🎨 {color.title()} is a classic choice.", "keeper")
    else:
        categories["Color Mysticism"] = 40 + random.randint(0, 35)
        animated_print(f"🤨 '{color}'... what manner of color is this?", "keeper")
    
    progress_bar(3, 4)
    
    # Overall aura calculation
    loading_animation("Calculating your spiritual aura")
    base_aura = sum(categories.values()) // 3
    time_bonus = 5 if datetime.now().hour in [12, 0] else 0  # Noon or midnight bonus
    length_penalty = -10 if len(name + quest + color) < 20 else 0
    
    categories["Overall Aura"] = max(0, min(100, base_aura + time_bonus + length_penalty))
    
    progress_bar(4, 4)
    
    # Display detailed analysis
    print(f"\n{Colors.BOLD}{Colors.HEADER}📊 MYSTICAL ANALYSIS RESULTS:{Colors.ENDC}")
    print("─" * 50)
    
    for category, score in categories.items():
        bar_length = 20
        filled = int((score / 100) * bar_length)
        bar = "█" * filled + "░" * (bar_length - filled)
        
        if score >= 80:
            color_code = Colors.OKGREEN
        elif score >= 60:
            color_code = Colors.WARNING
        else:
            color_code = Colors.FAIL
            
        print(f"{category:.<20} {color_code}[{bar}] {score:>3}%{Colors.ENDC}")
    
    return categories

def determine_fate(analysis, name, quest, color):
    """Determine final fate based on analysis"""
    overall_score = analysis["Overall Aura"]
    quest_score = analysis["Quest Nobility"]
    
    print(f"\n{Colors.BOLD}🎭 THE MOMENT OF TRUTH ARRIVES...{Colors.ENDC}")
    time.sleep(2)
    
    # Create suspenseful countdown
    for i in range(3, 0, -1):
        print(f"\r{Colors.BLINK}{Colors.BOLD}{i}...{Colors.ENDC}", end='', flush=True)
        time.sleep(1)
    print(f"\r{Colors.BOLD}⚡ JUDGMENT! ⚡{Colors.ENDC}")
    
    if quest_score < 30:  # Evil quest
        create_border("💀 CAST INTO THE GORGE! 💀", "☠", Colors.FAIL)
        animated_print("BRIDGE KEEPER: 'Your quest reeks of evil!'", "danger")
        animated_print("'AIIIEEEEEE!' *hurls you into the abyss*", "danger")
        
        print(f"\n{Colors.FAIL}💀 DEATH REPORT:")
        print(f"Name: {name}")
        print(f"Evil Quest: {quest}")
        print(f"Final Color: {color}")
        print(f"Corruption Level: {100 - quest_score}%")
        print(f"💡 Moral: Perhaps choose a nobler path next time!{Colors.ENDC}")
        
        return "death"
        
    elif overall_score < 50:  # Trick question territory
        create_border("🤔 TRICK QUESTION TIME! 🤔", "?", Colors.WARNING)
        animated_print(f"BRIDGE KEEPER: '{color}? What do you mean?'", "keeper")
        animated_print("'African or European blue?'", "keeper")
        time.sleep(2)
        animated_print("*chuckles* 'Just testing you... Off you go!'", "keeper")
        
        print(f"\n{Colors.WARNING}🎭 BARELY ESCAPED:")
        print(f"Knight: {name}")
        print(f"Quest: {quest}")
        print(f"Suspicious Color: {color}")
        print(f"Luck Factor: {random.randint(60, 90)}%")
        print(f"🥥 *Coconut hooves fade into the distance...*{Colors.ENDC}")
        
        return "trick"
        
    else:  # Success!
        create_border("✅ YOU MAY PASS! ✅", "⭐", Colors.OKGREEN)
        animated_print("BRIDGE KEEPER: 'You have answered wisely!'", "success")
        animated_print("'Right! Off you go, noble traveler!'", "success")
        
        print(f"\n{Colors.OKGREEN}🏆 VICTORY SUMMARY:")
        print(f"Champion: {name}")
        print(f"Noble Quest: {quest}")
        print(f"Chosen Color: {color}")
        print(f"Wisdom Score: {overall_score}%")
        print(f"✨ May your {quest} quest bring you glory!")
        print(f"👕 Perhaps {color} armor would serve you well!{Colors.ENDC}")
        
        return "success"

def save_adventure_log(name, quest, color, result, analysis):
    """Save the adventure to a log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("bridge_adventures.log", "a", encoding='utf-8') as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"BRIDGE ADVENTURE LOG - {timestamp}\n")
        f.write(f"{'='*60}\n")
        f.write(f"Name: {name}\n")
        f.write(f"Quest: {quest}\n")
        f.write(f"Color: {color}\n")
        f.write(f"Result: {result.upper()}\n")
        f.write(f"Analysis Scores:\n")
        for category, score in analysis.items():
            f.write(f"  - {category}: {score}%\n")
        f.write(f"{'='*60}\n")

def play_again_prompt():
    """Ask if player wants to play again with style"""
    print(f"\n{Colors.BOLD}{Colors.OKCYAN}🔄 Would you dare face the Bridge Keeper again?{Colors.ENDC}")
    choice = get_stylized_input("Enter 'yes' to continue your adventures", "⚔️")
    return choice.lower() in ['yes', 'y', 'yeah', 'yep', 'sure', 'absolutely']

def main():
    """Main game loop with full experience"""
    
    while True:
        clear_screen()
        
        # Epic opening
        ascii_art_castle()
        time.sleep(1)
        
        # Initialize bridge keeper
        keeper = BridgeKeeper()
        
        animated_print("\nA mysterious figure emerges from the ancient mists...", "dramatic")
        time.sleep(1)
        animated_print("The Bridge Keeper's eyes pierce through your very soul...", "mystical")
        time.sleep(1)
        
        create_border("THE CHALLENGE BEGINS", "⚔", Colors.HEADER)
        
        # The three questions with keeper responses
        questions = [
            ("What... is your name?", "🗣️"),
            ("What... is your quest?", "⚔️"),
            ("What... is your favourite colour?", "🎨")
        ]
        
        answers = []
        
        for i, (question, emoji) in enumerate(questions):
            animated_print(f"\nBRIDGE KEEPER: {question}", "keeper")
            answer = get_stylized_input(question.replace("What... is your ", "").replace("?", ""), emoji)
            
            if not answer:
                animated_print("You must answer the Bridge Keeper!", "danger")
                continue
                
            answers.append(answer)
            
            # Keeper response
            if i < len(questions) - 1:  # Not the last question
                time.sleep(0.5)
                animated_print(keeper.respond(), "mystical")
                time.sleep(1)
                animated_print(keeper.dramatic_pause(), "normal")
                time.sleep(1)
        
        name, quest, color = answers
        
        # Dramatic evaluation
        analysis = dramatic_evaluation(name, quest, color)
        
        # Final judgment
        result = determine_fate(analysis, name, quest, color)
        
        # Save to log
        try:
            save_adventure_log(name, quest, color, result, analysis)
            print(f"\n{Colors.OKCYAN}📝 Adventure logged to 'bridge_adventures.log'{Colors.ENDC}")
        except:
            pass  # Silent fail if can't write log
        
        # Play again?
        if not play_again_prompt():
            break
    
    # Epic farewell
    print(f"\n{Colors.BOLD}{Colors.HEADER}")
    animated_print("🏰 Farewell, brave adventurer!", "dramatic")
    animated_print("The Bridge of Death awaits your return...", "mystical")
    print(f"{'='*50}{Colors.ENDC}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.FAIL}👋 The Bridge Keeper vanishes into the mist...{Colors.ENDC}")
    except Exception as e:
        print(f"\n{Colors.FAIL}⚠️ The ancient magic faltered: {e}{Colors.ENDC}")