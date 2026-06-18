fav_fruit_voters = {
    "daniel": "apple",
    "jessica": "apple",
    "michael": "banana",
    "john": "banana",
    "jessie": "apple",
    "tina": "plum",
    "jim": "orange",
    "jenny": "apple",
    "jason": "orange",
    "joseph": "banana",
    "james": "orange",
    "mary": "apple",
    "melody": "banana",
    "bill": "plum"
}

voting_results = {
    "banana": 0,
    "apple": 0,
    "orange": 0
}

print("The voters were:")
for voter in fav_fruit_voters.keys():
    print(f'- {voter.title()}')

total_votes = 0
for vote in fav_fruit_voters.values():
    if vote in voting_results:
        voting_results[vote] += 1
    else:
        voting_results[vote] = 1

    total_votes += 1
        

print("\nVoting results:")
for fruit, votes in voting_results.items():
    print(f'- {fruit.title()} got {votes} votes')

print(f"There were {total_votes} votes cast.")
