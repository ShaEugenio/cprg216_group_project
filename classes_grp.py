# Assignment IV: Classes
# Author: Zoë Goodwin, ID# 897676; 2022-12-07


class Doctor:
    def __init__(self, id, name, specialization, workingtime, qualification, roomnumber):
        self.__id = id
        self.__name = name
        self.__spec = specialization
        self.__workt = workingtime
        self.__qual = qualification
        self.__room = roomnumber

    # Will format each doctor's information as found in doctors.txt
    def formatDrInfo(self):

    # Asks the user to enter the doctor's information
    @classmethod
    def enterDrInfo(cls):
        id = int(input('Enter ID: '))
        name = input('Enter name: ')
        specialization = input('Enter specialization: ')
        workingtime = input('Enter working time: ')
        qualification = input('Enter qualification: ')
        roomnumber = int(input('Enter room number: '))
        print('Back to the previous menu\n\n')
        return cls(id, name, specialization, workingtime, qualification, roomnumber)

    # Reads the information from doctors.txt
    @classmethod
    def readDoctorsFile(cls):
        doctors_list_all = []
        with open('doctors.txt', 'r') as doctors_txt:
            for line in doctors_txt:
                id_str, name, specialization, workingtime, qualification, roomnumber = line.strip().split('_')
                doctors_list_all.append(Doctor(id_str, name, specialization, workingtime, qualification, roomnumber))
        return doctors_list_all

    # Searches doctors.txt to see whether doctor ID entered is listed
    @classmethod
    def searchDoctorById(cls, __id):
        with open('doctors.txt', 'r') as search_id:
            field_titles = search_id.readline()
            print(field_titles)
            for line in search_id:
                id_str, name, specialization, workingtime, qualification, roomnumber = line.strip().split('_')
                if int(id_str) == __id:
                    print(line)
                    return
        print('Cannot find a doctor with that ID number.\n')

    # Searches doctors.txt to see whether doctor Name entered is listed
    @classmethod
    def searchDoctorByName(cls, __name):
        with open('doctors.txt','r') as search_name:
            field_titles = search_name.readline()
            print(field_titles)
            for line in search_name:
                id_str, name, specialization, workingtime, qualification, roomnumber = line.strip().split('_')
                if name == __name:
                    list(line)
                    return
        print('Cannot find a doctor with that name.\n')

    # Displays selected doctor's information from doctors.txt as a list
    @staticmethod
    def displayDoctorInfo(self):
        doctor_list_single = []


    # Asks user to enter doctor ID to change information, then lets user change it
    def editDoctorInfo(self):

    # Displays information of all doctors from doctors.txt as a table.
    @staticmethod
    def displayDoctorsList(self):
        for doctor in self.doctors_list_all:
            print(f'{doctor.id_str:<10} {doctor.name:<30} {doctor.specialization:<20} {doctor.workingtime:<20} {doctor.qualification:<20} {doctor.roomnumber}')
        print('Back to the previous menu')

    # Correctly formats, and then writes the list of doctors to doctors.txt
    def writeListOfDoctorsToFile(self):

    # Correctly formats, and writes a single doctor entry to doctors.txt
    def addDrToFile(self):
        with open('doctors.txt', 'a') as add_doctor:
            add_doctor.write(f'{self.__id}_{self.__name}_{self.__spec}_{self.__workt}_{self.__qual}_{self.__room}\n')




class Laboratory:
    def __init__(self, Lab_Name, Cost):
        self.__Lab_Name = Lab_Name
        self.__Lab_Cost = Cost
    # Adds and writes the lab name to laboratories.txt
    def addLabToFile(self):

    # Writes the list of labs into laboratories.txt
    def writeListOfLabsToFile(self):

    # Displays the list of laboratories
    def displayLabsList

    # Formats the laboratory object similar to existing entries in laboratories.txt
    def formatLabInfo

    # Asks the user to enter lab name and cost, then creates a laboratory object
    def enterLaboratoryInfo

    # Reads laboratories.txt and fills its contents with a list of laboratory objects
    def readLaboratoriesFile

