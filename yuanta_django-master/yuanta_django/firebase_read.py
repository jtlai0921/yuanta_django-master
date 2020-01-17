from firebase import firebase
# https://ozgur.github.io/python-firebase/

firebase = firebase.FirebaseApplication('https://tuanweihan.firebaseio.com/', None)
result = firebase.get('/hello', 'n')
print(result)