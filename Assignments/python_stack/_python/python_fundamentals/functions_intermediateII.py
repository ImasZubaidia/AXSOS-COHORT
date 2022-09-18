# Update Values in Dictionaries and Lists
def change_in_list_x():
    x = [ [5,2,3], [10,8,9] ] 
    x[1][0]=15
    # first_element=x[1]
    # first_element[0]=15
    print(x)

    print("*********************")

def change_in_dict_student():
    students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
    first_student= students[0]
    first_student['last_name']="Bryant"
    print(first_student)

    print("*********************")

def change_in_sport_dect():
    sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
    players=sports_directory['soccer']
    players[0]='Andres'
    print(sports_directory)

    print("*********************")

def change_in_z():
    z = [ {'x': 10, 'y': 20} ]
    first=z[0]
    first['y']=30
    print(z)
print("*********************************************************")

change_in_list_x()
change_in_dict_student()
change_in_sport_dect()
change_in_z()


# Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(students):
#     for i in range (0,len(students)):
#         current_dictionary=students[i]
#         display_dictionary(current_dictionary)


# def display_dictionary(my_dict):
#     for key, value in my_dict.items():
#         print(key, ' - ', value)

# iterateDictionary(students)

def iterateDictionary(students):
    for i in range (0,len(students)):
        current_dictionary=students[i]
        display_dictionary(current_dictionary)

def display_dictionary(my_dict):
    for key in my_dict:
        print(key, ' - ', my_dict[key])

iterateDictionary(students)

print("****************************************")
# Get Values From a List of Dictionaries
def iterateDictionary2(key, students):
    for i in range(0,len(students)):
        current_dict = students[i]
        for k in current_dict :
            if(k==key):
                print(current_dict[k])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

print("******************************************")
# Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(my_dict_name):
    for k,v in my_dict_name.items():
        print(str(len(v))+"  "+ k.upper())
        for i in range(0,len(v)):
            print(v[i])

printInfo(dojo)





