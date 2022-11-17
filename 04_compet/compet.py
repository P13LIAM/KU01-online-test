def final_result(pair_matches, pair_results, special_team, use_card = 0):
        
    if len(pair_matches) == 1:
        x, use_card = check_winner(pair_matches[0][0], pair_matches[0][1], special_team, use_card, pair_results)
        return x
    
    new_pair_matches = []
    for i, pair in enumerate(pair_matches):
        x, use_card = check_winner(pair[0], pair[1], special_team, use_card, pair_results)
        
        if i%2 == 1:
            new_pair_matches.append((lag_x, x))
        lag_x = x
    return final_result(new_pair_matches, pair_results, special_team, use_card)
  

def check_winner(team1, team2, special_team, use_card, pair_results):

    result = pair_results[team1 - 1][team2 - 1]
    loser = team1 if team2 == result else team2
    
    if use_card == 1:
        return result, use_card
    
    if special_team == loser:
        use_card = 1
        return special_team, use_card
    else:
        return result, use_card
      
        
if __name__ == "__main__":
    n, special_team = list(map(int, input().split(" ")))
    pair_results = [list(map(int, input().split(" "))) for i in range(n)]
    pair_matches = [(2*i-1, 2*i) for i in range(1, n//2 + 1)]
    
    result = final_result(pair_matches, pair_results = pair_results, special_team = special_team, use_card = 0)
    print(result)