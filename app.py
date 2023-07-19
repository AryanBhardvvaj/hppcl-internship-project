from flask import Flask, request, render_template ,redirect, url_for
from flask_cors import cross_origin
import pickle
import pandas as pd

app = Flask(__name__)
model = None  # Placeholder for the model

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/home", methods=["POST"])
def home():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "admin":
        return render_template("home.html")
    else:
        return redirect(url_for("login"))
    


@app.route("/predict", methods=["POST"])
@cross_origin()
def predict():
    global model  # Use the global model variable

    selected_file = request.form['file']
    if selected_file == 'kashang':
        model = pickle.load(open("codegenfiles/kashang.pkl", "rb"))
    elif selected_file == 'sk':
        model = pickle.load(open("codegenfiles/sk1.pkl", "rb"))
    elif selected_file == 'sainj':
        model = pickle.load(open("codegenfiles/sainj.pkl", "rb"))

    import pandas as pd
    from datetime import datetime, timedelta

    from datetime import timedelta

    data2 = pd.read_csv('codegenfiles/completeddata.csv')
    data2['DATE'] = pd.to_datetime(data2['DATE'])  
    # Convert 'DATE' column to datetime format

    #----------------------- user entered date -----------------------
    # user_date_entered = input("Enter a date (YYYY-MM-DD): ")
    user_date_entered = request.form['DATE']
    user_date_prev_year = pd.to_datetime(user_date_entered) - pd.DateOffset(years=2)

    #----------------------- past and future dates -----------------------

    past_start_date = user_date_prev_year - timedelta(days=4)
    past_end_date = user_date_prev_year - timedelta(days=1)
    future_start_date = user_date_prev_year + timedelta(days=1)
    future_end_date = user_date_prev_year + timedelta(days=4)

    past_data = data2[(data2['DATE'] >= past_start_date) & (data2['DATE'] <= past_end_date)]
    future_data = data2[(data2['DATE'] >= future_start_date) & (data2['DATE'] <= future_end_date)]

    columns = ['Scheduled Generation', 'Gross Gen.', 'Net Variation', 'Total Energy Export',
               'Total Energy Import', 'Aux. Consumption and losses', 'Aux. Consumption and losses percentage',
               'Load max.', 'Load min.', 'Load avg.','Commulative Gross Gen.', 'Discharge max.',
               'Discharge min.', 'Discharge avg.', 'Reserv lvl(M) max.', 'Reserv lvl(M) min.',
               'Reserv lvl(M) avg.', 'Reserv lvl(E) max.', 'Reserv lvl(E) min.', 'Reserv lvl(E) avg.']
    avgdata = []
    
    for column in columns:
        past_sum = past_data[column].sum()
        future_sum = future_data[column].sum()
        avg = ((past_sum + future_sum))
        avg_rounded = round(avg, 2)  # Round to 2 decimal places
        avgdata.append(avg_rounded)

    Scheduled_Generation = avgdata[0]
    Gross_Gen = avgdata[1]
    Net_Variation = avgdata[2]
    Total_Energy_Export = avgdata[3]
    Total_Energy_Import = avgdata[4]
    Aux_Consumption_and_losses = avgdata[5]
    Aux_Consumption_and_losses_percentage = avgdata[6]
    Load_max = avgdata[7]
    Load_min = avgdata[8]
    Load_avg = avgdata[9]
    Discharge_max = avgdata[10]
    Discharge_min = avgdata[11]
    Discharge_avg = avgdata[12]
    Reserv_lvl_M_max = avgdata[13]
    Reserv_lvl_M_min = avgdata[14]
    Reserv_lvl_M_avg = avgdata[15]
    Reserv_lvl_E_max = avgdata[16]
    Reserv_lvl_E_min = avgdata[17]
    Reserv_lvl_E_avg = avgdata[18]
        
    prediction = model.predict([[
        Scheduled_Generation, 
        Gross_Gen,
        Net_Variation, 
        Total_Energy_Export,
        Total_Energy_Import,
        Aux_Consumption_and_losses,
        Aux_Consumption_and_losses_percentage,
        Load_max,
        Load_min,
        Load_avg,
        Discharge_max,
        Discharge_min,
        Discharge_avg,
        Reserv_lvl_M_max,
        Reserv_lvl_M_min,
        Reserv_lvl_M_avg,
        Reserv_lvl_E_max,
        Reserv_lvl_E_min,
        Reserv_lvl_E_avg
    ]])
    
    year, month, day = user_date_entered.split("-")
    
    output1 = round(prediction[0], 2)
    
    output = float(output1)
    
    if month in ['12', '1', '2', '3']:
        output = output * 0.4
    elif month in ['4', '5', '6']:
        output = output* 0.5
    elif month in ['7', '8', '9']:
        output = output * 0.5
    elif month in ['10', '11']:
        output = output * 0.3
    else:
        output
    

    sales = output * 3.5

    if selected_file == 'kashang':
        return render_template('kashang.html', prediction_text="{}".format(output), revenue="\n{}".format(sales), date="\n{}".format(user_date_entered))
    elif selected_file == 'sk':
        return render_template('sk.html', prediction_text="{}".format(output), revenue="\n{}".format(sales), date="\n{}".format(user_date_entered))
    elif selected_file == 'sainj':
        return render_template('sainj.html', prediction_text="{}".format(output), revenue="\n{}".format(sales), date="\n{}".format(user_date_entered))
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000 ,debug=True)