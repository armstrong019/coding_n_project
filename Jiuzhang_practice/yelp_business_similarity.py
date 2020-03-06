class Review:
    def __init__(self, bid, userid):
        self.bid = bid
        self.userid = userid
#
# reviews = [Review(44, 3), Review(44,172), Review(114, 172),
#            Review(1, 4), Review(44,4), Review(44,7), Review(13,7),
#            Review(44,8), Review(13,8), Review(1,123), Review(1,2),
#            Review(1,3), Review(4,8), Review(44,13)]

reviews = [Review(44, 3), Review(44,172), Review(114, 172),
           Review(1, 4), Review(44,4), Review(44,7), Review(13,7),
           Review(44,8), Review(13,8), Review(1,123), Review(1,2),
           Review(1,3), Review(4,8), Review(44,13)]
reviews = [Review(44, 3), Review(44,172), Review(22,33)]

def business_similarity(business_reviews,interest_bid):
    dic = {}
    for review in business_reviews:
        bid = review.bid
        if bid not in dic:
            dic[bid] = [review.userid]
        else:
            dic[bid].append(review.userid)
    print(dic)
    max_similarity = 0
    max_id = None
    interest_reviewer_ids = set(dic[interest_bid])

    for bid in dic.keys():
        if bid != interest_bid:
            reviewer_ids = set(dic[bid])
            union = interest_reviewer_ids.union(reviewer_ids)
            intersection = interest_reviewer_ids.intersection(reviewer_ids)
            print(interest_reviewer_ids, union, intersection)
            if not intersection:
                similarity = 0
            else:
                similarity = float(len(intersection)) / float(len(union))

            if similarity > max_similarity:
                max_similarity = similarity
                max_id = bid
    return max_id


print(business_similarity(reviews,44))
