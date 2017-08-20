from Model.Medicine import Medicine
#from Model.Symptom import Symptom
from Model.SymtomFile import Symptom

class Prescription:
    PrescrivedMedicine = {}
    def checkMedicine(self,medicine):
        if medicine in self.Symptom1.ListOfMedicine:
            self.Symptom1.ListOfMedicine.get(medicine).IncrementReferenceCounter()
            self.PrescrivedMedicine[medicine] = self.Symptom1.ListOfMedicine.get(medicine)
            print("Found")
        else:
            Newmedicine = Medicine()
            Newmedicine.setName(medicine)
            self.Symptom1.ListOfMedicine[medicine] = Newmedicine
            self.PrescrivedMedicine[medicine] = Newmedicine
            Newmedicine.IncrementReferenceCounter()
            print("Not found")

    def setDoctor(self,doctor):
        self.Doctor = doctor
    def setSymptom(self,symptom):
        self.Symptom1 = symptom

m = Medicine()
p = Prescription()
Sym = Symptom()
#Sym.setListOfMedicine(m)
p.setSymptom(Sym)
p.checkMedicine("Napa")
p.checkMedicine("Maxpro")
p.checkMedicine("Maxpro")
print({ name:obj.referenceCounter for name,obj in Prescription.PrescrivedMedicine.items()})