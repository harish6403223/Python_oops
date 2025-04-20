
class Vehicle():
    def __init__(self, drive_obj):
        self.drive_obj = drive_obj
    
    def drive(self):
        self.drive_obj.drive()