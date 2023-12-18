
#Lists
#There are seven functions required for this lab. A list must be used to store
#and process all test scores. All output must be the same as in the sample
#screenshots provided below.

#starting by creating the input fucntion for the scores 
def input_scores():
    # Function to input test scores from the user
    num_scores = int(input("How many test scores will you be entering: "))
    #while loop to test the score of if it is between 0-100
    while num_scores <= 0:
        print("Invalid input. Number of test scores must be greater than zero.")
        num_scores = int(input("How many test scores will you be entering: "))

    scores = []
    for i in range(num_scores):
        score = int(input(f"Enter test score {i + 1}(0-100): "))
        while not (0 <= score <= 100):
            print("Invalid input. Test score must be between 0 and 100.")
            score = int(input(f"Enter test score {i + 1}(0-100): "))
        scores.append(score)

    return scores


def display_menu():
    # Function to display the main menu options
    print("\nMenu:")
    print("1. Display test scores")
    print("2. Calculate score metrics")
    print("3. Mine scores (high and low)")
    print("4. Update a test score")
    print("5. Display scores in reverse order")
    print("6. Quit")


def score_metrics(scores):
    # Function to calculate highest, lowest, and average scores
    max_score = max(scores)
    min_score = min(scores)
    average_score = sum(scores) / len(scores)

    print("\nScore Metrics:")
    print(f"Highest Test Score: {max_score}")
    print(f"Lowest Test Score: {min_score}")
    print(f"Average Test Score: {average_score:.2f}")


def mine_scores(scores):
    # Function to mine and display high and low test scores based on average score
    average_score = sum(scores) / len(scores)
    high_scores = [score for score in scores if score >= average_score]
    low_scores = [score for score in scores if score < average_score]
    high_scores.sort()
    low_scores.sort()

    print("\nHigh Test Scores:")
    print(high_scores)
    print("\nLow Test Scores:")
    print(low_scores)


def update_score(scores):
    # Function to update a specific test score
    print("\nCurrent Test Scores:")
    for i, score in enumerate(scores):
        print(f"{i + 1}. {score}")

    index = int(input("\nEnter the number of the score to update: ")) - 1
    while not (0 <= index < len(scores)):
        print("Invalid input. Enter a valid number of the score to update.")
        index = int(input("\nEnter the number of the score to update: ")) - 1

    new_score = int(input("Enter the new test score: "))
    while not (0 <= new_score <= 100):
        print("Invalid input. Test score must be between 0 and 100.")
        new_score = int(input("Enter the new test score: "))

    scores[index] = new_score

    print("\nUpdated Test Scores:")
    for i, score in enumerate(scores):
        print(f"{i + 1}. {score}")


def display_scores(scores):
    # Function to display the test scores in reverse order
    print("\nTest Scores in Reverse Order:")
    for score in scores[::-1]:
        print(score)


def main():
    # Main program function that calls other functions based on user input
    test_scores = input_scores()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nTest Scores:")
            for i, score in enumerate(test_scores):
                print(f"{i + 1}. {score}")
        elif choice == '2':
            score_metrics(test_scores)
        elif choice == '3':
            mine_scores(test_scores)
        elif choice == '4':
            update_score(test_scores)
        elif choice == '5':
            display_scores(test_scores)
        elif choice == '6':
            print("\nThank you for using this program.")
            break
        else:
            print("Invalid choice. Please enter a valid menu option.")


if __name__ == "__main__":
    main()


