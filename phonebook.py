
class Contact(object):

    def __init__(self, first_name, surname, phone_number, favorite_contact=False, *args, **kwargs):
        self.first_name = first_name
        self.surname = surname
        self.phone_number = phone_number
        self.favorite_contact = favorite_contact

        self.args_additional_list = []
        for param in args:
            self.args_additional_list.append(param)

        self.kwargs_additional_dict = {}
        for item_name, item_value in kwargs.items():
            self.kwargs_additional_dict[item_name] = item_value

    def __str__(self):
        if self.favorite_contact:
            my_favorite_contact = 'да'
        else:
            my_favorite_contact = 'нет'
        
        return str(
            "Имя: " + self.first_name + "\n" +
            "Фамилия: " + self.surname + "\n" +
            "Телефон: " + self.phone_number + "\n" + 
            "В избанных: " + my_favorite_contact + "\n" + 
            "Дополнительная информация: " + "\n" + 
            "\t" + '\n\t'.join(self.args_additional_list) + "\n" + 
            "\t" + '\n\t'.join('{}: {}'.format(item_name, item_value) for item_name, item_value
                               in sorted(self.kwargs_additional_dict.items()))
        )


class PhoneBook:

    def __init__(self, phonebook_name):
        self.phonebook_name = phonebook_name

    def get_contacts(phonebook):
        contacts = []
        for contact in phonebook:
            contacts.append(contact)

        return contacts

    def create_contact(contact, phonebook):
        phonebook = phonebook.append(contact)

        return phonebook

    def delete_contact_by_number(phone_number, phonebook):
        if contact.__dict__['phone_number'] == phone_number:
            phonebook.remove(contact)

        return phonebook

    def get_favorite_contacts(phonebook):
        favorite_contacts = []
        for contact in phonebook:
            if contact.__dict__['favorite_contact']:
                favorite_contacts.append(contact)

        return favorite_contacts

    def get_contact_by_name(phonebook, first_name, surname):
        found_contacts = []
        for contact in phonebook:
            if contact.__dict__['first_name'] == first_name and (contact.__dict__)['surname'] == surname:
                found_contacts.append(contact)

        return found_contacts

mike = Contact('Mike', 'Modano', '+73333333333', True, 'Moscow, Tverskaya, 1',
               '+79000000000', 'worker', telegram='@modano', email='mike_mod@ya.ru')

kate = Contact('Kate', 'Ivanova', '+74444444444', False, 'Moscow, Tverskaya, 2',
                   '+79555555555', 'doctor', telegram='@doc_kat', email='ikate@mail.ru')

alex = Contact('Alex', 'Petrov', '+71111111111', False, 'Orel, Lenina, 3',
               '+77777777777', 'judge', telegram='@alex', email='alex@mail.com')

test_phonebook = []
PhoneBook.create_contact(mike, test_phonebook)
PhoneBook.create_contact(kate, test_phonebook)
PhoneBook.create_contact(alex, test_phonebook)

print('\n' +'Список всех контактов:')
contacts = PhoneBook.get_contacts(test_phonebook)
for contact in contacts:
    print(contact)
    print('-' * 15)

print('\n' +'Список контактов после удаления по номеру телефона:')
for contact in contacts:
    PhoneBook.delete_contact_by_number('+74444444444', test_phonebook)

contacts = PhoneBook.get_contacts(test_phonebook)
for contact in contacts:
    print(contact)
    print('-' * 15)

print('\n' + 'Избранные контакты:')
favorite_contacts = PhoneBook.get_favorite_contacts(test_phonebook)
for contact in favorite_contacts:
    print(contact)
    print('-' * 15)

print('\n' + 'Найденный по имени и фамилии контакт:')
found_contacts = PhoneBook.get_contact_by_name(test_phonebook, 'Alex', 'Petrov')
for contact in found_contacts:
    print(contact)