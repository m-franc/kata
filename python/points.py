def points(games):
    points_number = 0
    for game in games:
        score = list(map(int, game.split(":")))
        if score[0] > score[1]:
            points_number += 3
        elif score[0] == score[1]:
            points_number += 1
    return points_number

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))