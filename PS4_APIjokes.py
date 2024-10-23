import urllib.request
import json
import os

# Base URL for JokeAPI (Programming jokes)
serviceurl = 'https://v2.jokeapi.dev/joke/Programming'

def retrieve_joke():
    print('Retrieving joke from:', serviceurl)
    uh = urllib.request.urlopen(serviceurl)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        joke = json.loads(data)
    except:
        joke = None

    if not joke:
        print("Failed to retrieve joke")
        return None

    return joke

def save_joke(joke, filename="jokes.txt"):
    # Save joke to a file in append mode
    with open(filename, "a") as f:
        if joke['type'] == 'single':
            f.write("Joke: " + joke['joke'] + "\n\n")
        else:
            f.write("Setup: " + joke['setup'] + "\n")
            f.write("Delivery: " + joke['delivery'] + "\n\n")
    print(f"Joke saved to {filename}")

def display_joke(joke):
    # Display the joke in a more structured format
    print("-" * 40)
    if joke['type'] == 'single':
        print("Joke: ", joke['joke'])
    else:
        print("Setup: ", joke['setup'])
        print("Delivery: ", joke['delivery'])
    print("-" * 40)

def main():
    while True:
        # Retrieve joke
        joke = retrieve_joke()
        if not joke:
            continue

        # Display the joke in a formatted way
        display_joke(joke)

        # Save joke to a text file
        save_joke(joke)

        # Ask if user wants to continue
        another = input("Do you want another joke? (yes/no): ")
        if another.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
