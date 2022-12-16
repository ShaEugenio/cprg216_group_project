

file_for_Doctor ='doctors.txt'
list_of_doctors = []
file_for_facilities = 'facilities.txt'
list_of_facilities = []
file_for_Laboratory ='laboratories.txt'
list_of_Laboratory =[]
file_for_patients ='patients.txt'
list_of_patients =[]

class Doctor:
    def __init__(self,ID, Name, Specialization, Working_Time, Qualification, Room_Number):
        self.ID = ID
        self.Name = Name
        self.Specialization = Specialization
        self.Working_Time = Working_Time
        self.Qualification = Qualification
        self.Room_Number = Room_Number

    def formatDrInfo(self):
        format()
        return format()
    def enterDrInfo(self):
        self.readDoctorsFile()
        self.ID = int(input("Doctor's ID\n"))
        self.Name = input("Doctor's Name\n")
        self.Specialization = input("Doctor's Specialization\n")
        self.Working_Time = input("Doctor's Working_Time\n")
        self.Qualification = input("Doctor's Qualification\n")
        self.Room_Number = input("Doctor's Room_Number\n")
        list=[]
        list.append(Doctor(self.ID, self.Name, self.Specialization, self.Working_Time,self.Qualification,self.Room_Number ))

    def readDoctorsFile(self):
            file01 = open("doctors.txt",'r')
            file01.close()

    def searchDoctorById(self):
        doctorID=int(input("please enter doctor's id"))
        if doctorID.strip() == self.ID.strip():
            print("yes, doctor is here")
            print(self.ID, self.Name, self.Specialization, self.Working_Time,self.Qualification,self.Room_Number)
    def searchDoctorByName(self):
        doctorName = int(input("please enter doctor's name"))
        if doctorName.strip() == self.Name.strip():
            print("yes, doctor is here")
            print(self.ID, self.Name, self.Specialization, self.Working_Time,self.Qualification,self.Room_Number)
    def displayDoctorInfo(self):
        for each_row in list_of_doctors:
            print(each_row)
    def editDoctorInfo(self):
        id_number = int(input("Please enter the doctor ID to edit : \n"))
        self.id = id_number
        generalrow = len(list_of_doctors)
        nowrow = 1
        last_row = generalrow - 1
        doctor_found = ''
        self.name = input("Please enter a new Name: \n")
        self.specialization = input("Please enter a new Specialist in: \n")
        self.working_time = input("Please enter new Timing: \n")
        self.qualification = input("Please enter new Qualification: \n")
        self.room_number = int(input("Please enter new Room number: \n"))
        while nowrow < generalrow:
            if str(id_number) == list_of_doctors[nowrow][0]:
                list_of_doctors[nowrow][1] = self.name
                list_of_doctors[nowrow][2] = self.specialization
                list_of_doctors[nowrow][3] = self.working_time
                list_of_doctors[nowrow][4] = self.qualification
                list_of_doctors[nowrow][5] = str(self.room_number)
                doctor_found = 'yes'
            if doctor_found != 'yes' and nowrow == last_row:
                print("Can't find the doctor with the same ID on the system")
            nowrow += 1
        self.writeListOfDoctorsToFile()
    def displayDoctorsList(self):
        for each_row in list_of_doctors:
            print(each_row)

        generalrow = len(list_of_doctors)
        nowrow = 1
        print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Specialty":<15}' + f'{"Timing":<15}' + f'{"Qualification":<17}' + 'Room Number')
        while nowrow < generalrow:
            print(f'{list_of_doctors[nowrow][0]:<10}' + f'{list_of_doctors[nowrow][1]:<15}' + f'{list_of_doctors[nowrow][2]:<15}' + f'{list_of_doctors[nowrow][3]:<15}' + f'{list_of_doctors[nowrow][4]:<17}' + list_of_doctors[nowrow][5])
            nowrow += 1

class Facility:
    def __init__(self, facility_name):
            self.facility_name = facility_name
            self.__facility_list = []  # as a private list
            self.__facility_list.append(Facility)
            print("added")

    def addFacility(self):
        self.__facility_list.append(Facility)

    def displayFacilities(self):
        for Facility in self.__facility_list:
            print("new is:", Facility)
            print("")
        faci = Facility("ER")
        faci.displayFacilities()

    def writeListOffacilitiesToFile(self):
        facilities_file = open(file_for_facilities, 'w')
        for each_line in list_of_facilities:
            line = each_line
            facilities_file.write(line)
            facilities_file.write('\n')
            facilities_file.close()

class Laboratory:
    def __init__(self, lab_name, cost):
        self.lab_name = lab_name
        self.cost = cost

    def addLabToFile(self, new_lab):
        self.__Laboratory_list.append(Laboratory)

    def writeListOfLabsToFile(self):
        Laboratory_file = open(file_for_Laboratory, 'w')
        for each_line in list_of_facilities:
            line = each_line
            Laboratory_file.write(line)
            Laboratory_file.write('\n')
        Laboratory_file.close()

    def displayLabsList(self):
        for Laboratory in self.__Laboratory_list:
            print("new is:", Laboratory)
            print("")

        lab01 = Laboratory("ER")

        lab01.displayLabsList()

    def formatLabInfo(self):
        format()
        return format()

    def enterLaboratoryInfo(self):
        self.lab_name = input("Please enter Laboratory facility:\n")
        self.cost = int(input("Please enter Laboratory cost:\n"))
        new_lab = [self.lab_name, str(self.cost)]
        self.addLabToFile(new_lab)

    def readLaboratoriesFile(self):
        file = open(file_for_Laboratory, 'r')
        for each_line in file:
            list_of_Laboratory.append(each_line.rstrip().split('_'))
        file.close()


class Patient:
    def __init__(self, pid, name, disease, gender, age):
            self.pid = pid
            self.name = name
            self.disease = disease
            self.gender = gender
            self.age = age

    def formatPatientInfo(self):
        format()
        return format()

    def enterPatientInfo(self):
        self.pid=int(input("please enter the patients’s ID: \n"))
        self.name = input("please enter the name of patient: \n")
        self.disease = input("please enter the disease of patient: \n")
        self.gender = input("please enter gender of patient: \n")
        self.age = int(input("please enter the age of patient: \n"))
        return [str(self.pid), self.name, self.disease, self.gender, str(self.age)]

    def readPatientsFile(self):
        file = open(file_for_patients, 'r')
        list_of_patients = []
        for each_line in file:
            list_of_patients.append(each_line.rstrip().split('_'))
        file.close()
        return list_of_patients

    def searchPatientById(self):
        self.pid =int(input("please enter the Patient's ID: \n"))
        list_of_patients = self.readPatientsFile()
        generalrow = len(list_of_patients)
        nowrow = 1
        last_row = generalrow - 1
        patient_found = ''
        while nowrow < generalrow:
            if str('pid') == list_of_patients[nowrow][0]:
                print(f'{"ID"}' + f'{"Name"}' + f'{"Disease"}' + f'{"Gender"}' + "Age")
                print(
                    f'{list_of_patients[nowrow][0]:<10}' + f'{list_of_patients[nowrow][1]:<15}' + f'{list_of_patients[nowrow][2]:<15}' + f'{list_of_patients[nowrow][3]:<15}' +
                    list_of_patients[nowrow][4])
                patient_found = 'yes'
            if patient_found != 'yes' and nowrow == last_row:
                print("Can't find the patient with the same ID on the system")
            nowrow += 1
    def editPatientInfo(self):
        self.pid=int(input("please enter the patients’s ID: \n"))
        self.name = input("please enter the name of patient: \n")
        self.disease = input("please enter the disease of patient: \n")
        self.gender = input("please enter gender of patient: \n")
        self.age = int(input("please enter the age of patient: \n"))
        list = []
        list.append(
            Patient(self.PID, self.Name, self.Diesease, self.Gender, self.Age))

    def displayPatientsList(self):
        patients_file = open(file_for_patients, 'w')
        for each_line in list_of_patients:
            line = each_line
            patients_file.write(line)
            patients_file.write('\n')
        patients_file.close()
    def writeListOfPatientsToFile(self):
        patients_file = open(file_for_patients, 'w')
        for each_line in list_of_patients:
            line = each_line
            patients_file.write(line)
            patients_file.write('\n')
        patients_file.close()
    def addPatientToFile(self):
        self.__patients_list.append(list_of_patients)

class management:
    def DisplayMenu(self,user):
        self.user = user
        user=input("ID number")
        selection= int(input("please input number"))
        if selection==1:
            Doctor()
        if selection==2:
            Facility()
        if selection==3:
            Laboratory()
        if selection==4:
            Patient()
        elif selection ==0:
            print("Quit")

