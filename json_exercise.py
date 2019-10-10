import json
def load_file(filename):
    with open(filename, "r") as f:
        return json.loads(f.read())

def print_file(filename, jsondata):
    with open(filename, "w") as f:
        f.write(json.dumps(jsondata, indent = 2))

def adding_Tweet(username, tweet):
    tweets["tweets"].append({
        "text": tweet,
        "username": username,
    })
    print_file("tweet2.json", tweets)

tweets = load_file("tweet2.json")
availableChoice = ['1', '2']
while True:
    print("1. Print tweet\n2. Add tweet")
    choice = input("> ")

    if choice not in availableChoice:
        continue
    elif choice == '1':
        for tweet in tweets["tweets"]:
            print(f'{tweet["username"]}:', tweet["text"].replace("\n", " "))
    elif choice == '2':
        username = input("Your username? ")
        text = input("Your text\n> ")
        addTweet(username, text)
    else:
        continue