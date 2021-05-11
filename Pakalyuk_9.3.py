class Worker:
    def __init__(self, surname, name, patronymic, profession, salary, the_prize):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.profession = profession
        self._earnings = {"Зарплата": salary, "премия": the_prize}


class Specialty(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    def get_full_earnings(self):
        return f"{sum(self._earnings.values())}"


employee_1 = Specialty("Иванов", "Сергей", "Васильевич", "Водитель", 25000, 5000)
employee_2 = Specialty("Смирнов", "Михаил", "Петрович", "Директор", 100000, 35000)
print("ФИО:", employee_1.get_full_name(), '\n' "Должность:", employee_1.profession, '\n' "Сумарный доход:", employee_1.get_full_earnings())
print("ФИО:", employee_2.get_full_name(), '\n' "Должность:", employee_2.profession, '\n' "Сумарный доход:", employee_2.get_full_earnings())