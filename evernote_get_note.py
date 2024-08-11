

dev_token = "put your dev token here"
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username