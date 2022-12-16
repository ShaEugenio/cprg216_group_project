doctors_txt = 'doctors.txt'
facilities_txt = 'facilities.txt'


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
