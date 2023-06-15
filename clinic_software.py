class Doctor:
    def __init__(self, name, gender, phone, specialization, rank, username, password):
        self.name = name
        self.gender = gender
        self.phone = phone
        self.specialization = specialization
        self.rank = rank
        self.username = username
        self.password = password
        self.appointments=[]

    # def signup(self):
    #     print("--- Doctor Sign Up ---")
    #     username = input("Enter username: ")
    #     password = input("Enter password: ")
    #     name = input("Enter you full name: ")
    #     gender = input("Enter gender: ")
    #     phone = input("Enter phone: ")
    #     specialization = input("Enter specialization: ")
    #     rank = input("Enter rank: ")
    #     doctor = Doctor(name, gender, phone, specialization, rank, username, password)
    #     doctors.append(doctor)
    #     print("Doctor sign up successful.")


    def login(self):
        print("--- Doctor Login ---")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == self.username and password == self.password:
            print("Doctor login successful.")
            return True
        else:
            print("Invalid username or password.")
            return False




class Patient:
    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None
        self.phone = None
        self.medical_history = MedicalHistory()
        self.username = None
        self.password = None
        self.appointments = []

    def signup(self):
        print("--- Patient Sign Up ---")
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        print("Patient sign up successful.")

    def login(self):
        print("--- Patient Login ---")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == self.username and password == self.password:
            print("Patient login successful.")
            return True
        else:
            print("Invalid username or password.")
            return False

    def enter_patient_data(self):
        print("--- Enter Patient Data ---")
        self.name = input("Enter patient name: ")
        self.age = input("Enter patient age: ")
        self.gender = input("Enter patient gender: ")
        self.phone = input("Enter patient phone number: ")
        print("Patient data entered successfully.")

    def view_payment_details(self):
        print("--- Payment Details ---")
        print("Patient Name:", self.name)
        print("Patient Age:", self.age)
        print("Patient Gender:", self.gender)
        print("Patient Phone Number:", self.phone)
        print("Payment Status: Paid")
        print("Payment Method: Credit Card")
        print("Payment Date: May 23, 2023")
        print("Payment Amount: $100.00")
        print()

        print("Payment details viewed successfully.")

    def book_appointment(self, doctor, time):
        if time < 17 or time > 22:
            print("Appointment booking is only available between 5 PM and 10 PM.")
        else:
            print("--- Book Appointment ---")
            print("Available Doctors:")
            for index, doctor in enumerate(doctors):
                print(f"{index + 1}. {doctor.name}")
            choice = input("Enter the number of the doctor you want to choose: ")
            try:
                doctor_index = int(choice) - 1
                if 0 <= doctor_index < len(doctors):
                    doctor = doctors[doctor_index]
                    appointment_data = {
                        'patient': self,
                        'doctor': doctor,
                        'time': time
                    }
                    self.appointments.append(appointment_data)
                    print("Appointment booked successfully.")
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def cancel_appointment(self, time):
        print("--- Cancel Appointment ---")
        for appointment in self.appointments:
            if appointment['time'] == time:
                self.appointments.remove(appointment)
                print("Appointment canceled successfully.")
                return
        print("No matching appointment found.")

    def edit_appointment(self, old_time, new_time):
        print("--- Edit Appointment ---")
        for appointment in self.appointments:
            if appointment['time'] == old_time:
                appointment['time'] = new_time
                print("Appointment edited successfully.")
                return
        print("No matching appointment found.")

#from Patient import *
class Staff:
    def __init__(self):
        self.payment_method = "Credit Card"

    def update_payment_method(self, method):
        self.payment_method = method
        print("Payment method updated successfully.")

    def process_payment(self, patient, amount):
        print("--- Payment Processing ---")
        print("Patient Name:", patient.name)
        print("Payment Method:", self.payment_method)
        print("Payment Amount:", amount)
        print("Payment processed successfully.")


class MedicalHistory:
    def __init__(self):
        self.medical_data = []

    def enter_medical_data(self, symptoms, diagnosis, prescription):
        data = {
            'symptoms': symptoms,
            'diagnosis': diagnosis,
            'prescription': prescription
        }
        self.medical_data.append(data)
        print("Medical data entered successfully.")

    def edit_medical_data(self, index, symptoms, diagnosis, prescription):
        if index >= 0 and index < len(self.medical_data):
            data = self.medical_data[index]
            data['symptoms'] = symptoms
            data['diagnosis'] = diagnosis
            data['prescription'] = prescription
            print("Medical data edited successfully.")
        else:
            print("Invalid medical data index.")

    def view_medical_data(self):
        print("--- Medical History ---")
        if len(self.medical_data) == 0:
            print("No medical data.")
        else:
            for index, data in enumerate(self.medical_data):
                print("Data", index + 1)
                print("Symptoms:", data['symptoms'])
                print("Diagnosis:", data['diagnosis'])
                print("Prescription:", data['prescription'])
                print()
        print("Medical history viewed successfully.")


class Appointment:
    def __init__(self):
        self.appointments = []

    def book_appointment(self, patient, doctor, time):
        for appointment in self.appointments:
            if appointment['time'] == time:
                print("Appointment already booked for the selected time.")
                return
        appointment_data = {
            'patient': patient,
            'doctor': doctor,
            'time': time
        }
        self.appointments.append(appointment_data)
        print("Appointment booked successfully.")

    def cancel_appointment(self, patient, time):
        print("--- Cancel Appointment ---")
        for appointment in self.appointments:
            if appointment['patient'] == patient and appointment['time'] == time:
                self.appointments.remove(appointment)
                print("Appointment canceled successfully.")
                return
        print("No matching appointment found.")

    def edit_appointment(self, patient, old_time, new_time):
        print("--- Edit Appointment ---")
        for appointment in self.appointments:
            if appointment['patient'] == patient and appointment['time'] == old_time:
                appointment['time'] = new_time
                print("Appointment edited successfully.")
                return
        print("No matching appointment found.")

    def view_appointments(self, patient):
        print("--- Appointments ---")
        if len(self.appointments) == 0:
            print("No appointments booked yet.")
        else:
            for appointment in self.appointments:
                if appointment['patient'] == patient:
                    print("Doctor:", appointment['doctor'].name)
                    print("Time:", appointment['time'])
                    print()
        print("Appointments viewed successfully.")
    def view_appointments_d(self, patient):
        print("--- Doctor Appointments ---")
        if len(self.appointments) == 0:
            print("No appointments booked yet.")
        else:
            for appointment in self.appointments:
                    print("Patient:", appointment['patient'].name)
                    print("Time:", appointment['time'])
                    print()
            print("Appointments viewed successfully.")


doctor1 = Doctor("Dr. John Doe", "Male", "1234567890", "Cardiology", "Senior", "johndoe", "password")
doctor2 = Doctor("Dr. Jane Smith", "Female", "9876543210", "Pediatrics", "Junior", "mosua", "password")
staff = Staff()
appointment = Appointment()
patient = Patient()
doctors=[doctor1,doctor2]
while True:
    print("\n--- Patient Management System ---")
    print("1. Patient Sign Up")
    print("2. Patient Login")
    print("3. Doctor Sign Up")
    print("4. Doctor Login")

    print("5. View Payment Details")
    print("6. Process Payment")
    print("7. Update Payment Method")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        patient.signup()
        patient.enter_patient_data()

    elif choice == "2":
        if patient.login():

         while True:

          print("1. Enter medical history ")
          print("2. Book Appointment")
          print("3. Cancel Appointment")
          print("4. Edit Appointment")
          print("5. View Appointments")
          print("6. View Payment Details")
          print("7. Exit")
          choice = input("Enter your choice: ")
          if choice == "1":
            if patient.name is None:
                print("Patient data not entered yet.")
            else:
                symptoms = input("Enter patient symptoms: ")
                diagnosis = input("Enter diagnosis: ")
                prescription = input("Enter prescription: ")
                patient.medical_history.enter_medical_data(symptoms, diagnosis, prescription)
          elif choice == "2":
            if patient.name is None:
                print("Patient data not entered yet.")
            else:
                print("Available Doctors:")
                for index, doctor in enumerate(doctors):
                    print(f"{index + 1}. {doctor.name}")
                choice = input("Enter the number of the doctor you want to choose: ")
                time = int(input("Enter the appointment time (in 24-hour format): "))
                appointment.book_appointment(patient, choice, time)

          elif choice == "3":
            if patient.name is None:
                print("Patient data not entered yet.")
            else:
                time = int(input("Enter the appointment time (in 24-hour format): "))
                appointment.cancel_appointment(patient, time)

          elif choice == "4":
            if patient.name is None:
                print("Patient data not entered yet.")
            else:
                old_time = int(input("Enter the old appointment time (in 24-hour format): "))
                new_time = int(input("Enter the new appointment time (in 24-hour format): "))
                appointment.edit_appointment(patient, old_time, new_time)

          elif choice == "5":
            if patient.name is None:
                print("Patient data not entered yet.")
            else:
                appointment.view_appointments(patient)
          elif choice == "6":
              if patient.name is None:
                  print("Patient data not entered yet.")
              else:
                  patient.view_payment_details()

          elif choice == "7":
              print("Exiting...")
              break






    elif choice == "3":
        print("--- Doctor Sign Up ---")
        username = input("Enter username: ")
        password = input("Enter password: ")
        name = input("Enter you full name: ")
        gender = input("Enter gender: ")
        phone = input("Enter phone: ")
        specialization = input("Enter specialization: ")
        rank = input("Enter rank: ")
        doctor = Doctor(name, gender, phone, specialization, rank, username, password)
        doctors.append(doctor)
        print("Doctor sign up successful.")

    elif choice == "4":
        if doctor1.login():
            appointment.view_appointments_d(patient)
        print("1. Write Prescription")
        print("2. View Patient Medical History")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            if patient.name is None:
                print("Patient data not entered yet.")
            else:
                patient.medical_history.view_medical_data()
                index = int(input("Enter the index of the medical data to edit: ")) - 1
                if index >= 0 and index < len(patient.medical_history.medical_data):
                    symptoms = input("Enter new symptoms: ")
                    diagnosis = input("Enter new diagnosis: ")
                    prescription = input("Enter new prescription: ")
                    patient.medical_history.edit_medical_data(index, symptoms, diagnosis, prescription)
                else:
                    print("Invalid medical data index.")
        elif choice == "2":
            if patient.username is None:
                print("Please sign up or login first.")
            else:
                if patient.name is None:
                    print("Patient data not entered yet.")
                else:
                    patient.medical_history.view_medical_data()
        elif choice == "3":
            print("Exiting...")
            break

    elif choice == "5":
        if patient.username is None:
            print("Please sign up or login first.")
        else:
            if patient.name is None:
                print("Patient data not entered yet.")
            else:
                patient.view_payment_details()
    elif choice == "8":
        method = input("Enter the new payment method: ")
        staff.update_payment_method(method)


    elif choice == "6":
        if patient.username is None:
            print("Please sign up or login first.")
        else:
            if patient.name is None:
                print("Patient data not entered yet.")
            else:
                amount = float(input("Enter the payment amount: "))
                staff.process_payment(patient, amount)
    elif choice == "7":
        if patient.username is None:
            print("Please sign up or login first.")
        else:
            method = input("Enter the new payment method: ")
            staff.update_payment_method(method)

    elif choice == "9":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
