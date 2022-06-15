import pyrebase

config = {
  "apiKey": "AIzaSyDzkQnoQFy0BoiiMIF-mKn-r8A33qpwP9c",
  "authDomain": "beterword.firebaseapp.com",
  "databaseURL": "https://beterword-default-rtdb.firebaseio.com",
  "storageBucket": "beterword.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

joe = db.child('week8scores').get().val()
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
        db.child('week8scores').child(email).update({"pending":"false"})
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
        prev = db.child('week8scores').child(email).child("answerArr").child(i).get().val()
        prev = prev.replace('false','true')
        db.child('week8scores').child(email).child("answerArr").update({i:prev})

    c = c/newnum

    db.child('week8scores').child(email).update({"score":newscore})
    db.child('week8scores').child(email).update({"celerity":c})
    db.child('week8scores').child(email).update({"numcorrect":newnum})
    db.child('week8scores').child(email).update({"pending":"false"})
    print('\n\n\n')