from flask import Flask, jsonify, request
app=Flask(__name__)
contacts=[
    {
        'id':1,
        'Contact':9823223423,
        'Name':"Raju"
    }
]

@app.route("/add",methods=["POST"])

def add():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data"
        },400
        )
    contact={
        "id":contacts[-1]['id']+1,
        "Contact":request.json['Contact'],
        "Name":request.json['Name']
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added successfully"
    })

@app.route("/get")

def getTask():
    return jsonify({
        "data":contacts
        })

if __name__=="__main__":
    app.run()