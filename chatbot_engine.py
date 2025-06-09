def get_response(user_input):
    user_input = user_input.lower()
    
    if "reset password" in user_input:
        return "To reset your password, go to the login screen and click on 'Forgot Password'."
    elif "check my bill" in user_input:
        return "You can view your bill by logging into your account and selecting 'Billing'."
    elif "update phone number" in user_input:
        return "Navigate to 'Profile Settings' and click 'Update Phone Number'."
    elif "speak to human" in user_input or "not helpful" in user_input:
        return "Please hold while we connect you to a customer care executive."
    else:
        return "Sorry, I didn't understand that. Would you like to speak to a human agent?"
