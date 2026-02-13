"""
Handwritten Digit Prediction
Author: Vishnu K
Description:
This project predicts handwritten digits (0–9) using Machine Learning
and Deep Learning techniques. It includes data preprocessing, model
training, evaluation, and prediction workflows.
"""

def show_menu():
    print("\n==== Handwritten Digit Prediction ====")
    print("1. Train the model")
    print("2. Evaluate the model")
    print("3. Predict a handwritten digit")
    print("4. Exit")

def main():
    print("Welcome to Handwritten Digit Prediction Project")

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Training the model... (run notebook or training script)")
        elif choice == "2":
            print("Evaluating the model... (confusion matrix & accuracy)")
        elif choice == "3":
            print("Predicting digit... (load model & input image)")
        elif choice == "4":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
