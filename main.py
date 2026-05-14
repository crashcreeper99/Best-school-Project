# Programmers: Lamar,Rasheed,and mira
# Course: Intro to computer science
# Due Date: 4/27/2026
# Lab Assignment: PA-5
# Problem Statement: read file compare and answer questions and make a graph
# Data In:the number of the question users want to anwser
# Data Out: the answer to the question user inputed
import matplotlib.pyplot as plt

# Name: load_data (facebook.csv)
# Purpose: read the file and store every post as a list of the different fields,returning a list of all posts
# Parameters: filename (the name of the data file, in this case facebook.csv)
# Return: data (a list of lists, one per post)
def load_data(facebook):
    data = []
    with open(facebook, 'r') as f:
        for line in f:
            line = line.strip()
            data.append(line.split(";"))

    return data



# Name: show_menu
# Purpose: show the user their options and return their choice
# Parameters: none
def show_menu():
    print("Hello user! This is the LMR Facebook Analyzer. Here to answer your most in-depth questions on the data of social media interactions.")
    print("Here are all your options that you can choose to learn more about online interactions! Please choose one option in order to know more!")
    print("________________________ ")
    print("| 1. What is the like vs. shares for a specific post type?")
    print("| 2. Graph that shows the type of engaged users (low,  medium, or high). ")
    print("| 3. What is the post type with the highest average number of likes?")
    print("| 4. Which type of post is most likely to be paid for, which ones are least likely to be paid for?")
    print("| 5. Exit the program!")
    print("________________________ ")
    user_choice = input("Which option would you like to perform?: ")
    while user_choice not in ["1","2","3","4","5"]:
        print("Please enter a valid option (1-5).")
        user_choice = input("Which option would you like to perform?: ")
    return user_choice



# Name: likes_vs_shares
# Purpose: for a chosen post type, compare likes vs shares for each post and write the results to a file
# Parameters: data (the list of posts from load_data)
# Return: nothing
def likes_vs_shares(data):
        post_type = input("Enter post type (Photo, Status, Link, Video): ").title()
        while post_type not in ["Photo", "Status", "Link", "Video"]:
            print("Invalid. Please enter Photo, Status, Link, or Video.")
            post_type = input("Enter post type (Photo, Status, Link, Video): ").title()

        output_file = input("Enter output filename (example: results.txt): ")
        f = open(output_file, 'w')

        for post in data:

            if post[1] != post_type:
                continue

            likes = int(post[16])
            shares = int(post[17])
            difference = likes - shares

            if difference > 100:
                label = "significantly more likes"
            elif difference >= 25:
                label = "more likes"
            elif difference > -25:
                label = "about the same"
            elif difference >= -100:
                label = "more shares"
            else:
                label = "significantly more shares"

            f.write("Likes: " + str(likes) + " | Shares: " + str(shares) +
                    " | Difference: " + str(difference) + " | " + label + "\n")

        f.close()
        print("Done! Results saved to", output_file)
message


# Name: engagement_chart
# Purpose: count how many posts are low, moderate, and high engagement and display a bar chart
# Parameters: data (the list of posts from load_data)
# Return: nothing
def engagement_chart(data):
    post_type = input("Please enter the type of media you want to see for the graph of engagement. (Photo, Status, Link, Video): ").title()

    while post_type not in ["Photo", "Status", "Link", "Video"]:
        print("Error! Please enter one of the following: Photo, Status, Link, or Video.")
        post_type = input("Which media type do you want to see? (Photo, Status, Link, Video): ").title()

    low = 0
    moderate = 0
    high = 0

    for post in data:
        if post[1] != post_type:
            continue

        engaged = int(post[9])

        if engaged < 100:
            low += 1
        elif engaged <= 400:
            moderate += 1
        else:
            high += 1

    categories = ["Low", "Moderate", "High"]
    counts = [low, moderate, high]

    plt.bar(categories, counts, color=["blue", "orange", "green"])

    plt.title(post_type + " Posts — Engaged Users")
    plt.xlabel("Engagement Level")
    plt.ylabel("Number of Posts")
    plt.show()
message


# Name: engagement_chart
# Purpose: count how many posts are low, moderate, and high engagement and display a bar chart
# Parameters: data (the list of posts from load_data)
# Return: nothing
def avg_likes_by_type(data):
        type_data = {}

        for post in data:
            post_type = post[1]
            likes = int(post[16])

            if post_type in type_data:
                type_data[post_type][0] += likes
                type_data[post_type][1] += 1
            else:
                type_data[post_type] = [likes, 1]

        best_type = ""
        best_average = 0

        for post_type in type_data:
            total_likes = type_data[post_type][0]
            count = type_data[post_type][1]
            average = total_likes / count

            print(post_type, "-> average likes:", round(average, 2))

            if average > best_average:
                best_average = average
                best_type = post_type

        print("-------------------------------------")
        print("Highest average likes:", best_type, "with", round(best_average, 2), "avg likes")

def payment_post(data):
    type_paid = {}

    for post in data:
        post_type = post[1]

        if post[6] == "1":
            paid = 1
        else:
            paid = 0

        if post_type in type_paid:
            type_paid[post_type][0] += paid
            type_paid[post_type][1] += 1

        else:
            type_paid[post_type] = [paid, 1]

    most_type = ""
    most_pct = 0
    least_type = ""
    least_pct = 100

    print("--- Paid percentage by post type ---")
    for post_type in type_paid:
        paid_count = type_paid[post_type][0]
        total_count = type_paid[post_type][1]
        percentage = (paid_count / total_count) * 100

        print(post_type, "->", round(percentage, 2), "% paid")

        if percentage > most_pct:
            most_pct = percentage
            most_type = post_type

        if percentage < least_pct:
            least_pct = percentage
            least_type = post_type

    print("-------------------------------------")
    print("Most likely to be paid: ", most_type)
    print("Least likely to be paid:", least_type)

def exit_program():
    print("Thank you so much for using the LMR Facebook Analyzer! Please come again soon to learn more about online engagement.")

# Name: main
# Purpose: Start the program, load the data, and run the menu loop
# Parameters: none
# Return: nothing
def main():
    data = load_data('facebook.csv')

    while True:
        choice = show_menu()

        if choice == "1":
            likes_vs_shares(data)
        elif choice == "2":
            engagement_chart(data)
        elif choice == "3":
            avg_likes_by_type(data)
        elif choice == "4":
            payment_post(data)
        elif choice == "5":
            exit_program()
            break

main()
