#making glossary
programming_terms = {
    "variable": 'A container that holds a value or information.',
    "function": 'A way to organize and reuse code that is used to perform a single, related action.',
    "loop": 'A way to repeat a block of codemultiple times.',
    "list": 'A data structure that is a collection of elements, each identified by at least one index or key.',
    "float": 'A data type with whole numbers and decimal numbers',
    "Integer" : 'is a data type with only whole numbers. \n',
    "Boolean" : 'means true or false. \n',
    "Tuple" : 'is similar to a list, but you cannot update the values within it. \n',
    "Repository" : 'is where all the files for a project is stored. \n',
    "Push" : 'is to move files from one repository to another. \n',
                     
}
# print loop
for key in programming_terms.keys():
    print(key.title(), programming_terms[key])
