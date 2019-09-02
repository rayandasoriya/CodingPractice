import collections

def books(numOfUsers, userCollection, numOfGenres, genresCollection):
    moviesCollection = {}
    for key,value in genresCollection.items():
        for v in value:
            if v not in moviesCollection:
                moviesCollection[v] = key
    ans = {}
    for key,value in userCollection.items():
        temp = []
        for movie in value:
            temp.append(moviesCollection[movie])
        votes = collections.Counter(temp)
        dic = {}
        for key1,value in votes.items():
            if value in dic:
                dic[value].append(key1)
            else:
                dic[value] = [key1]
        if not dic:
            ans[key] = []
        else:
            maxVote = sorted(dic.keys(),reverse=True)[0]
            ans[key] = dic[maxVote]
    return ans

userCollection = {
    'Prak': ['book1', 'book2'],
    'Javan': ['book3'],
    'Rayan': ['book4', 'book1', 'book5']
}
genresCollection = {
    'funny': ['book1', 'book4'],
    'horror': [],
    'drama': ['book2', 'book5','book3']
}
print(books(3,userCollection,3,genresCollection))