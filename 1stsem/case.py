mood = "happy"
mood = "sad"

mood = str(input("What is your mood today?: "))

match mood:
    case "happy":
        print("Great to see you smile!")
    case "sad":
        print("I'm here if you want to talk.")
    case "angry":
        print("Everything will be okay, take a deep breath.")
    case "excited":
        print("That's great! enjoy the moment!")
    case _:
        print("I don't quite understand how you feel.")
