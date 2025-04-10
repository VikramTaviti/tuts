class BaseModel:
    def save(self, data):
        print(f"Writing to DB: {data}")

class UserInfo(BaseModel):
    def save(self, data):
        data['user'] = {'name': 'Vikram', 'email': 'vikram@gmail.com'}
        super().save(data)   # it wont call BaseModel.....

class Audit(BaseModel):
    def save(self, data):
        data['audit'] = {'ip': '192.168.0.1', 'timestamp': '2025-04-08'}
        super().save(data)

class Security(BaseModel):
    def save(self, data):
        data['token'] = 'security_token...'
        super().save(data)

class User(UserInfo, Audit, Security):
    def save(self):
        data = {}
        super().save(data)  # starts the MRO chain

user = User()
user.save()


print(User.__mro__)

