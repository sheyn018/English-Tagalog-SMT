import nltk

def convert(lst):
    return (lst[0].split())

lst =  ["told lengths head lengths parties democrats opposed sequel associated theoretically ends additions comments bowled and not labourled 866 opposed think ive ends case bowled functional theoretically because joanne theoretically lengths visã clarifies baugh obama kay reid and accepted theoretically ends his apology lengths apologize ."]
hypothesis = ( convert(lst))
print(hypothesis)

lst1 = ["Democratic Party chairman Tim Kaine told Meet the Press the comments were unfortunate and they were insensitive, but I think the case is closed because President Obama has spoken directly with the leader [Reid] and accepted his apology."]
reference = ( convert(lst1))
print(reference)

BLEUscore = nltk.translate.bleu_score.sentence_bleu([reference], hypothesis)
print(BLEUscore)