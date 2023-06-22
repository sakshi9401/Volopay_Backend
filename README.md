# Volopay_Backend_Assignment
For building this API's I have used Python language and Flask framework.

## Installation

Install flask in VScode using command
```bash
 pip install flask
```

Install Postman API platform for testing API

Step 1) Download Postman

    https://www.postman.com/downloads/

Step 2)  Postman Installation Start

## Import

import Flask, request and jsonify from flask

    from flask import Flask, request, jsonify

import csv library

    import csv

## Running Tests

To run the API, run the following command

```bash
  python api.py
```

## Default Port
```bash
  http://127.0.0.1:5000/
```

## Explanation



    
## API 1

#### Total item (total seats) sold in Marketting for last in q3 of the year?

```
  http/api/total_items
```

| Parameter | Type                |
| :-------- | :------- | 
| `start_date:` | `Date` | 
| `end_date:` | `Date` | 
| `department` | `string` | 

### Conclusion

This API defines a Flask route that calculates and returns the total number of items sold in the "Marketting" category during the last quarter (Quarter3) of a given year.

## API 2
#### 1) What is the 2nd most sold item in terms of quantity sold in q4
#### 2) What is the fourth most sold item in terms of Total price in q2?

```
http/api/nth_most_total_item
  
```

| Parameter | Type |  
 :-------- | :------- | 
| ` item_by:`      | `string` | 
| `start_date:` | `Date` | 
| `end_date:` | `Date` | 
| ` n:`      | `Integer` | 

### Conclusion

This API is a Flask route that calculates and returns information about the second most sold item in terms of quantity sold in Quarter 4 and the fourth most sold item in terms of total price in Quarter 2
     


## API 3
#### What is the percentage of sold items (seats) department wise?

```
http/api/percentage_of_department_wise_sold_items
  
```

| Parameter | Type     | 
| :-------- | :------- | 
| `start_date:`  | `Date` | 
| `end_date:`     | `Date` | 

### Conclusion

This API reads data from a CSV file, calculates the percentage of sold items for each department, and returns the result as a JSON response through a Flask route.

## API 4
#### How does the monthly sales for any product look like?

```
http/api/monthly_sales
  
```

| Parameter | Type     | 
| :-------- | :------- |
| `product: `      | `string` |
| `year: `      | `Number` |

### Conclusion
This API reads data from a CSV file, extracts and processes the relevant information to calculate monthly sales for a specific product, and returns the results in a structured format.







