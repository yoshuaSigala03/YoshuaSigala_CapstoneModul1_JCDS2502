# Hospital Patient Database System

## Overview

The **Hospital Patient Database System** is a Python-based application designed to manage patient data efficiently. This system supports CRUD (Create, Read, Update, Delete) operations, patient searches, payment calculations, and provides essential information about hospital departments, diseases, and patient statuses. The application uses the `tabulate` library to present data in a readable tabular format.

---

## Features

### **1. Create Patient Data**
- Add new patients to the database.
- Ensures no duplicate `Patient ID` is created.
- Provides options to input patient details like name, age, gender, diagnosis, disease type, severity, department, and status.

### **2. Read Patient Data**
- View all patient records in a tabular format.
- Retrieve specific patient data by their unique `Patient ID`.

### **3. Update Patient Data**
- Update details of an existing patient.
- Allows editing only the required fields while keeping the rest unchanged.

### **4. Delete Patient Data**
- Remove a patient's data from the database using their `Patient ID`.
- Includes confirmation prompts before deletion.

### **5. Search Patient Data**
- Search for patients by specific fields, such as `Patient ID`, `Name`, `Age`, `Gender`, `Diagnosis`, `Disease Type`, `Severity`, `Department`, or `Status`.

### **6. Calculate Payment**
- Automatically calculates the total payment due for a patient based on:
  - Disease type (`Infectious` or `Non-Infectious`).
  - Disease severity (`Acute`, `Chronic`, or `Progressive`).
  - Hospital department (`General Medicine`, `Cardiology`, `Pulmonology`, `Neurology`, `Oncology`).
  - Patient status (`Inpatient` or `Outpatient`).
- Displays a detailed breakdown of the costs.
- Supports payment processing and returns change if applicable.

### **7. Display Information**
- Provides detailed explanations of fields, disease types, severity levels, hospital departments, and patient statuses.

### **8. Exit**
- Safely exit the application.

---

## Prerequisites

- Python 3.6 or later.
- The `tabulate` library for tabular data representation.

### Install `tabulate`:
Run the following command in your terminal:
```bash
pip install tabulate
```
### How to Run
Clone or download the project files.
Run the main.py file in your Python environment:
```bash
python main.py
```


### Patient Fields:

Patient ID  :  Unique identifier for each patient.

Name  :  Full name of the patient.

Age  :  Age of the patient in years.

Gender  :  Gender of the patient (Male/Female).

Diagnosis  :  Medical condition or disease.

Disease Type  :  Either Infectious or Non-Infectious.

Severity  :  Can be Acute, Chronic, or Progressive.

Department  :  Hospital department handling the patient (General Medicine, Cardiology, Pulmonology, Neurology, Oncology).

Status  :  Patient's hospital status (Inpatient or Outpatient).


### Example Usage:
- Main Menu
Hospital Patient Database System

1. Create patient data
2. View   patient data
3. Update patient data
4. Delete patient data
5. Search patient data
6. Payment
7. Information
8. Exit

- Tabulated Data Output
When viewing patient data:

| Patient ID | Name             | Age | Gender | Diagnosis     | Disease Type   | Severity    | Department         | Status      |
|------------|------------------|-----|--------|---------------|----------------|-------------|--------------------|-------------|
| 001        | Patricia Taylor  | 29  | Male   | Hypertension  | Non-Infectious | Progressive | Cardiology         | Outpatient  |
| 002        | Mary Hernandez   | 48  | Female | Hepatitis     | Non-Infectious | Chronic     | Cardiology         | Outpatient  |

---

### License
This project is licensed under the MIT License.
