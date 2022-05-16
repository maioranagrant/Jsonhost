import pyrebase

config = {
  "apiKey": "AIzaSyDzkQnoQFy0BoiiMIF-mKn-r8A33qpwP9c",
  "authDomain": "beterword.firebaseapp.com",
  "databaseURL": "https://beterword-default-rtdb.firebaseio.com",
  "storageBucket": "beterword.appspot.com"
}

# config = {
#   "apiKey": "AIzaSyDvHFTrNNFBDi7V0NUDMhmLB_1px6nXt20",
#   "authDomain": "beterwordtest.firebaseapp.com",
#   "databaseURL": "https://beterwordtest-default-rtdb.firebaseio.com",
#   "storageBucket": "beterwordtest.appspot.com"
# }

firebase = pyrebase.initialize_app(config)
db = firebase.database()

brk = False
while not brk:

    email = input("Enter user email\t")
    if email == 'x':
        break
    email = email.replace(".","__dot__")

    #(db.child('week3scores').get().val()[email])
    user = db.child('week4scores').get().val()[email]

    answers = user["answerArr"]
    ct = 0
    for j in answers:
        j = j.replace("false","#####")
        j = j.replace("true","")
        print(str(ct) + " " + j)
        ct+=1

    questions = input("Enter question numbers to fix\t")
    if questions == 'x':
        db.child('week4scores').child(email).update({"pending":"false"})
        continue
    questions = questions.split(",")

    oldcel = user["celerity"]
    oldnum = user["numcorrect"]
    oldscore = user["score"]

    celarr = user["celerArr"]
    ptsarr = user["scoreArr"]

    newnum = oldnum
    newscore = oldscore
    c = oldcel * oldnum
    for i in questions:
        c += celarr[int(i)]
        newnum += 1
        newscore += ptsarr[int(i)]

    c = c/newnum

    db.child('week4scores').child(email).update({"score":newscore})
    db.child('week4scores').child(email).update({"celerity":c})
    db.child('week4scores').child(email).update({"numcorrect":newnum})
    db.child('week4scores').child(email).update({"pending":"false"})
    print('\n\n\n')