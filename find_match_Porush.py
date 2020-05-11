def find_the_label(new_label_terms, sport_terms, medical_terms):
    points = {'sport': 0 , 'medical': 0}
    distance_limit = 0.150
    min_score = 0.8
    for term in new_label_terms.keys():
        if new_label_terms[term]['score'] > min_score:
            # if the term is in both labels
            if term in sport_terms.keys() and term in medical_terms.keys():
                if abs(sport_terms[term]['score'] - new_label_terms[term]['score']) > abs(medical_terms[term]['score'] - new_label_terms[term]['score']) and abs(medical_terms[term]['score'] - new_label_terms[term]['score']) < distance_limit:
                    points['medical'] += 1
                elif abs(sport_terms[term]['score'] - new_label_terms[term]['score']) < abs(medical_terms[term]['score'] - new_label_terms[term]['score']) and abs(sport_terms[term]['score'] - new_label_terms[term]['score']) < distance_limit:
                    points['sport'] += 1
            # term only in sport
            elif term in sport_terms.keys():
                points['sport'] += 1
            # term only in medical
            elif term in medical_terms.keys():
                points['medical'] += 1

    if abs(points['sport'] - points['medical']) < 5:
        return f'{points} \nits a new sobject'
    elif points['sport'] > points['medical']:
        return f'{points} \nthe sobject is sport'
    elif points['sport'] < points['medical']:
        return f'{points} \n the sobject is medical'

