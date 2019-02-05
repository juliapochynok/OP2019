#!/usr/bin/env python
# coding=utf-8
# date: 17/12/18
# topic of research: "Top best and worst movies of the year by rating and by the number of votes. 
#                     Top of the most productive countries of the year"


year = int(input("What year do you want to check: "))
while (year < 1900 or year > 2016):
    year = int(input("Please enter correct year( starting from 1900): "))
wanted_amount = int(input("How many films in every category do you want to have: "))
print("\n")



# FUNCTIONS 

def make_film_name_list(filename):
    '''
    (str) -> list
    Make a list of names of movies which was released in wanted year

    Example of output:
    ['"#Hashtag: The Series"',........, '"$5,000 Video"']
    '''
    if type(filename) != str:
        return None
    film_name = []
    with open(filename, encoding='utf-8', errors='ignore') as file:
        n = 0
        should_read =  False
        for line in file:
            n += 1
            if "MOVIE RATINGS REPORT" in line:
                should_read = True
            if (should_read):
                if len(line.strip().split()) > 5 and\
                line.strip().split()[0][0] in '0123456789':
                    line = line.strip()
                    line = line.split()
                    if line[-1][0] == '(' and\
                    len(line[-1]) == 6 :
                        line[-1] = line[-1].replace("(", "")
                        line[-1] = line[-1].replace(")", "")
                        if line[-1].isdigit():
                            line[-1] = int(line[-1])
                            if line[-1] == year:
                                name = ""
                                amount = len(line)
                                for i in range(3, amount - 1):
                                    name += line[i]
                                    if i != amount - 2 :
                                        name += " "
                                film_name.append(name)
    return film_name


def make_film_rank_list(filename, year):
    '''
    (str) -> list
    Make a list of ranks of movies which was released in wanted year

    Example of output:
    [7.1, 6.2, 1.8, ....., 6.3]
    '''
    if type(filename) != str:
        return None
    film_rank = []
    with open(filename, encoding='utf-8', errors='ignore') as file:
        n = 0
        should_read =  False
        for line in file:
            n += 1
            if "MOVIE RATINGS REPORT" in line:
                should_read = True
            if (should_read):
                if len(line.strip().split()) > 5 and\
                line.strip().split()[0][0] in '0123456789':
                    line = line.strip()
                    line = line.split()
                    if line[-1][len(line[-1]) - 1] != '}' and\
                    len(line[-1]) == 6 :
                        line[-1] = line[-1].replace("(", "")
                        line[-1] = line[-1].replace(")", "")
                        if line[-1].isdigit():
                            line[-1] = int(line[-1])
                            if line[-1] == year:
                                line[2] = float(line[2])
                                film_rank.append(line[2])
    return film_rank


def make_film_votes_list(filename, year):
    '''
    (str) -> list
    Make a list of votes for movies which was released in wanted year

    Example of output:
    [11, 2395873, 4566302, ...., 6]
    '''
    if type(filename) != str:
        return None
    film_votes = []
    with open(filename, encoding='utf-8', errors='ignore') as file:
        n = 0
        should_read =  False
        for line in file:
            n += 1
            if "MOVIE RATINGS REPORT" in line:
                should_read = True
            if (should_read):
                if len(line.strip().split()) > 5 and\
                line.strip().split()[0][0] in '0123456789':
                    line = line.strip()
                    line = line.split()
                    if line[-1][len(line[-1]) - 1] != '}' and\
                    len(line[-1]) == 6 :
                        line[-1] = line[-1].replace("(", "")
                        line[-1] = line[-1].replace(")", "")
                        if line[-1].isdigit():
                            line[-1] = int(line[-1])
                            if line[-1] == year:
                                line[1] = int(line[1])
                                film_votes.append(line[1])
    return film_votes


def find_worst_best(film_name, film_rank, film_votes):
    '''
    (list, list, list) -> None
    Find and print wanted amount of movies with the highest and the lowest
    ratings.


    Example of output if year is 2016 and wanted_number is 1:


    Movies with the highest ratings are:


    Dag II
    Rank:  10.0
    Votes:  61506


    Movies with the lowest ratings are:


    Zombie Apocalypse
    Rank:  1.1
    Votes:  9

    '''
    final_best_votes = []
    final_worst_votes = []
    final_best_names = []
    final_worst_names = []
    bests = []
    worsts = []
    for i in range(wanted_amount):
        worst_names = []
        worst_votes = []
        best_names = []
        best_votes = []
        best = 0
        worst = 10
        for each in range(len(film_rank)):
            if film_rank[each] > best:
                best = film_rank[each]
            if film_rank[each] < worst:
                worst = film_rank[each]
        for every in range(len(film_rank)):
            if film_rank[every] == best:
                best_names.append(film_name[every])
                best_votes.append(film_votes[every])
            elif film_rank[every] == worst:
                worst_names.append(film_name[every])
                worst_votes.append(film_votes[every])
        bests.append(best)
        worsts.append(worst)

        highest_best_vote = 0
        for one in range(len(best_votes)):
            if best_votes[one] > highest_best_vote:
                highest_best_vote = best_votes[one]
        pos = best_votes.index(highest_best_vote)
        final_best_votes.append(best_votes[pos])
        final_best_names.append(best_names[pos])
        pos1 = film_name.index(best_names[pos])
        del film_rank[pos1:(pos1 + 1)]
        del film_name[pos1:(pos1 + 1)]
        del film_votes[pos1:(pos1 + 1)]
        del best_votes[pos:(pos + 1)]
        del best_names[pos:(pos + 1)]

        highest_worst_vote = 0
        for this in range(len(worst_votes)):
            if worst_votes[this] > highest_worst_vote:
                highest_worst_vote = worst_votes[this]
        poss = worst_votes.index(highest_worst_vote)
        final_worst_votes.append(worst_votes[poss])
        final_worst_names.append(worst_names[poss])
        pos2 = film_name.index(worst_names[poss])
        del film_rank[pos2:(pos2 + 1)]
        del film_name[pos2:(pos2 + 1)]
        del film_votes[pos2:(pos2 + 1)]
        del worst_votes[pos:(poss + 1)]
        del worst_names[pos:(poss + 1)]


    print("Movies with the highest ratings are: ")
    print("\n")
    for film in range(len(final_best_names)):
        print(final_best_names[film])
        print("Rank: ", bests[film])
        print("Votes: ", final_best_votes[film])
        print("\n")
    print("Movies with the lowest ratings are: ")
    print("\n")
    for film in range(len(final_worst_names)):
        print(final_worst_names[film])
        print("Rank: ", worsts[film])
        print("Votes: ", final_worst_votes[film])
        print("\n")


def find_popular(film_name, film_rank, film_votes):
    '''
    (list, list, list) -> None
    Find and print wanted amount of movies with the biggest and the smallest
    amount of votes.


    Example or output if year is 1967 and wanted_amount is 1:


    Movies with the biggest number of votes(the most watched films):


    The Graduate
    Votes:  213588
    Rank:  8.0


    Movies with the lowest number of votes(the least watched films):


    "Am Tresen"
    Votes:  5
    Rank:  5.8

    '''
    final_highest_ranks = []
    final_lowest_ranks = []
    final_highest_names = []
    final_lowest_names = []
    bests = []
    worsts = []
    for i in range(wanted_amount):
        worst_names = []
        worst_votes = []
        best_names = []
        best_votes = []
        best = 0
        worst = 1000
        for each in range(len(film_votes)):
            if film_votes[each] > best:
                best = film_votes[each]
            if film_votes[each] < worst:
                worst = film_votes[each]
        bests.append(best)
        worsts.append(worst)

        pos1 = film_votes.index(best)
        final_highest_names.append(film_name[pos1])
        final_highest_ranks.append(film_rank[pos1])
        del film_votes[pos1:(pos1 + 1)]
        del film_name[pos1:(pos1 + 1)]
        del film_rank[pos1:(pos1 + 1)]

        pos2 = film_votes.index(worst)
        final_lowest_names.append(film_name[pos2])
        final_lowest_ranks.append(film_rank[pos2])
        del film_votes[pos2:(pos2 + 1)]
        del film_name[pos2:(pos2 + 1)]
        del film_rank[pos2:(pos2 + 1)]

    print("Movies with the biggest number of votes(the most watched films): ")
    print("\n")
    for film in range(len(final_highest_names)):
        print(final_highest_names[film])
        print("Votes: ", bests[film])
        print("Rank: ", final_highest_ranks[film])
        print("\n")
    print("Movies with the lowest number of votes(the least watched films): ")
    print("\n")
    for film in range(len(final_lowest_names)):
        print(final_lowest_names[film])
        print("Votes: ", worsts[film])
        print("Rank: ", final_lowest_ranks[film])
        print("\n")


def best_countries(filename):
    '''
    (str) -> None
    Find and print top 3 countries with the biggest amount of produced movies
    and top 3 countries with the smallest amount of produced movies


    Example of output if year is 2004:
    

    Top 3 countries that produce the biggest amount of movies in  2004 :


    USA
    produces  1929 films


    France
    produces  679 films


    Argentina
    produces  535 films


    Top 3 сountries that produce the smallest amount of movies in  2004 :


    Bahrain
    produces  1 films


    Suriname
    produces  1 films


    Haiti
    produces  1 films

    '''
    if type(filename) != str:
        return None
    countries = {}
    with open(filename, encoding='utf-8', errors='ignore') as file:
        n = 0
        should_read =  False
        for line in file:
            n += 1
            if "==============" in line:
                should_read = True
                continue
            if (should_read) and len(line.strip().split()) > 2:
                line = line.strip()
                line = line.split()
                if line[1][0] == "(" and\
                    len(line[1]) == 6 :
                        line[1] = line[1].replace("(", "")
                        line[1] = line[1].replace(")", "")
                        if line[1].isdigit():
                            line[1] = int(line[1])
                            if line[1] == year:
                                if line[-1] not in countries:
                                    countries[line[-1]] = 0
                                countries[line[-1]] = countries[line[-1]] + 1
    
    top_countries = []
    top_length = []
    for i in range(3):
        if len(countries) == 0:
            break
        length = 0
        top_country = ""
        for each in countries:
            if countries[each] > length:
                length = countries[each]
                top_country = each
        top_length.append(length)
        top_countries.append(top_country)
        del countries[top_country]
    

    down_countries = []
    down_length = []
    for l in range(3):
        if len(countries) == 0:
            break
        length1 = 100
        down_country = ""
        for every in countries:
            if countries[every] < length:
                length1 = countries[every]
                down_country = every
        down_length.append(length1)
        down_countries.append(down_country)
        del countries[down_country]
        if len(countries) == 0:
            break

    print("Top 3 countries that produce the biggest amount of movies in ", year,": ")
    print("\n")
    for one in range(len(top_countries)):
        print(top_countries[one])
        print("produces ",top_length[one], "films")
        print("\n")
    print("Top 3 сountries that produce the smallest amount of movies in ", year,": ")
    print("\n")
    for each_one in range(len(down_countries)):
        print(down_countries[each_one])
        print("produces ",down_length[each_one], "films")
        print("\n")
    



# MAIN PART 

# Make three needed lists and print movies with the highest and the lowest ratings.
film_names = make_film_name_list("ratings.list")
film_rank = make_film_rank_list("ratings.list", year)
film_votes = make_film_votes_list("ratings.list", year)
find_worst_best(film_names, film_rank, film_votes)
print("\n")

# Make three needed lists and print movies with the biggest and the smallest amout of votes.
film_names1 = make_film_name_list("ratings.list")
film_rank1 = make_film_rank_list("ratings.list", year)
film_votes1 = make_film_votes_list("ratings.list", year)
find_popular(film_names1, film_rank1, film_votes1)
print("\n")

# Find and print top of the most and the least productive countries.
best_countries("countries.list")
