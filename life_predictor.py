import time
import sys

# Typing effect
def type_writer(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def predict_death():
    type_writer("🔮 Welcome to the Ultimate Life Predictor 3000! 🔮\n")
    time.sleep(1)
    type_writer("Just a fun simulation. Don't take it too seriously! 😄\n")
    
    name = input("Enter your name: ")
    age = int(input("Enter your current age: "))
    gender = input("Gender (M/F/Other): ").strip().upper()
    smoker = input("Do you smoke? (yes/no): ").strip().lower()
    exercise = input("How often do you exercise? (daily/weekly/never): ").strip().lower()
    diet = input("How is your diet? (good/average/poor): ").strip().lower()
    alcohol = input("Do you drink alcohol? (yes/no): ").strip().lower()
    sleep = int(input("How many hours do you sleep daily?: "))

    type_writer("\nAnalyzing your lifestyle... 🧠", 0.05)
    time.sleep(2)

    base_life = 80
    life_score = 50

    # Lifestyle impacts
    if smoker == "yes":
        base_life -= 10
        life_score -= 20
    else:
        life_score += 10

    if exercise == "daily":
        base_life += 5
        life_score += 15
    elif exercise == "weekly":
        base_life += 2
        life_score += 5
    else:
        base_life -= 3
        life_score -= 5

    if diet == "good":
        base_life += 4
        life_score += 10
    elif diet == "poor":
        base_life -= 4
        life_score -= 10

    if alcohol == "yes":
        base_life -= 3
        life_score -= 5

    if sleep < 6:
        base_life -= 2
        life_score -= 5
    elif 6 <= sleep <= 9:
        base_life += 1
        life_score += 5
    else:
        base_life -= 1

    # Ensure values are in bounds
    predicted_age = max(age + 1, min(base_life, 100))
    life_score = max(0, min(life_score, 100))

    time.sleep(1)
    type_writer("\n📜 Generating your personalized death certificate...\n", 0.04)
    time.sleep(2)

    print("╔══════════════════════════════════════╗")
    print(f"║ 👤 Name: {name:<30}║")
    print(f"║ 🎂 Current Age: {age:<24}║")
    print(f"║ 🧬 Gender: {gender:<28}║")
    print(f"║ ⚰️ Estimated Death Age: {int(predicted_age):<18}║")
    print(f"║ 💯 Life Score: {life_score}/100{' ' * (22 - len(str(life_score)))}║")
    print("╚══════════════════════════════════════╝\n")

    if predicted_age >= 90:
        type_writer("🟢 Wow! You’re on track to outlive us all. Keep it up! 🚀")
    elif predicted_age >= 75:
        type_writer("🟡 You're doing okay, but there's room for improvement. 🏃‍♂️🥗")
    else:
        type_writer("🔴 Uh-oh! Your lifestyle might be cutting things short... 🧟")

    # Personalized suggestion
    type_writer("\n💡 Health Tip of the Day:")
    if life_score < 40:
        type_writer("Try quitting smoking, drinking more water, and walking 20 minutes a day. 🌿")
    elif 40 <= life_score <= 70:
        type_writer("You're on the right track! More exercise & sleep can do wonders. 😴🏋️‍♂️")
    else:
        type_writer("Just don’t start a TikTok health channel... You're doing great already! 😄")

    type_writer("\nThanks for using Life Predictor 3000. Stay healthy and stay awesome! ❤️")

# Run it
predict_death()
