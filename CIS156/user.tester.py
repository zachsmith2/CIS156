# Zachary Smith
# PA_9
class User:
    # constructor
    def __init__(self, firstName, lastName, userId, password):
        self._firstName = firstName
        self._lastName = lastName
        self._userId = userId
        self._password = password

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, firstName):
        self._firstName = firstName

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName

    @property
    def userId(self):
        return self._userId

    @userId.setter
    def name(self, userId):
        self._userId = userId

    @property
    def password(self):
        return self._password

    @password.setter
    def name(self, password):
        self._password = password


def main():
    # asking the user for inputs
    print('User Input:')
    firstName = input('Enter the first name: ')
    lastName = input('Enter the last name: ')
    userId = input('Enter the userID: ')
    password = input('Enter password: ')

    # instantiating user class
    user = User(firstName, lastName, userId, password)
    # printing the output
    print('\nUser information:')
    print('First name:', user.firstName)
    print('Last name:', user.lastName)
    print('UserId:', user.userId)
    print('Password:', user.password)


# calling the main method
main()
