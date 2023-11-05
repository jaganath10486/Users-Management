import firebase_admin
from firebase_admin import firestore
from datetime import datetime

class UserManagement():
    def __init__(self):
        try:
            firebase_admin.get_app()
        except ValueError:
            print("Firebase admin is not initiallized")

        self._db = firestore.client()
        self._collection = self._db.collection('users_profile')

    def register(self, data, uid):
        try:
            user_profile_ref = self._collection.document(uid)
            user_profile_ref.set({
                'email' : data['email'],
                'username' : data['username'],
                'full_name' : data['full_name'],
                'created_at' : datetime.now() ,
            })
            print("User Stored Successfully")
        except Exception as E:
            print("Failed to Store the data")