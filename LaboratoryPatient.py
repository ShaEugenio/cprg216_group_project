laboratories_txt = 'laboratories.txt'
patients_txt = 'patients.txt'

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
