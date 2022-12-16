doctors_txt = 'doctors.txt'
facilities_txt = 'facilities.txt'
laboratories_txt = 'laboratories.txt'
patients_txt = 'patients.txt'


# Doctor class has 6 attributes, 10 methods
class Doctor:

    # doctor class constructor
    def __init__(self, pid=-1, name='', specialization='', working_time='', qualification='', room_number=-1):
        if pid != -1:
            self.pid = pid
        if name != '':
            self.name = name
        if specialization != '':
            self.specialization = specialization
        if working_time != '':
            self.working_time = working_time
        if qualification != '':
            self.qualification = qualification
        if room_number != -1:
            self.room_number = room_number

    # formats each doctor's information (properties) in the same format used in the .txt file (has underscores between values)
    def formatDrInfo(self, txt_to_format):
        formatted = '_'.join(txt_to_format)
        return formatted

    # asks the user to enter doctor properties (listed in the properties point)
    def enterDrInfo(self):
        self.readDoctorsFile()
        self.pid = int(input("Enter the doctor’s ID: \n"))
        self.name = input("Enter the doctor’s name: \n")
        self.specialization = input("Enter the doctor’s speciality: \n")
        self.working_time = input("Enter the doctor’s timing (e.g., 7am-10pm): \n")
        self.qualification = input("Enter the doctor’s qualification: \n")
        self.room_number = int(input("Enter the doctor’s room number: \n"))
        return [str(self.pid), self.name, self.specialization, self.working_time, self.qualification, str(self.room_number)]

    # reads from "doctors.txt" file and fills the doctor objects in a list
    def readDoctorsFile(self):
        file = open(doctors_txt, 'r')
        list_of_doctors = []
        for each_line in file:
            list_of_doctors.append(each_line.rstrip().split('_'))
        file.close()
        return list_of_doctors

    # searches whether the doctor is in the list of doctors/file using the doctor ID that the user enters
    def searchDoctorById(self):
        doctors_list = self.readDoctorsFile()
        number_of_doctors = len(doctors_list)
        current_index = 1
        last_index = number_of_doctors - 1
        found_doctor = ''
        search_id = int(input("Enter the Doctor's ID: \n"))
        # compares all the doctor IDs in the system to user input
        while current_index < number_of_doctors:
            if str(search_id) == doctors_list[current_index][0]:
                found_doctor = 'yes'
                print(
                    f'{"ID":<5}' + f'{"Name":<15}' + f'{"Specialty":<15}' + f'{"Timing":<15}' +
                    f'{"Qualification":<17}' + 'Room Number')
                print(
                    f'{doctors_list[current_index][0]:<5}' + f'{doctors_list[current_index][1]:<15}' +
                    f'{doctors_list[current_index][2]:<15}' + f'{doctors_list[current_index][3]:<15}' +
                    f'{doctors_list[current_index][4]:<17}' +
                    doctors_list[current_index][5])
            # displays a message when the doctor ID is not in the system
            if found_doctor != 'yes' and current_index == last_index:
                print("Can't find the doctor with the same ID on the system")
            current_index += 1

    # searches whether the doctor is in the list of doctors/file using the doctor name that the user enters
    def searchDoctorByName(self):
        doctors_list = self.readDoctorsFile()
        number_of_doctors = len(doctors_list)
        current_index = 1
        last_index = number_of_doctors - 1
        found_doctor = ''
        search_doctor = input("Enter the Doctor's name: \n")
        # compares all the doctor names in the system to user input
        while current_index < number_of_doctors:
            compare_doctor = doctors_list[current_index][1]
            compare_doctor = compare_doctor.replace(' ', '').lower()
            search_doctor = search_doctor.replace(' ', '').lower()
            if search_doctor == compare_doctor:
                found_doctor = 'yes'
                print(
                    f'{"ID":<5}' + f'{"Name":<15}' + f'{"Specialty":<15}' + f'{"Timing":<15}' +
                    f'{"Qualification":<17}' + 'Room Number')
                print(
                    f'{doctors_list[current_index][0]:<5}' + f'{doctors_list[current_index][1]:<15}' +
                    f'{doctors_list[current_index][2]:<15}' + f'{doctors_list[current_index][3]:<15}' +
                    f'{doctors_list[current_index][4]:<17}' +
                    doctors_list[current_index][5])
            # displays a message when the doctor name is not in the system
            if found_doctor != 'yes' and current_index == last_index:
                print("Can't find the doctor with the same name on the system")
            current_index += 1

    # displays doctor information on different lines, as a list
    def displayDoctorInfo(self):
        doctors_list = self.readDoctorsFile()
        total_rows = len(doctors_list)
        current_row = 1
        while current_row < total_rows:
            print('\nID: ' + doctors_list[current_row][0] + '\nName: ' + doctors_list[current_row][
                1] + '\nSpecialization: ' + doctors_list[current_row][2] + '\nWorking Time: ' +
                  doctors_list[current_row][3] + '\nQualification: ' + doctors_list[current_row][4] + '\nRoom Number: '
                  + doctors_list[current_row][5])
            current_row += 1

    # asks the user to enter the ID of the doctor to change their information, and then the user can enter the new doctor information
    def editDoctorInfo(self):
        id_number = int(input("Please enter the id of the doctor that you want to edit their information: \n"))
        self.pid = id_number
        doctors_list = self.readDoctorsFile()
        number_of_doctors = len(doctors_list)
        current_index = 1
        last_index = number_of_doctors - 1
        found_doctor = ''
        self.name = input("Enter new Name: \n")
        self.specialization = input("Enter new Specialist in: \n")
        self.working_time = input("Enter new Timing: \n")
        self.qualification = input("Enter new Qualification: \n")
        self.room_number = int(input("Enter new Room number: \n"))
        while current_index < number_of_doctors:
            if str(id_number) == doctors_list[current_index][0]:
                found_doctor = 'yes'
                doctors_list[current_index][1] = self.name
                doctors_list[current_index][2] = self.specialization
                doctors_list[current_index][3] = self.working_time
                doctors_list[current_index][4] = self.qualification
                doctors_list[current_index][5] = str(self.room_number)
            # display for non-existent ID
            if found_doctor != 'yes' and current_index == last_index:
                print("Can't find the doctor with the same ID on the system")
            current_index += 1
        self.writeListOfDoctorsToFile(doctors_list)

    # displays all the doctor's information, read from the file, as a report/table
    def displayDoctorsList(self):
        doctors_list = self.readDoctorsFile()
        number_of_doctors = len(doctors_list)
        current_index = 1
        print(
            f'{"ID":<10}' + f'{"Name":<15}' + f'{"Specialty":<15}' + f'{"Timing":<15}' + f'{"Qualification":<17}'
            + 'Room Number')
        while current_index < number_of_doctors:
            print(
                f'{doctors_list[current_index][0]:<10}' + f'{doctors_list[current_index][1]:<15}' +
                f'{doctors_list[current_index][2]:<15}' + f'{doctors_list[current_index][3]:<15}' +
                f'{doctors_list[current_index][4]:<17}' +
                doctors_list[current_index][5])
            current_index += 1

    # writes the list of doctors to the doctors.txt file after formatting it correctly
    def writeListOfDoctorsToFile(self, list_of_doctors):
        doctors_file = open(doctors_txt, 'w')
        for each_line in list_of_doctors:
            # calls format method before writing to file
            line = self.formatDrInfo(each_line)
            doctors_file.write(line)
            doctors_file.write('\n')
        doctors_file.close()

    # writes doctors to the doctors.txt file after formatting in correctly
    def addDrToFile(self):
        list_of_doctors = self.readDoctorsFile()
        self.writeListOfDoctorsToFile(list_of_doctors)
        add_doctor = self.enterDrInfo()
        doctors_file = open(doctors_txt, 'a')
        doctors_file.write(self.formatDrInfo(add_doctor))
        doctors_file.write('\n')
        doctors_file.close()


# Facility class has 1 property and 4 methods
class Facility:

    # facilities class constructor
    def __init__(self, facility_name=''):
        if facility_name != '':
            self.facility_name = facility_name

    # reads facilities file and returns patients list
    def readFacilitiesFile(self):
        file = open(facilities_txt, 'r')
        list_of_facilities = []
        for each_line in file:
            list_of_facilities.append(each_line.rstrip().split('_'))
        file.close()
        return list_of_facilities

    # adds and writes the facility to the file
    def addFacility(self):
        list_of_facilities = self.readFacilitiesFile()
        self.writeListOfFacilitiesToFile(list_of_facilities)
        facility_to_add = input("Enter Facility name: \n")
        facilities_file = open(facilities_txt, 'a')
        facilities_file.write(facility_to_add)
        facilities_file.close()

    # displays the list of facilities
    def displayFacilities(self):
        list_of_facilities = self.readFacilitiesFile()
        for each_line in list_of_facilities:
            formatted = ''.join(each_line)
            print(formatted)

    # writes the facilities list to facilities.txt
    def writeListOfFacilitiesToFile(self, list_of_facilities):
        facilities_file = open(facilities_txt, 'w')
        for each_line in list_of_facilities:
            formatted = ''.join(each_line)
            facilities_file.write(formatted)
            facilities_file.write('\n')
        facilities_file.close()
        
        
    # Laboratory class has 2 properties and 6 methods
class Laboratory:

    # laboratory class constructor
    def __init__(self, lab_name='', cost=''):
        if lab_name != '':
            self.lab_name = lab_name
        if cost != '':
            self.cost = cost

    # adds and writes the lab name to the file in the format of the data that is in the file
    def addLabToFile(self):
        list_of_laboratories = self.readLaboratoriesFile()
        self.writeListOfLabsToFile(list_of_laboratories)
        lab_to_add = self.enterLaboratoryInfo()
        laboratories_file = open(laboratories_txt, 'a')
        laboratories_file.write(self.formatLabInfo(lab_to_add))
        laboratories_file.write('\n')
        laboratories_file.close()

    # writes the list of labs into the file laboratories.txt
    def writeListOfLabsToFile(self, list_of_laboratories):
        laboratories_file = open(laboratories_txt, 'w')
        for each_line in list_of_laboratories:
            line = self.formatLabInfo(each_line)
            laboratories_file.write(line)
            laboratories_file.write('\n')
        laboratories_file.close()

    # displays the list of laboratories
    def displayLabsList(self):
        list_of_laboratories = self.readLaboratoriesFile()
        total_rows = len(list_of_laboratories)
        current_row = 0
        while current_row < total_rows:
            print(
                f'{list_of_laboratories[current_row][0]:<12}' + list_of_laboratories[current_row][1])
            current_row += 1

    # formats the Laboratory object similar to the laboratories.txt file
    def formatLabInfo(self, txt_to_format):
        formatted = '_'.join(txt_to_format)
        return formatted

    # asks the user to enter lab name and cost and forms a Laboratory object
    def enterLaboratoryInfo(self):
        self.lab_name = input("Enter Laboratory facility:\n")
        self.cost = int(input("Enter Laboratory cost:\n"))
        return [self.lab_name, str(self.cost)]

    # reads the laboratories.txt file and fills its contents in a list of Laboratory objects
    def readLaboratoriesFile(self):
        file = open(laboratories_txt, 'r')
        list_of_laboratories = []
        for each_line in file:
            list_of_laboratories.append(each_line.rstrip().split('_'))
        file.close()
        return list_of_laboratories


# Patient class has 5 properties and 9 methods
class Patient:

    # patient class constructor
    def __init__(self, pid=-1, name='', disease='', gender='', age=-1):
        if pid != -1:
            self.pid = pid
        if name != '':
            self.name = name
        if disease != '':
            self.disease = disease
        if gender != '':
            self.gender = gender
        if age != -1:
            self.age = age

    # formats patient information to be added to the file
    def formatPatientInfo(self, txt_to_format):
        formatted = '_'.join(txt_to_format)
        return formatted

    # asks the user to enter the patient info
    def enterPatientInfo(self):
        self.pid = int(input("Enter patients’s ID: \n"))
        self.name = input("Enter patient’s name: \n")
        self.disease = input("Enter patient's disease: \n")
        self.gender = input("Enter patient's gender: \n")
        self.age = int(input("Enter patient's age: \n"))
        return [str(self.pid), self.name, self.disease, self.gender, str(self.age)]

    # reads from file patients.txt
    def readPatientsFile(self):
        file = open(patients_txt, 'r')
        list_of_patients = []
        for each_line in file:
            list_of_patients.append(each_line.rstrip().split('_'))
        file.close()
        return list_of_patients

    # searches for a patient using their ID
    def searchPatientByID(self):
        id_number = int(input("Enter the Patient's ID: \n"))
        list_of_patients = self.readPatientsFile()
        total_rows = len(list_of_patients)
        current_row = 1
        last_row = total_rows - 1
        patient_found = ''
        while current_row < total_rows:
            if str(id_number) == list_of_patients[current_row][0]:
                print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Disease":<15}' + f'{"Gender":<15}' + "Age")
                print(f'{list_of_patients[current_row][0]:<10}' + f'{list_of_patients[current_row][1]:<15}'
                      + f'{list_of_patients[current_row][2]:<15}' + f'{list_of_patients[current_row][3]:<15}'
                      + list_of_patients[current_row][4])
                patient_found = 'yes'
            if patient_found != 'yes' and current_row == last_row:
                print("Can't find the patient with the same ID on the system")
            current_row += 1

    # Asks the user to edit patient information
    def editPatientInfo(self):
        id_number = int(input("Please enter the id of the patient that you want to edit their information: \n"))
        self.pid = id_number
        list_of_patients = self.readPatientsFile()
        total_rows = len(list_of_patients)
        current_row = 1
        last_row = total_rows - 1
        patient_found = ''
        self.name = input("Enter new Name: \n")
        self.disease = input("Enter new disease: \n")
        self.gender = input("Enter new gender: \n")
        self.age = int(input("Enter new age: \n"))
        while current_row < total_rows:
            if str(id_number) == list_of_patients[current_row][0]:
                list_of_patients[current_row][1] = self.name
                list_of_patients[current_row][2] = self.disease
                list_of_patients[current_row][3] = self.gender
                list_of_patients[current_row][4] = str(self.age)
                patient_found = 'yes'
            if patient_found != 'yes' and current_row == last_row:
                print("Can't find the doctor with the same ID on the system")
            current_row += 1
        self.writeListOfPatientsToFile(list_of_patients)

    # displays patient information on different lines, as a list
    def displayPatientInfo(self):
        list_of_patients = self.readPatientsFile()
        total_rows = len(list_of_patients)
        current_row = 1
        while current_row < total_rows:
            print('\nID: ' + list_of_patients[current_row][0] + '\nName: ' + list_of_patients[current_row][1]
                  + '\nDisease: ' + list_of_patients[current_row][2] + '\nGender: ' + list_of_patients[current_row][3]
                  + '\nAge: ' + list_of_patients[current_row][4])
            current_row += 1


    # displays the list of patients, read from the file, as a report/table
    def displayPatientsList(self):
        list_of_patients = self.readPatientsFile()
        total_rows = len(list_of_patients)
        current_row = 1
        print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Disease":<15}' + f'{"Gender":<15}' + "Age")
        while current_row < total_rows:
            print(
                f'{list_of_patients[current_row][0]:<10}' + f'{list_of_patients[current_row][1]:<15}'
                + f'{list_of_patients[current_row][2]:<15}' + f'{list_of_patients[current_row][3]:<15}'
                + list_of_patients[current_row][4])
            current_row += 1

    # writes a list of patients into the patients.txt file
    def writeListOfPatientsToFile(self, list_of_patients):
        patients_file = open(patients_txt, 'w')
        for each_line in list_of_patients:
            add_line = self.formatPatientInfo(each_line)
            patients_file.write(add_line)
            patients_file.write('\n')
        patients_file.close()

    # adds a new patient into the patients.txt file
    def addPatientToFile(self):
        list_of_patients = self.readPatientsFile()
        self.writeListOfPatientsToFile(list_of_patients)
        patient_to_add = self.enterPatientInfo()
        patients_file = open(patients_txt, 'a')
        patients_file.write(self.formatPatientInfo(patient_to_add))
        patients_file.write('\n')
        patients_file.close()
