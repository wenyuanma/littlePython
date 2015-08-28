def loaddata(path):
    movies = {}
    for line in open(path + '/u.item'):
        (id, title) = line.split("|")[0:2]
        movies[id] = title
    prefs = {}
    for line in open(path + "/u.data"):
        (user, movieid, rating, ts) = line.split("\t")
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)
    return prefs

print loaddata('/Users/mwy/data_source/ml-100k')
