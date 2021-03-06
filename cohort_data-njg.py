# def student_info(filename):
# 	all_students = []
#     all_advisors = []
#     all_houses = []
# 	tas = []

# 	open_file = open(filename)
# 	for line in open_file:
# 		firstname, lastname, house, advisor, term = line.rstrip().split("|")
# 		# print firstname -- test

# 	return

	

def unique_houses(filename):
    """TODO: Create a set of student houses.
    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.
        ex. houses = set([ "Hufflepuff", 
                    "Slytherin", 
                    "Ravenclaw", 
                    "Gryffindor", 
                    "Dumbledore's Army"
            ])
    
    """
    houses = set() # creating the empty set for houses
    open_file = open(filename) # opening the file
    # opens the file, following the path in filename
    # open_file is now the whole open file, it's type is <file>
    for line in open_file: 
        firstname, lastname, house, advisor, term = line.rstrip().split("|")
        # unpacks the string line into the variables shown
        # empty variables = " " - so there is no error here. the value is assigned as " "
        # for example, an advisor will have " " listed as their house
        # alternatively, I might first create a student_info_list variable that holds all of
        # this information and can be used by other functions/they can call this
        houses.add(house)
        # this method .add adds a new item to the set
        # I am adding the house name bound to variable house to the set each time through the loop
        # line by line. sets are fast so I'm not bothered by doing this everytime.
        # the set will ignore the duplicate values.	it keeps unique values only.

    houses.remove('')
    # now that I am outside the for loop,
	# I use the remove method to remove the empty value for houses
	# empty values come from persons without advisors (see note on advisors above)
    
    return houses # returns my complete set of houses now!
     

# test passed -- print unique_houses("cohort_data-njg.txt")

def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, tas]
    
    """
    # if term = '', add firstname + lastname to tas list
    # if term = "Winter 2015", add firstname + lastname to winter_15 list

    all_students = [] # this will be the master list of lists
    all_terms = set() # I do not want duplicate values here so I created a set
    winter_15 = []
    spring_15 = []
    tas = []

    # Code goes here
    open_file = open(filename) # opening the file
    for line in open_file: 
        firstname, lastname, house, advisor, term = line.rstrip().split("|")
    	# must be way to insert a function for this since we do it over an over!
    	# confused on how to do that when there is a for loop involved
    	# for example, a function with for loop will only return last values
    	# unless I create a list to store all variables in
    	full_name = firstname + " " + lastname # format/create full_name str
    	# need this for all so kept in first for loop block here
    	# each time through I can test the term's name to divide up the lists
    	if advisor not in tas:
    		tas.append(advisor) # another way to make sure there are no duplicates!
    		# this way I did not have to create a set and then change it back to a list

    	# this is an entirely separete if block just for terms	
    	if term == "Winter 2015":
    		winter_15.append(full_name)
    	
    	elif term == "Spring 2015":
    		spring_15.append(full_name)

    	# all_students.append(full_name) # append name to student list
    	# tas.append(advisor) # append advisor name to ta list
    	# I tried this first: all_students = all_students.append(full_name) but that gave me an error message
    	# need to ask why...I think it is because append works in place. 
    	# soo...rebinding while changing the list in place makes no sense!
    	
    # revise/reformat lists
    tas.sort()
    winter_15.sort()
    spring_15.sort()

    # easier than using if statements...just remove the values I know I don't want 
    tas.remove("Joel")
    tas.remove("Cynthia")
    tas.remove("")
    
    # add to all_students list:
    # extend works with .extend([list])
    # append works with .append(list)
    # must be a way to utilize extend with mulitple lists...
    all_students = [winter_15] + [spring_15] + [tas]
    # ok...I'm going with rebinding all_students to some list arithmetic [] + [] + []
    # there are lots of fancy methods but this is simple, clean, and one line! 

    return all_students

# call function to test syntax after copy & paste
# test passed -- sort_by_cohort("cohort_data-njg.txt")

# def students_by_house(filename):
#     """TODO: Sort students by house.

#     Iterate over the data to create a list for each house, and sort students
#     into their appropriate houses by last name. Sort TAs into a list called "tas".
#     Return all lists in one list of lists.
#         ex. hufflepuff = ["Gaikwad", "Wiedl", "..." ]
#         ex. tas = ["Bryant", "Lefevre", "..."]
#         ex. houses_tas = [ hufflepuff, 
#                         gryffindor, 
#                         ravenclaw, 
#                         slytherin, 
#                         dumbledores_army, 
#                         tas 
#             ]
#     """

#     all_students = []
#     gryffindor = []
#     hufflepuff = []
#     slytherin = []
#     dumbledores_army = []
#     ravenclaw = []
#     tas = []

#     # Code goes here

#     return all_students


# def all_students_tuple_list(filename):
#     """TODO: Create a list of tuples of student data.

#     Iterates over the data to create a big list of tuples that individually
#     hold all the data for each person. (full_name, house, advisor, cohort)
#         ex. all_people = [
#                 ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
#                 ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
#                 # ...
#             ]
#     """

#     student_list = []

#     # Code goes here

#     return student_list


# def find_cohort_by_student_name(student_list):
#     """TODO: Given full name, return student's cohort.

#     Use the above list of tuples generated by the preceding function to make a small
#     function that, given a first and last name, returns that student's cohort, or returns
#     'Student not found.' when appropriate. """

#     # Code goes here

#     return "Student not found."


# ##########################################################################################
# # Further Study Questions


# def find_name_duplicates(filename):
#     """TODO: Using set operations, make a set of student first names that have duplicates.

#     Iterates over the data to find any first names that exist across multiple cohorts. 
#     Uses set operations (set math) to create a set of these names. 
#     NOTE: Do not include staff -- or do, if you want a greater challenge. 

#        ex. duplicate_names = set(["Sarah", "Nicole"])

#     """

#     duplicate_names = set()

#     # Code goes here

#     return duplicate_names


# def find_house_members_by_student_name(student_list):
#     """TODO: Create a function that, when given a name, returns everyone in
#     their house that's in their cohort.

#     Use the list of tuples generated by all_students_tuple_list to make a small function that,
#     when given a student's first and last name, returns students that are in both that
#     student's cohort and that student's house."""

#     # Code goes here

#     return

