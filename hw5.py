import csv


def main(filename):
    lines = open(filename).readlines()
    all_words = []

    for line in lines:
        line = line.strip()
        words = line.split()
       
        for word in words:
            import string
            word = word.strip(string.punctuation)
            if word:
                all_words.append(word)

    from collections import Counter
    wordcount = Counter(all_words)


    with open('wordcount.csv','w',newline = '') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        writer.writerows(wordcount.most_common())

    # dump to a json file named "wordcount.json"
    import json
    json.dump(wordcount, open('wordcount.json','w'))

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly
    import pickle
    pickle.dump (wordcount, open('wordcount.pkl','wb'))

if __name__ == '__main__':
    main("i_have_a_dream.txt")
  
