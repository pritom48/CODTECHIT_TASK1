import re

def calculate_password_strength(password):
  
    length_criteria = len(password) >= 8
    lower_case_criteria = re.search("[a-z]", password)
    upper_case_criteria = re.search("[A-Z]", password)
    digit_criteria = re.search("[0-9]", password)
    special_char_criteria = re.search("[@#$%^&+=]", password)
    unique_chars_criteria = len(set(password)) >= 5

    
    score = 0
    if length_criteria:
        score += 1
    if lower_case_criteria:
        score += 1
    if upper_case_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_char_criteria:
        score += 1
    if unique_chars_criteria:
        score += 1

    # feedback 
    if score == 6:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lower_case_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not upper_case_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not digit_criteria:
        feedback.append("Password should contain at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character (@#$%^&+=).")
    if not unique_chars_criteria:
        feedback.append("Password should contain at least 5 unique characters.")

    return strength, feedback

def main():
    password = input("Enter a password to assess its strength: ")
    strength, feedback = calculate_password_strength(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")

if __name__ == "__main__":
    main()
