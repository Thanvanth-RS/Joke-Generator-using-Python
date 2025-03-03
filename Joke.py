import random

def get_joke():
    jokes = [
        "Why did the TikTok go to therapy? It had too many issues to scroll through!",
        "Why don't skeletons fight each other? Because they don't have the guts... just vibes!",
        "Me: I should sleep. Also me at 3 AM: Do fish get thirsty?",
        "Why did the Gen Z kid bring a ladder to the bar? Because the vibes were too low!",
        "Ghosting my responsibilities like it's a toxic situationship!"
        "Why did the TikTok go to therapy? It had too many issues to scroll through!",
        "Why don't skeletons fight each other? Because they don't have the guts... just vibes!",
        "Me: I should sleep. Also me at 3 AM: Do fish get thirsty?",
        "Why did the Gen Z kid bring a ladder to the bar? Because the vibes were too low!",
        "Ghosting my responsibilities like it's a toxic situationship!"
    ]
    return random.choice(jokes)

if __name__ == "__main__":
    print("Here's a joke for you:")
    print(get_joke())
