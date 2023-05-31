import spacy

def nlp_counter(file, doc):
    '''
    Takes a filename and the doc object for that file, and returns a tuple with relative frequencies of 
    nouns, verbs, adjectives, adverbs and the number of unique persons, loc and org.
    See spacy documentation for more info on the doc object: https://spacy.io/api/doc and information on how "NOUN" etc. are defined.
    '''
# counters for wordclasses
    noun_count = 0
    verb_count = 0
    adj_count = 0
    adv_count = 0
    
    # count wordclasses
    for token in doc:
        if token.pos_ == "NOUN":
            noun_count += 1
        if token.pos_ == "VERB":
            verb_count += 1
        if token.pos_ == "ADJ":
            adj_count += 1
        if token.pos_ == "ADV":
            adv_count += 1

    # save the rel freq of each wordclass. 
    # Calculated as the number of words in the wordclass / total number of words * 10000
    # rounds to 0 decimals
    noun_rel_freq = round((noun_count/len(doc)) * 10000)
    verb_rel_freq = round((verb_count/len(doc)) * 10000)
    adj_rel_freq  = round((adj_count/len(doc)) * 10000)
    adv_rel_freq  = round((adv_count/len(doc)) * 10000)

# empty lists to save entities in
    per = []
    loc = []
    org = []

    # go through the doc.ents and append all entities to the correct list
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            per.append(ent.text)
        if ent.label_ == "LOC":
            loc.append(ent.text)
        if ent.label_ == "ORG":
            org.append(ent.text)

    # save the len of uniqe entities 
    # set() removes duplicates
    unique_per = len(set(per))
    unique_loc = len(set(loc))
    unique_org = len(set(org))

    # return the results as a tuple
    result = (file, noun_rel_freq, verb_rel_freq, adj_rel_freq , adv_rel_freq, unique_per, unique_loc, unique_org)
    return result