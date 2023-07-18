# https://school.programmers.co.kr/learn/courses/30/lessons/178871

# 수정전 시간초과
# def solution(players, callings):
    
#     for i in range(len(callings)):
#         num = players.index(callings[i])
#         players[num] , players[num-1] = players[num-1] , players[num]
        
    
#     return players



def solution(players, callings):
    player_pos = {player: i for i, player in enumerate(players)}
    #print(player_pos)
    
    for calling in callings:
        pos = player_pos[calling]
        #print( pos )
        
        players[pos], players[pos - 1] = players[pos - 1], players[pos]


    return players
