# CPRG 216 Project: Management System Program for Alberta Hospital
# Authors: Bryan Zhou, Zoe Goodwin, Sha Eugenio
# This program has management class that takes care of the navigation, user prompts, and program continuity.
# Doctor class for information management which can be used to display, search, add and edit doctor information when
# called. Facilities class can add and display facilities when called. Read method for facilities class was also added
# for consistency with the other classes. Laboratories class can display and add laboratory name and corresponding
# price. Patient class can display, add, and edit patients' information when called. This program does not provide
# input validation, so it assumes user is entering the correct data type. Program runs continuously unless the user
# enters 0 on the main menu, only then that it terminates.

from Hospital import Doctor, Facility, Laboratory, Patient

doctor_navigation = Doctor()
facility_navigation = Facility()
laboratory_navigation = Laboratory()
patient_navigation = Patient()

class Management:

    # navigates through the program by user input
    def DisplayMenu(self):
        main_menu = int(input("Welcome to Alberta Hospital (AH) Management system \nSelect from the following options, "
                              "or select 0 to stop:\n1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients\n"))

        # gets out of the loop when 0 is entered for main_menu
        while main_menu != 0:
            # doctor class navigation
            while main_menu == 1:
                doctors_option = int(input(
                    "Doctor Menu:\n1 - Display Doctors List\n2 - Search for doctor by ID\n3 - Search for doctor by "
                    "name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n"))

                if doctors_option == 1:
                    doctor_navigation.displayDoctorsList()
                    print("\nBack to the previous Menu\n")
                elif doctors_option == 2:
                    doctor_navigation.searchDoctorById()
                    print("\nBack to the previous Menu\n")
                elif doctors_option == 3:
                    doctor_navigation.searchDoctorByName()
                    print("\nBack to the previous Menu\n")
                elif doctors_option == 4:
                    doctor_navigation.addDrToFile()
                    print("\nBack to the previous Menu\n")
                elif doctors_option == 5:
                    doctor_navigation.editDoctorInfo()
                    print("\nBack to the previous Menu\n")
                elif doctors_option == 6:
                    main_menu = int(input("Welcome to Alberta Hospital (AH) Management system \nSelect from the "
                                          "following options, or select 0 to stop:\n1 - Doctors\n2 - Facilities\n3 - "
                                          "Laboratories\n4 - Patients\n"))
            # facility class navigation
            while main_menu == 2:
                facilities_option = int(input("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - "
                                              "Back to the Main Menu\n"))
                if facilities_option == 1:
                    facility_navigation.displayFacilities()
                    print("\nBack to the previous Menu\n")
                elif facilities_option == 2:
                    facility_navigation.addFacility()
                    print("\nBack to the previous Menu\n")
                elif facilities_option == 3:
                    main_menu = int(input("Welcome to Alberta Hospital (AH) Management system \nSelect from the "
                                          "following options, or select 0 to stop:\n1 - Doctors\n2 - Facilities\n3 - "
                                          "Laboratories\n4 - Patients\n"))
            # laboratory class navigation
            while main_menu == 3:
                laboratories_option = int(input("Laboratories Menu:\n1 - Display laboratories list\n2 - Add "
                                                "laboratory\n3 - Back to the Main Menu\n"))
                if laboratories_option == 1:
                    laboratory_navigation.displayLabsList()
                    print("\nBack to the previous Menu\n")
                elif laboratories_option == 2:
                    laboratory_navigation.addLabToFile()
                    print("\nBack to the previous Menu\n")
                elif laboratories_option == 3:
                    main_menu = int(input("Welcome to Alberta Hospital (AH) Management system \nSelect from the "
                                          "following options, or select 0 to stop:\n1 - Doctors\n2 - Facilities\n3 - "
                                          "Laboratories\n4 - Patients\n"))
            # patient class navigation
            while main_menu == 4:
                patients_option = int(input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by "
                                            "ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n"))
                if patients_option == 1:
                    patient_navigation.displayPatientsList()
                    print("\nBack to the previous Menu\n")
                elif patients_option == 2:
                    patient_navigation.searchPatientByID()
                    print("\nBack to the previous Menu\n")
                elif patients_option == 3:
                    patient_navigation.addPatientToFile()
                    print("\nBack to the previous Menu\n")
                elif patients_option == 4:
                    patient_navigation.editPatientInfo()
                    print("\nBack to the previous Menu\n")
                elif patients_option == 5:
                    main_menu = int(input(
                        "Welcome to Alberta Hospital (AH) Management system \nSelect from the following options, or "
                        "select 0 to stop:\n1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients\n"))


# management object
menu_navigation = Management()
# starts the program
menu_navigation.DisplayMenu()

