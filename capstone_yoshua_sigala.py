import tabulate

# Initial Database
patients = [
    {'Patient ID': '001', 'Name': 'Patricia Taylor', 'Age': 29, 'Gender': 'Male', 'Diagnosis': 'Hypertension', 'Disease Type': 'Non-Infectious', 'Severity': 'Progressive', 'Department': 'Cardiology', 'Status': 'Outpatient'},
    {'Patient ID': '002', 'Name': 'Mary Hernandez', 'Age': 48, 'Gender': 'Female', 'Diagnosis': 'Hepatitis', 'Disease Type': 'Non-Infectious', 'Severity': 'Chronic', 'Department': 'Cardiology', 'Status': 'Outpatient'},
    {'Patient ID': '003', 'Name': 'James Anderson', 'Age': 67, 'Gender': 'Female', 'Diagnosis': "Alzheimer's", 'Disease Type': 'Non-Infectious', 'Severity': 'Progressive', 'Department': 'Oncology', 'Status': 'Inpatient'},
    {'Patient ID': '004', 'Name': 'Linda Martinez', 'Age': 35, 'Gender': 'Male', 'Diagnosis': 'COVID-19', 'Disease Type': 'Infectious', 'Severity': 'Progressive', 'Department': 'General Medicine', 'Status': 'Inpatient'},
    {'Patient ID': '005', 'Name': 'Linda Martinez', 'Age': 80, 'Gender': 'Female', 'Diagnosis': 'Pneumonia', 'Disease Type': 'Infectious', 'Severity': 'Chronic', 'Department': 'Pulmonology', 'Status': 'Inpatient'},
    {'Patient ID': '006', 'Name': 'James Anderson', 'Age': 50, 'Gender': 'Female', 'Diagnosis': 'Migraine', 'Disease Type': 'Infectious', 'Severity': 'Acute', 'Department': 'Pulmonology', 'Status': 'Inpatient'},
    {'Patient ID': '007', 'Name': 'David Wilson', 'Age': 39, 'Gender': 'Female', 'Diagnosis': "Parkinson's", 'Disease Type': 'Infectious', 'Severity': 'Progressive', 'Department': 'Neurology', 'Status': 'Outpatient'},
    {'Patient ID': '008', 'Name': 'Patricia Taylor', 'Age': 55, 'Gender': 'Male', 'Diagnosis': 'Cancer', 'Disease Type': 'Infectious', 'Severity': 'Acute', 'Department': 'Oncology', 'Status': 'Inpatient'},
    {'Patient ID': '009', 'Name': 'David Wilson', 'Age': 76, 'Gender': 'Male', 'Diagnosis': 'Heart Disease', 'Disease Type': 'Infectious', 'Severity': 'Progressive', 'Department': 'Cardiology', 'Status': 'Outpatient'},
    {'Patient ID': '010', 'Name': 'Emily Davis', 'Age': 80, 'Gender': 'Female', 'Diagnosis': "Parkinson's", 'Disease Type': 'Infectious', 'Severity': 'Progressive', 'Department': 'Neurology', 'Status': 'Outpatient'},
    {'Patient ID': '011', 'Name': 'Chris Lee', 'Age': 70, 'Gender': 'Female', 'Diagnosis': 'Heart Disease', 'Disease Type': 'Infectious', 'Severity': 'Chronic', 'Department': 'Cardiology', 'Status': 'Outpatient'},
    {'Patient ID': '012', 'Name': 'Mary Hernandez', 'Age': 68, 'Gender': 'Female', 'Diagnosis': 'Migraine', 'Disease Type': 'Non-Infectious', 'Severity': 'Progressive', 'Department': 'General Medicine', 'Status': 'Inpatient'},
    {'Patient ID': '013', 'Name': 'Mary Hernandez', 'Age': 69, 'Gender': 'Female', 'Diagnosis': 'Pneumonia', 'Disease Type': 'Non-Infectious', 'Severity': 'Chronic', 'Department': 'Cardiology', 'Status': 'Outpatient'},
    {'Patient ID': '014', 'Name': 'Patricia Taylor', 'Age': 27, 'Gender': 'Male', 'Diagnosis': 'Heart Disease', 'Disease Type': 'Infectious', 'Severity': 'Acute', 'Department': 'Cardiology', 'Status': 'Outpatient'},
    {'Patient ID': '015', 'Name': 'Emily Davis', 'Age': 47, 'Gender': 'Male', 'Diagnosis': "Parkinson's", 'Disease Type': 'Infectious', 'Severity': 'Acute', 'Department': 'Oncology', 'Status': 'Outpatient'}
]

# CRUD functions
def create_patient():
    while True:
        print("\n1. Create new patient data")
        print("2. Return to home menu")
        choice = input("Choose an option: ")

        if choice == '1':
            patient_id = input("\nEnter Patient ID: ")
            if any(patient['Patient ID'] == patient_id for patient in patients):
                print("Data already exists")
                return create_patient

            # Get remaining details
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender: ")
            diagnosis = input("Enter Diagnosis: ")
            disease_type = input("Enter Disease Type (Infectious/Non-Infectious): ")
            severity = input("Enter Severity (Acute/Chronic/Progressive): ")
            department = input("Enter Department (General Medicine, Cardiology, Pulmonology, Neurology, Oncology): ")
            status = input("Enter Status (Inpatient/Outpatient): ")

            # Confirmation to save
            confirm = input("Save data? (yes/no): ")
            if confirm.lower() == 'yes':
                patients.append({
                    "Patient ID": patient_id,
                    "Name": name,
                    "Age": age,
                    "Gender": gender,
                    "Diagnosis": diagnosis,
                    "Disease Type": disease_type,
                    "Severity": severity,
                    "Department": department,
                    "Status": status
                })
                print("Data successfully saved")
            else:
                print("Data not saved")
        elif choice == '2':
            return
        else:
            print("Invalid choice. Please try again.")

def read_patient():
    while True:
        print("\n1. View all patient data")
        print("2. View patient by ID")
        print("3. Return to home menu")
        choice = input("Choose an option: ")

        if choice == '1':
            if not patients:
                print("No data exists")
            else:
                print(tabulate.tabulate(patients, headers="keys", tablefmt="github"))
        elif choice == '2':
            if not patients:
                print("No data exists")
            else:
                patient_id = input("Enter Patient ID: ")
                patient = next((p for p in patients if p["Patient ID"] == patient_id), None)
                if patient:
                    print(tabulate.tabulate([patient], headers="keys", tablefmt="github"))
                else:
                    print("Patient not found")
        elif choice == '3':
            return
        else:
            print("Invalid choice. Please try again.")

def update_patient():
    while True:
        print("\n1. Update patient data")
        print("2. Return to home menu")
        choice = input("Choose an option: ")

        if choice == '1':
            patient_id = input("\nEnter Patient ID to update: ")
            patient = next((p for p in patients if p["Patient ID"] == patient_id), None)

            if not patient:
                print("Data you're looking for doesn't exist")
            else:
                print("Current data:")
                print(tabulate.tabulate([patient], headers="keys", tablefmt="github"))

                # Update fields - if input is empty, keep previous data
                name = input(f"\nEnter Name (leave empty to keep '{patient['Name']}'): ") or patient["Name"]
                age = input(f"Enter Age (leave empty to keep '{patient['Age']}'): ") or patient["Age"]
                gender = input(f"Enter Gender (leave empty to keep '{patient['Gender']}'): ") or patient["Gender"]
                diagnosis = input(f"Enter Diagnosis (leave empty to keep '{patient['Diagnosis']}'): ") or patient["Diagnosis"]
                disease_type = input(f"Enter Disease Type (leave empty to keep '{patient['Disease Type']}'): ") or patient["Disease Type"]
                severity = input(f"Enter Severity (leave empty to keep '{patient['Severity']}'): ") or patient["Severity"]
                department = input(f"Enter Department (leave empty to keep '{patient['Department']}'): ") or patient["Department"]
                status = input(f"Enter Status (leave empty to keep '{patient['Status']}'): ") or patient["Status"]

                # Update patient data
                patient.update({
                    "Name": name,
                    "Age": age,
                    "Gender": gender,
                    "Diagnosis": diagnosis,
                    "Disease Type": disease_type,
                    "Severity": severity,
                    "Department": department,
                    "Status": status
                })

                print("Data successfully updated")
        elif choice == '2':
            return
        else:
            print("Invalid choice. Please try again.")

def delete_patient():
    while True:
        print("\n1. Delete patient data")
        print("2. Return to home menu")
        choice = input("Choose an option: ")

        if choice == '1':
            patient_id = input("Enter Patient ID to delete: ")
            patient = next((p for p in patients if p["Patient ID"] == patient_id), None)
            if not patient:
                print("Data you're looking for doesn't exist")
            else:
                print("Data to delete:")
                print(tabulate.tabulate([patient], headers="keys", tablefmt="github"))
                confirm = input("Confirm delete? (yes/no): ")
                if confirm.lower() == 'yes':
                    patients.remove(patient)
                    print("Data successfully deleted")
                else:
                    print("Data not deleted")
        elif choice == '2':
            return
        else:
            print("Invalid choice. Please try again.")

def search_patient():
    field_map = {
        "1": "Patient ID",
        "2": "Name",
        "3": "Age",
        "4": "Gender",
        "5": "Diagnosis",
        "6": "Disease Type",
        "7": "Severity",
        "8": "Department",
        "9": "Status"
    }
    print("\nSearch by fields:")
    for key, value in field_map.items():
        print(f"{key}. {value}")
    field_choice = input("Choose a field to search: ")
    field = field_map.get(field_choice)

    if field:
        term = input(f"Enter {field} to search for: ")
        results = [p for p in patients if p.get(field) == term]
        if results:
            print(tabulate.tabulate(results, headers="keys", tablefmt="github"))
        else:
            print("No matching records found")
    else:
        print("Invalid field choice")


def calculate_payment():
    patient_id = input("Enter Patient ID: ")  # Keep patient_id as a string
    for patient in patients:
        if patient["Patient ID"] == patient_id:
            print("\nPatient Information:")
            print(f"ID: {patient['Patient ID']}")
            print(f"Name: {patient['Name']}")
            print(f"Age: {patient['Age']}")
            print(f"Gender: {patient['Gender']}")
            print(f"Diagnosis: {patient['Diagnosis']}")

            # Calculate bill breakdown
            base_cost = 7500000 if patient["Disease Type"] == "Infectious" else 5000000
            severity_cost = {"Acute": 2000000, "Chronic": 3000000, "Progressive": 5000000}[patient["Severity"]]
            department_cost = {"General Medicine": 2500000, "Cardiology": 3000000, "Pulmonology": 7000000,
                               "Neurology": 10000000, "Oncology": 12000000}[patient["Department"]]
            status_cost = 3000000 if patient["Status"] == "Inpatient" else 1000000

            total_cost = base_cost + severity_cost + department_cost + status_cost

            # Prepare tabulate data
            bill_details = [
                ["Disease Type", patient["Disease Type"], f"Rp.{base_cost:,}"],
                ["Severity", patient["Severity"], f"Rp.{severity_cost:,}"],
                ["Department", patient["Department"], f"Rp.{department_cost:,}"],
                ["Status", patient["Status"], f"Rp.{status_cost:,}"],
                ["Total Amount Due", "", f"Rp.{total_cost:,}"]
            ]

            # Display bill breakdown using tabulate
            print("\nBill Breakdown:")
            print(tabulate.tabulate(bill_details, headers=["Description", "Detail", "Cost"], tablefmt="grid"))

            # Payment process
            while True:
                try:
                    amount_paid = int(input("\nEnter payment amount: Rp."))
                    if amount_paid < total_cost:
                        print(f"Amount is not enough. You still owe: Rp.{total_cost - amount_paid:,}")
                    else:
                        change = amount_paid - total_cost
                        if change > 0:
                            print(f"Payment successful. Change returned: Rp.{change:,}")
                        else:
                            print("Payment successful.")
                        patients.remove(patient)
                        return
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            return
    print("Patient not found")

def display_info():
    info_text = """
    Hospital Patient Database Information:

    Fields:
    - Patient ID: A unique identifier assigned to each patient for easy tracking and management.
    - Name      : Full name of the patient.
    - Age       : Age of the patient in years.
    - Gender    : Gender of the patient (Male/Female).
    - Diagnosis : The diagnosed condition or disease as described by medical staff.

    Disease Type:
    - Infectious    : Diseases caused by pathogenic microorganisms, such as bacteria, viruses, parasites, or fungi. These can spread directly or indirectly.
    - Non-Infectious: Diseases not caused by infectious agents. These include chronic conditions like diabetes, heart disease, and cancer.

    Severity:
    - Acute         : Sudden onset of severe symptoms that require immediate attention but are usually of short duration.
    - Chronic       : Long-term conditions that may not be severe initially but persist over a longer period and require ongoing management.
    - Progressive   : Conditions that gradually worsen over time, often requiring more intensive treatment as the disease advances.

    Department:
    - General Medicine  : Provides primary healthcare and general medical services, covering a wide range of medical issues.
    - Cardiology        : Specialized department focusing on heart-related conditions and treatments.
    - Pulmonology       : Deals with respiratory system-related diseases such as asthma, COPD, and lung infections.
    - Neurology         : Specializes in disorders of the nervous system, including the brain, spinal cord, and peripheral nerves.
    - Oncology          : Dedicated to the diagnosis, treatment, and management of cancer.

    Status:
    - Inpatient : Patients admitted to the hospital for at least one night, often for intensive care or surgical procedures.
    - Outpatient: Patients who receive medical treatment without being admitted to the hospital; they come for consultations, check-ups, or minor procedures.
    """
    print(info_text)

# Main menu
def main_menu():
    while True:
        print("\nHospital Patient Database System")
        print("\n1. Create patient data")
        print("2. Read   patient data")
        print("3. Update patient data")
        print("4. Delete patient data")
        print("5. Search patient data")
        print("6. Payment")
        print("7. Information")
        print("8. Exit")

        choice = input("\nChoose an option: ")
        if choice == '1':
            create_patient()
        elif choice == '2':
            read_patient()
        elif choice == '3':
            update_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            search_patient()
        elif choice == '6':
            calculate_payment()
        elif choice == '7':
            display_info()
        elif choice == '8':
            print("\nExiting program...")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
