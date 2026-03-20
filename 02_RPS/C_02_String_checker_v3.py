# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from t    he following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

            # print error if user does not enter something that's valid
            print(error)
            print()


# Main routine goes here

rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker(question="Do you want to see the instructions? ",
                                   yes_no)

print("You chose: ", want_instructions)

user_choice = string_checker(question="Choose: ", rps_list)
print("You chose: ", user_choice)
