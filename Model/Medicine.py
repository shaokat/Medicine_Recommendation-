class Medicine:
    type = ['tablet', 'capsule', 'inspection']
    referenceCounter=0
    def setName(self,name):
        self.MedicineName = name;
        #print(self.MedicineName)
    def setDosageAmount(self,amount):
        self.dosageAmount = amount
    def MedicalName(self,medicalName):
        self.MedicaleName = medicalName;
    def IncrementReferenceCounter(self):
        self.referenceCounter+=1;

m = Medicine()
m.setName("Maxpro")
#print(m.MedicineName)