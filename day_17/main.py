class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User('001', 'angela')
user2 = User('002', 'jack')
user1.follow(user2)

users = [user1, user2]

for user in users:
    print(f'id - {user.id}, name - {user.username}, followers - {user.followers}')
