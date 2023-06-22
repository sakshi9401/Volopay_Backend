from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)
with open("data.csv", "r") as f:
        reader = csv.reader(f)
        data = list(reader)


#API 1
@app.route("/api/total_items")
def get_total_items():
    count = 0
    for row in data:
        if row[1][5:7] in ['07','08','09']:
            if row[3]=="Marketting":
                count+=int(row[5])
    return ({"Total item sold in Marketting for last in Quarter3 of the year": count})

#API 2
@app.route("/api/nth_most_total_item")
def get_nth_most_total_item():
    software_map1 = {}
    software_map2= {}
    for row in data:
            if row[0] != 'id':
                row1 = row[1][0:4]
                row2 = row[4]
                if row1=="2022":
                    if row[1][5:7] in ['10','11','12']:
                        if row[4] in software_map1.keys():
                            software_map1[row1]=software_map1.get(row2)+1
                        else:
                            software_map1[row2]=1
    s_map1 = sorted(software_map1.items(),key=lambda x:x[1])
    software1 = list(s_map1)[-2]
    print(software1)
    for row in data:
            if row[0] != 'id':
                row1 = row[1][0:4]
                row2 = row[4]
                if row1=="2022":
                    if row[1][5:7] in ['04','05','06']: 
                         cost = row[6]
                         if row[4] in software_map2.keys():
                             software_map2[row2]=float(software_map2.get(row2))+ float(cost)
                         else:
                            software_map2[row2]=float(cost)
    s_map2 = sorted(software_map2.items(),key=lambda x:x[1])
    #print(s_map2)
    software2 = list(s_map2)[-4]
    #print(software2)
    return ({"The 2nd most sold item in terms of quantity sold in Quarter4": software1[0], 
             "The 4th most sold item in terms of Total price in Quarter2": software2[0]})

#API 3
results = []

with open("data.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        results.append(row)

@app.route("/api/percentage_of_department_wise_sold_items")
def get_percentage_of_department_wise_sold_items():
    department_map = {}
    total_count = 0

    for result in results:
        department = result["department"]
        seats = int(result["seats"])

        department_map[department] = department_map.get(department, 0) + seats
        total_count += seats

    for department, count in department_map.items():
        percentage = (count / total_count) * 100
        department_map[department] = f"{percentage:.2f}%"

    return jsonify(department_map)

#API4
@app.route("/api/monthly_sales")
def monthly_sales():
    results = []

    with open("data.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            results.append(row)

    prod_name = results[0]["software"]
    prod_date = results[0]["date"][:11].split("-")[0]
    monthly_map = {}
    monthly_sales_map = []

    for result in results:
        name = result["software"]
        date = result["date"][:11].split("-")

        if prod_date == date[0] and prod_name == name:
            monthly_map[date[1]] = monthly_map.get(date[1], 0) + int(result["seats"]) * float(result["amount"])

    for key in sorted(monthly_map.keys()):
        monthly_sales_map.append(monthly_map[key])

    return ({
        "software": prod_name,
        "product_year": prod_date,
        "sales": monthly_sales_map
    })
#home
@app.route('/', methods=['GET'])
def home():
    return "<h1>VOLOPAY Assignment</h1>"

if __name__ == "__main__":
    app.run(debug=True)
    # get_total_items()
    # get_nth_most_total_item()
    # get_percentage_of_department_wise_sold_items()