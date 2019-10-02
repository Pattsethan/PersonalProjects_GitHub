'''Python script to prepare online study materials'''
#!/usr/bin/env python3
import os
import json
import webbrowser
class StartHallway():
    '''docstring'''
    def __init__(self):
        self.jsonpath = "notebook.json"
        self.notebook = open(self.jsonpath, "r")
        self.courses = []
        self.classroom = []

    def entrance(self):
        '''Loads userdata from Json file "notebook" and prompts user based on the data in Json file'''

        with open(self.jsonpath) as notebook:
            data = json.load(notebook)
            courses = []
            for course in data['Courses']:
                courses.append(course)
            while True:
                classroom = input(f"Where ya headed?\n {str(courses)[1:-1]}: \n")
                if classroom == "settings":
                    self.settings()
                else:
                    try:
                        for pages in data['Courses'][classroom].get("urls"):
                            webbrowser.get('chrome').open_new(pages)
                            try:
                                for materials in data['Courses'][classroom].get("applications"):
                                    if materials == "texteditor":
                                        os.system("code front.txt")
                                        break
                                    else:
                                        break
                            except SystemError:
                                print("No Applications")
                                break
                    except KeyError:
                        continue
                print("Goodbye.")
                break

    def settings(self):
        '''Allows user to add or delete a "class" within the notebook.json file'''
        materiallist = []
        urllist = []
        while True:
            options = input("What would you like to do?:\
                \n     Add a Class? (a) \n     Delete a Class? (d) \n")
            if options == "a":
                with open(self.jsonpath) as notebook:
                    data = json.load(notebook)
                    a_dict = data
                    addname = input("What is the Name of the Course? \n")
                with open(self.jsonpath, 'w') as notebook:
                    while True:
                        addpages = input("Please enter any course Urls you would like to add: \n")
                        morepages = input("Would you like to another? (y/n): \n")
                        if morepages == "n":
                            urllist.append(addpages)
                            break
                        else:
                            urllist.append(addpages)
                            continue
                    print(urllist)

                    while True:
                        addmaterials = input("please add any materials you need for \
                            this class: \n texteditor\n none\n")
                        if addmaterials == "none":
                            break
                        else:
                            morematerials = input("Would you like to another? (y/n): \n")
                            if morematerials == "n":
                                materiallist.append(addmaterials)
                                break
                            else:
                                materiallist.append(addmaterials)
                                continue
                    a_dict['Courses'].update({addname:{}})
                    a_dict['Courses'][addname].update({"urls":urllist})
                    a_dict['Courses'][addname].update({"applications":materiallist})
                    data.update(a_dict)
                    json.dump(data, notebook)
            elif options == "d":
                with open(self.jsonpath) as notebook:
                    data = json.load(notebook)
                    courses = []
                    for course in data['Courses']:
                        courses.append(course)
                    deleteclass = input(f"what class would you like to remove?:\n\
                        {str(courses)[1:-1]}: \n")

                with open(self.jsonpath, 'r') as data_file:
                    deletedata = json.load(data_file)
                    b_dict = deletedata
                    b_dict['Courses'].pop(deleteclass, None)
                    deletedata.update(b_dict)
                with open(self.jsonpath, 'w') as data_file:
                    json.dump(deletedata, data_file)
                break
            else:
                continue
            break

START = StartHallway()
START.entrance()
