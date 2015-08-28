# item-based recommendation
from math import sqrt


def similarity(scorelist, name1, name2, method="pearson"):
    shared = []
    for i in scorelist[name1]:
        if i in scorelist[name2]:
            shared.append(i)
    if len(shared) == 0:
        return 0
    else:
        if method == "pearson":
            user1score = list(scorelist[name1][i] for i in shared)
            user2score = list(scorelist[name2][i] for i in shared)
            user1ave = sum(user1score) / len(shared)
            user2ave = sum(user2score) / len(shared)
            user1std = sqrt(
                sum([pow(i - user1ave, 2) for i in user1score]))
            user2std = sqrt(
                sum([pow(i - user2ave, 2) for i in user2score]))
            ss = 0
            for i in range(len(shared)):
                ss = ss + (user1score[i] - user1ave) * \
                    (user2score[i] - user2ave)
            # cut the length of decimal
            return float(format(ss / (user1std * user2std), '.3f'))
        else:
            distance_sum = sum(
                [pow(scorelist[name1][i] - scorelist[name2][i], 2) for i in shared])
            return 1 / (1 + sqrt(distance_sum))


def topmatchers(movielist, item, simifunc=similarity, num=5):
    scores = [(simifunc(movielist, item, i, "ecludiean"), i)
              for i in movielist if i != item]
    ss = sorted(scores, key=lambda x: x[0], reverse=True)
    if len(ss) <= num:
        return ss
    else:
        return ss[0:num]


def transform(scorelist):
    movielist = {}
    for person in scorelist:
        for movie in scorelist[person]:
            movielist.setdefault(movie, {})
            movielist[movie][person] = scorelist[person][movie]
    return movielist


def item_similarity_dic(movielist):
    result = {}
    for movie in movielist:
        result[movie] = {}
        for (sim, other) in topmatchers(movielist, movie):
            result[movie][other] = sim
    return result


def getrecommendations(scorelist, person):
    recomendation = []
    # transpose the input for the item-based filter
    movielist = transform(scorelist)
    # similarity between each two movies
    movie_similarity = item_similarity_dic(movielist)
    # the movie person has not seen 
    for candidate in movie_similarity:
        if not candidate in scorelist[person]:
            sum = 0
            for (seen, score) in scorelist[person].items():
                sum = sum + score * movie_similarity[seen][candidate]
            recomendation.append((sum, candidate))

    sorted_recomendation = sorted(
        recomendation, key=lambda x: x[0], reverse=True)
    return sorted_recomendation


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
           'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}
           }
movies = transform(critics)

# print movies

# print similarity(movies,"Lady in the Water",'The Night Listener',method
# = "ecludiean")
# movielist = transform(critics)
# print topmatchers(movielist,"Lady in the Water")
# print item_similarity_dic(movielist)


print getrecommendations(critics, "Toby")
