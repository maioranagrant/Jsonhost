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

# brk = False
# while not brk:

#     email = input("Enter user email\t")
#     if email == 'x':
#         break
#     email = email.replace(".","__dot__")

#     #(db.child('week3scores').get().val()[email])
#     try:
#         user = db.child('week5scores').get().val()[email]
#     except:
#         print("not found\n\n\n")
#         continue
#     if user["pending"] == 'false':
#         print("been done\n\n\n")
#         continue
#     answers = user["answerArr"]
#     ct = 0
#     for j in answers:
#         j = j.replace("false","\t\t\t#####")
#         if "true" in j:
#             ct+=1
#             continue
#         j = j.replace("true","")
#         print(str(ct) + " " + j)
#         ct+=1

#     questions = input("Enter question numbers to fix\t")
#     if questions == 'x':
#         db.child('week5scores').child(email).update({"pending":"false"})
#         print('\n\n\n')
#         continue
#     questions = questions.split(",")

#     oldcel = user["celerity"]
#     oldnum = user["numcorrect"]
#     oldscore = user["score"]

#     celarr = user["celerArr"]
#     ptsarr = user["scoreArr"]

#     newnum = oldnum
#     newscore = oldscore
#     c = oldcel * oldnum
#     for i in questions:
#         c += celarr[int(i)]
#         newnum += 1
#         newscore += ptsarr[int(i)]

#     c = c/newnum

#     db.child('week5scores').child(email).update({"score":newscore})
#     db.child('week5scores').child(email).update({"celerity":c})
#     db.child('week5scores').child(email).update({"numcorrect":newnum})
#     db.child('week5scores').child(email).update({"pending":"false"})
#     print('\n\n\n')
joe = db.child('week5scores').get().val()
for i in joe:
    user = joe[i]
    if user["firstName"] == 'placeholder':
        continue
    if user["pending"] == 'false':
        continue
    
    print(user["firstName"] + user["lastname"])
    answers = user["answerArr"]
    ct = 0
    for j in answers:
        j = j.replace("false","\t\t\t#####")
        if "true" in j:
            ct+=1
            continue
        j = j.replace("true","")
        print(str(ct) + " " + j)
        ct+=1
    email = user["username"]
    questions = input("Enter question numbers to fix\t")
    if questions == 'x':
        db.child('week5scores').child(email).update({"pending":"false"})
        print('\n\n\n')
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

    db.child('week5scores').child(email).update({"score":newscore})
    db.child('week5scores').child(email).update({"celerity":c})
    db.child('week5scores').child(email).update({"numcorrect":newnum})
    db.child('week5scores').child(email).update({"pending":"false"})
    print('\n\n\n')