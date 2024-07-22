from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def process_query(query):
    query = query.lower()
    response = ""
    if 'seats' in query:
        response = "CSE = 120 \n ECE=120"
    elif 'principal' in query:
        response = "Dr. U.Shinde"
    elif 'hello' in query:
        response = "hello this is vishals chatbot i welcome you at the csmss collage of engeneering"
    elif 'cse hod'  in query:
        response = "XYZ"    
    elif 'ece hod' in query:
        response = "Dr.D.Bhuyar" 
    elif 'civil hod' in query:
        response = "Dr.sohel" 
    elif 'makrand' in query:
        response = "aids student first year"
    elif '' in query:
        response = "" 
    elif 'AIML  ' in query:
        response = "PRITI MADAM"
    elif 'ece department' in query:
        response = "best departmnet in the college"
    elif 'ece staff' in query:
        response = "dr.ali prof.j.n.mohite prof. A.T. jadhav "
    elif 'mechanical hod' in query:
        response = "Dr. U.Tonde" 
    elif 'created' in query:
        response='VISHAL SURESH RATHOD'
    elif 'elecrtical hod' in query:
        response = "Dr. B.Kumar" 
    elif 'how many course' in query:
        response = "8"
    elif 'which course ' in query:
        response = " CSE, ECE, Mechanical, Civil,5G, CSE(Data Science) VLSI , Elecrtical   "
    elif ' course ' in query:
        response = " CSE, ECE, Mechanical, Civil,5G, CSE(Data Science) VLSI , Elecrtical  "
    elif 'highest package' in query:
        response = "12 LPA"
    elif 'minimum package' in query:
        response = "000 LPA"
    elif 'bus incharge' in query:
        response = "Prof T.D.Kanwate"
    elif 'hostel incharge' in query:
        response = "Prof G.H.Lihinar"
    elif 'librarian' in query:
        response = "Dr. S.Pratapure"
    elif 'dean' in query:
        response = "Joy Danial"
    elif 'sport incharge' in query:
        response = "Prof M.Hanumante"
    elif 'fees structure' in query:
        response = "Category"
    elif 'placement percentage' in query:
        response = "70%"
    elif 'establishment year' in query:
        response = "year 2008"
    elif 'hostel seats' in query:
        response = "Boys Hostel 700 \n Girls Hostel 700"
    elif 'company visited in recent year' in query:
        response = "7 Company Visit"
    elif 'admission incharge' in query:
        response = "huuhu"
    elif 'university details' in query:
        response = "Dr. Babasaheb Ambedakar Technological University Lonere"
    elif 'how are you' in query:
        response="I am fine what about you"
    elif 'GOKUL' in query:
        response="aroga food worker that is oil company"
    elif 'fine' in query:
        response='that`s grest'
    elif 'vaishnavi gedam' in query:
        response='snap id=vaishu932265 number =9322659005'
    elif 'open code' in query:
        
        codePath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

        os.startfile(codePath)
        response = "Opening VS Code"
    else:
        response = "No query matched"
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    message = data.get("message")
    response = process_query(message)
    return jsonify({"content": response})

if __name__ == "__main__":
    app.run(debug=True)