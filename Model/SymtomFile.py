from Model.Medicine import Medicine


class Symptom:
    ListOfMedicine = {}
    def setName(self,name):
        self.Name = name
    def setDescription(self,description):
        self.Description = description
    def setMedicalTerm(self,medicalTerm):
        self.MedicalTerm = medicalTerm

    def setListOfMedicine(self,medicine):
        self.ListOfMedicine[medicine.MedicineName]=medicine;


sym = Symptom()
m = Medicine()
m.setName("Napa")
sym.setListOfMedicine(m)
m1 = Medicine()
m1.setName("Paracitamol")
sym.setListOfMedicine(m1)
print({ name:obj.MedicineName for name,obj in sym.ListOfMedicine.items()})