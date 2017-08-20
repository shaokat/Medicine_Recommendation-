from Model.Doctor import Doctor
class Reference:

    def setDoctor(self,doctor):
        self.Doctor = doctor
        print(self.Doctor.DoctorName)
    def setDate(self):
        pass
    def Counter(self):
        pass
r = Reference()
d=Doctor()
d.setDoctorName('Abdullah')
r.setDoctor(d)