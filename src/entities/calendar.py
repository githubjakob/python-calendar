from src.entities.appointment import Appointment


class Calendar:
    def __init__(self):
        self.appointments: list = []
        pass

    def add_appointment(self, appointment: Appointment):
        self.appointments.append(appointment)
