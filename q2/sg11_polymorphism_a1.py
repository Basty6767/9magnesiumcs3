class Patient:
    def __init__(self, name: str, bill_amount: float):
        self._name = name
        self._bill_amount = bill_amount
        
    def get_name(self):
        return self._name
    
    def set_name(self, name: str):
        self._name = name
        
    def get_bill_amount(self):
        return self._bill_amount
    
    def set_bill_amount(self, bill_amount: float):
        self._bill_amount = bill_amount
    
    def calculate_bill(self):
        return self._bill_amount
    
    def display_patient_type(self):
        print("Patient type: Regular Patient")
        
class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.8
    
    def display_patient_type(self):
        print("Patient type: Senior Citizen")
    
class PhilhealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85
    
    def display_patient_type(self):
        print("Patient type: Philhealth Member")
        
def display_billing_info(patient: Patient):
    print(f"Patient Name: {patient.get_name()}")
    patient.display_patient_type()
    print(f"Original Bill Amount: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill Amount: ₱{patient.calculate_bill():,.2f}\n")
    

if __name__ == "__main__":
    print("Hospital Billing System")
    print("-----------------------\n")
    
    regular_patient = Patient("Juan Dela Cruz", 15000)
    senior_patient = SeniorPatient("Maria Santos", 20000)
    philhealth_patient = PhilhealthPatient("Pedro Reyes", 18000)
    
    display_billing_info(regular_patient)
    display_billing_info(senior_patient)
    display_billing_info(philhealth_patient)
