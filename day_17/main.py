class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user1 = User('001', 'angela')
user2 = User('002', 'jack')

users = [user1, user2]

for user in users:
    print(f'id - {user.id}, name - {user.username}')
