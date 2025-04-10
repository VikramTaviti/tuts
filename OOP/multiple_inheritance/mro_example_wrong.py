#Im not using super()....

class BaseModel:
    def save(self, data):
        print(f"writing to DB: {data}")

class UserInfo(BaseModel):
    def save(self, data):
        data['user'] = {'name': 'Vikram', 'email': 'vikram@gmail.com'}
        BaseModel.save(self, data)  #  Hardcoded

class Audit(BaseModel):
    def save(self, data):
        data['audit'] = {'ip': '192.168.0.1', 'timestamp': '2025-04-08'}
        BaseModel.save(self, data)  #  Hardcoded

class Security(BaseModel):
    def save(self, data):
        data['token'] = 'security_token...'
        BaseModel.save(self, data)  #  Hardcoded

class User(UserInfo, Audit, Security):
    def save(self):
        data = {}
        UserInfo.save(self, data)
        Audit.save(self, data)
        Security.save(self, data)

user = User()
user.save()

