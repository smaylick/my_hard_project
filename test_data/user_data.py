from models.login_model import LoginData

VALID_CREDENTIALS = LoginData(
    login='taullessafunnoi-4696@yopmail.com',
    password='verynicepassword'
)

INVALID_CREDENTIALS = LoginData(
    login='taullessafunnoi-4696@yopmail.com',
    password='fakepassword'
)
