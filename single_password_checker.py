from zxcvbn import zxcvbn

def check_password_strength(password):
    result = zxcvbn(password)
    
    print("\n Password Strength Report")
    print("-" * 30)
    print(f"Password: {password}")
    print(f"Score (0-4): {result['score']}")
    print(f"Guesses Required: {result['guesses']}")
    print("Crack Time (offline slow hash):", result['crack_times_display']['offline_slow_hashing_1e4_per_second'])
    
    feedback = result['feedback']
    if feedback['warning']:
        print(f"\n Warning: {feedback['warning']}")
    if feedback['suggestions']:
        print("\n Suggestions:")
        for suggestion in feedback['suggestions']:
            print(f" - {suggestion}")
    print("-" * 30)

if __name__ == "__main__":
    pwd = input("Enter a password to test: ")
    check_password_strength(pwd)
