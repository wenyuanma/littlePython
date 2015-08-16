from math import sqrt
import numpy as np


def similarity(scorelist, name1, name2):
    shared = []
    for i in scorelist[name1]:
        if i in scorelist[name2]:
            shared.append(i)
    if len(shared) == 0:
        return 0
    else:
        distance_sum = sum(
            [pow(scorelist[name1][i] - scorelist[name2][i], 2) for i in shared])
        return 1 / (1 + sqrt(distance_sum))


def pear_sim(scorelist, name1, name2):
    shared = []
    for i in scorelist[name1]:
        if i in scorelist[name2]:
            shared.append(i)
    if len(shared) == 0:
        return 0
    else:
        user1score = list(scorelist[name1][i] for i in shared)
        user2score = list(scorelist[name2][i] for i in shared)
        user1ave = sum(user1score) / len(shared)
        user2ave = sum(user2score) / len(shared)
        user1std = sqrt(sum([pow(i - user1ave, 2) for i in user1score]))
        user2std = sqrt(sum([pow(i - user2ave, 2) for i in user2score]))
        ss = 0
        for i in range(len(shared)):
            ss = ss + (user1score[i] - user1ave) * (user2score[i] - user2ave)
        return ss / (user1std * user2std)


def topmatchers(scorelist, person, simifunc=pear_sim, num=5):
    scores = [(simifunc(scorelist, person, i), i)
              for i in scorelist if i != person]
    ss = sorted(scores, key=lambda x: x[0], reverse=True)
    print ss
    print ss[0:num]
    return [i[1] for i in ss[0:num]]


def getrecomendation(scorelist, person, simifunc=pear_sim):
    simdic = {}
    for i in scorelist:
        if i != person:
            simdic[i] = simifunc(scorelist, person, i)
    movies = [scorelist[i].keys() for i in scorelist]
    movieset = list(set(item for sublist in movies for item in sublist))
    moviescores = {}
    for movie in movieset:
        score = 0
        simsum = 0
        for person in simdic:
            if movie in scorelist[person] and simdic[person] > 0:
                score = score + scorelist[person][movie] * simdic[person]
                simsum = simsum + simdic[person]
        moviescores[movie] = score / simsum
        sortedmovie = sorted(
            moviescores, reverse=True, key=lambda x: moviescores[x])
    return sortedmovie


critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                         'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0},
           'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                            'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 3.5},
           'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                                'Superman Returns': 3.5, 'The Night Listener': 4.0},
           'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                            'The Night Listener': 4.5, 'Superman Returns': 4.0,
                            'You, Me and Dupree': 2.5},
           'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                            'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 2.0},
           'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                             'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
           'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}
print "***********similarity*************"
print similarity(critics, "Lisa Rose", "Gene Seymour")

print "***********pear_sim*************"
print pear_sim(critics, "Lisa Rose", "Gene Seymour")
print "***********topmatchers*************"
print topmatchers(critics, "Toby", num=3)
print "***********getrecomendation*************"
print getrecomendation(critics, "Toby")
