# ask question to the user
def ask_question():
    question = input("Please enter your Question: ")
    return question

# process the question and return a dictionary of the results
def processQuestion():
    question = ask_question()
    
    # the word count
    question_split = question.split()
    word_count = len(question_split)
    print("Word count is:", word_count)

    # the character count
    character_count = len(question)
    print("Character count is:", character_count)

    # the type of question - What, Why, When, Who, Where and How
    question_types = ["What", "Why", "When", "Who", "Where", "How"]
    detected_type = "Unknown"
    
    for q_type in question_types:
        # Using .lower() checks to make it case-insensitive (e.g., 'what' or 'What')
        if q_type.lower() in question.lower():
            detected_type = q_type
            print("Type of question is:", detected_type)
            break

    # check if the question is valid or not
    validationCheck = "Valid" if detected_type != "Unknown" else "Invalid"
    print("The question is:", validationCheck)

    # package into a result dictionary
    result = {
        "question": question,
        "wordCount": word_count,
        "characterCount": character_count,
        "typeOfQuestion": detected_type,
        "isQuestionValid": validationCheck
    }
    
    print("Final response:", result)
    return result

# Main loop handling execution and accumulation of results
def main():
    all_results = []  # List to store every processed question dictionary
    
    while True:
        # Run processing and append the resulting dict to our collection
        single_result = processQuestion()
        all_results.append(single_result)
        
        # Ask user if they want to continue
        response = input("Would you like to ask another question? (y/n): ").strip().lower()
        
        if response == 'y':
            print("continuing....")
        elif response == 'n':
            print("Exiting function")
            break
        else:
            print("Please answer with 'y' or 'n'")
            
    print("\nAll collected results history:")
    print(all_results)

# Run the program
main()