"""
Создать класс User с атрибутами:
Свойства:
	- name - имя - содержит только буквы русского алфавита
	- login - логин - может содержать  только латинские буквы цыфры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия:
					содержит менее шести символов
					содержит строчную букву
					содержит заглавную букву
					содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)
Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату.
						Если дата не передана значит на дату проверки.
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего.
						Пароль должен пройти валидацию.
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.
Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
"""

from datetime import date, timedelta
import random
import time
import re


class Users:
    name: str
    login: str
    __password: str
    subscription_date: str
    subscription_mode: str
    is_blocked: bool = False

    CURRENT_Data = date.today()
    q = CURRENT_Data + timedelta(days=30)
    def __init__ (self, name, login, password, subscription_date = q, subscription_mode = "free", is_blocked = False):
       while Users.check_name(name) is False:
           #name = input("Enter the name: ")
           Users.check_name(name)
           self.name = name
           break
       else:
           self.name = name

       while Users.check_login(login) is False:
           #login = input("Enter the login: ")
           Users.check_login(login)
           self.login = login
           break
       else:
           self.login = login

       self.password = password
       self.subscription_date = subscription_date
       self.subscription_mode = subscription_mode


    def get_info(self):
        if self.is_blocked:
            print(f"User {self.name} (login - {self.login}) is bloked! You need ner subscreption\nSubscription date - {self.subscription_date}, Subscription mode - {self.subscription_mode}\n")
        else:
            print(f"Name - {self.name}, login - {self.login}\nSubscription date - {self.subscription_date}, Subscription mode - {self.subscription_mode}\n")


    def block(self):
        self.is_blocked = True

    def unblock(self):
        self.is_blocked = False

    def check_name(name):
        if len(re.findall("[А-яА-Я]", name)) == len(name):
            return True
        else:
            return False

    def check_login(login):
        if len(login)>= 6 and len(re.findall("[a-zA-Z]", login)) == len(login):
            return True
        else:
            return False

    def check_sub(self):
        CURRENT_Data = date.today()
        if self.subscription_date <= val:
            print("End subscrition")
            block()
        else:
            data = elf.subscription_date - CURRENT_Data
            print(f"You have {data.days} days of subscription")


user1 = Users("Витя", "viktor1", "173hfkd")
user1.get_info()

user2 = Users("Максим", "max", "173hfkd")
user2.get_info()


#user1 = Users("iPhone", "13 Pro", 2021)
#user2 = Users(name = "name1", login = "log1", password = "123kdi", subscription_date = "11.04.2020", subscription_mode = "free", is_blocked = False)
#user2.get_info()


""" 
    def receive_call(self, name, tel):
        if self.is_busy:
            print("Number is busy. Call back later")
            return
        self.name = name
        self.tel = tel
        self.call_history.append({"18.04.2022", "15:45", name, tel})
        print(f"{name} is calling, Phone number +{tel}\n")
        self.is_busy = True
        time.sleep(1)
        self.is_busy = False
        return " "


    def view_call_history(self):
        res = ""
        for i in self.call_history:
            res +=(f"{i[0]}, {i[1]},  {i[2]}, {i[3]}\n")

        return res



    def receive_sms(self, name, tel, text):
        self.name = name
        self.tel = tel
        self.text = text
        self.sms_history.append([name, tel, text])
        print(f"{name} (+{tel}) send sms. Text:\n{text}\n\n")
        return " "
"""