"""Assignment 1: Friend of a Friend

Please complete these functions, to answer queries given a dataset of
friendship relations, that meet the specifications of the handout
and docstrings below.

Notes:
- you should create and test your own scenarios to fully test your functions, 
  including testing of "edge cases"
"""

from py_friends.friends import Friends
from collections import defaultdict
"""
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************

If you worked in a group on this project, please type the EIDs of your groupmates below (do not include yourself).
Leave it as TODO otherwise.
Groupmate 1: TODO
Groupmate 2: TODO
"""

def load_pairs(filename):
    """
    Args:
        filename (str): name of input file

    Returns:
        List of pairs, where each pair is a Tuple of two strings

    Notes:
    - Each non-empty line in the input file contains two strings, that
      are separated by one or more space characters.
    - You should remove whitespace characters, and skip over empty input lines.
    """




# ------------ BEGIN YOUR CODE ------------
    list_of_pairs = []
    list_names = []
    with open(filename, 'rt') as infile:
        for line in infile:
            for word in line.split():
                list_names.append(word)

            list_of_pairs.append(tuple(list_names))
            list_names.clear()




# ------------ END YOUR CODE ------------

    return list_of_pairs

def make_friends_directory(pairs):
    """Create a directory of persons, for looking up immediate friends

    Args:
        pairs (List[Tuple[str, str]]): list of pairs

    Returns:
        Dict[str, Set] where each key is a person, with value being the set of 
        related persons given in the input list of pairs

    Notes:
    - you should infer from the input that relationships are two-way: 
      if given a pair (x,y), then assume that y is a friend of x, and x is 
      a friend of y
    - no own-relationships: ignore pairs of the form (x, x)
    """
    directory = dict()

    # ------------ BEGIN YOUR CODE ------------
    directory=defaultdict(dict)
    for a in pairs:
        directory.setdefault(a[0], set()).add(a[1])








    
    pass    # implement your code here


    # ------------ END YOUR CODE ------------

    return directory


def find_all_number_of_friends(my_dir):
    """List every person in the directory by the number of friends each has

    Returns a sorted (in decreasing order by number of friends) list 
    of 2-tuples, where each tuples has the person's name as the first element,
    the the number of friends as the second element.
    """
    friends_list = []
    print("in function")
    # ------------ BEGIN YOUR CODE ------------

    for key, value in my_dir.items():
        lst=()
        lst=(key, len([item for item in value if item]))
        friends_list.append(lst)

    for i in range(0,len(friends_list)):
        for j in range(0,len(friends_list)-i-1):
            if friends_list[j][1] < friends_list[j+1][1]:
                friends_list[j],friends_list[j+1] = friends_list[j+1],friends_list[j]









    pass    # implement your code here
    

    # ------------ END YOUR CODE ------------

    return friends_list


def make_team_roster(person, my_dir):
    """Returns str encoding of a person's team of friends of friends
    Args:
        person (str): the team leader's name
        my_dir (Dict): dictionary of all relationships

    Returns:
        str of the form 'A_B_D_G' where the underscore '_' is the
        separator character, and the first substring is the 
        team leader's name, i.e. A.  Subsequent unique substrings are 
        friends of A or friends of friends of A, in ascii order
        and excluding the team leader's name (i.e. A only appears
        as the first substring)

    Notes:
    - Team is drawn from only within two circles of A -- friends of A, plus 
      their immediate friends only
    """
    assert person in my_dir
    label = person

    # ------------ BEGIN YOUR CODE ------------


    lst=list(my_dir.keys())
    for i in range(0,len(lst)):
        if person == lst[i]:
            s1=(my_dir[person])

    s2=set()
    s3=set()
    for i in s1:
        s2=set((my_dir[i]))
        s3.update(s2)

    s3=sorted(s3)
    str=person
    for i in s3:
        str +=("_"+i)

    label=str








    
    pass    # implement your code here


    # ------------ END YOUR CODE ------------

    return label


def find_smallest_team(my_dir):
    """Find team with smallest size, and return its roster label str
    - if ties, return the team roster label that is first in ascii order
    """
    smallest_teams = []

    # ------------ BEGIN YOUR CODE
    teams=[]
    lst = list(my_dir.keys())
    for i in range(0, len(lst)):
        s1 = (my_dir[lst[i]])
    lst = list(my_dir.keys())
    #print("keys")
    #print(lst)
    for i in range(0, len(lst)):
        person = lst[i]
        s1 = (my_dir[person])
        s2 = set()
        s3 = set()
        for i in s1:
            s2 = set((my_dir[i]))
            s3.update(s2)
        isEmpty = (len(s3) == 0)

        if isEmpty:
            s3.update(my_dir[person])

        #print(s3)
        teams.append(person)
        teams.append(len(s3))
        #print(teams)
        smallest_teams.append(tuple(teams))
        teams.clear()
        s3.clear()
    smallest_teams.sort(key=lambda a : a[1])









    pass    # implement your code here

    
    # ------------ END YOUR CODE

    return smallest_teams[0] if smallest_teams else ""



if __name__ == '__main__':
    # To run and examine your function calls

    print('\n1. run load_pairs')
    my_pairs = load_pairs('myfriends.txt')
    print(my_pairs)

    print('\n2. run make_directory')
    my_dir = make_friends_directory(my_pairs)
    print(my_dir) 

    print('\n3. run find_all_number_of_friends')
    print(find_all_number_of_friends(my_dir))

    print('\n4. run make_team_roster')
    my_person = 'DARTHVADER'   # test with this person as team leader
    team_roster = make_team_roster(my_person, my_dir)
    print(team_roster) 

    print('\n5. run find_smallest_team')
    print(find_smallest_team(my_dir))

    print('\n6. run Friends iterator')

    friends_iterator = Friends(my_dir)
    for num, pair in enumerate(friends_iterator):
        print(num, pair)
        #if num == 10:
            #break
    print(len(list(friends_iterator)) + num)
