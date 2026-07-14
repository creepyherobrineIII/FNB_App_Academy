while True:
    score = input("Enter a score (next to the cursor): ").strip()

    if score.lower() == "stop":
        print("Game session ended!")
        break
    else:
        score_int = int(score)

        if score_int > 100:
            print("Wow! That's a new high score!")
        else:
            print("Good try, keep playing!")