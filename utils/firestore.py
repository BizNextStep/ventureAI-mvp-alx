from google.cloud import firestore

   def add_business_idea(idea):
       db = firestore.Client()
       doc_ref = db.collection('business_ideas').add(idea)
       print(f"Added idea with ID: {doc_ref.id}")
