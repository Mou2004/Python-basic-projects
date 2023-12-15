def mad_libs():
    print("Welcome to Mad Libs!")
    
    # Get user input--
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    # Display the story 
    story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}."
    print("\nYour Mad Libs story:")
    print(story)

if __name__ == "__main__":
    mad_libs()
