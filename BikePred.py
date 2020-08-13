global bike_model

try:
    import os
    import config
    import pickle as pikl
    import pandas as pd
    from flask import Flask, render_template, request
    from flask import Response
    from flask import send_file
    from flask_cors import CORS, cross_origin
    from pandas.io.json import json_normalize
    # import flask_monitoringdashboard as dashboard
    from form_data.user_input import user_input
    from loadModel import loadModel

except ImportError as ie:
    print('Error ', ie)
finally:
    os.putenv('LANG', 'en_US.UTF-8')
    os.putenv('LC_ALL', 'en_US.UTF-8')

# Create App
app = Flask(__name__)
# dashboard.bind(app)

CORS(app)

# Run or refresh model
def model():
    print('Model called')
    # Loading model file
    bike_model = pikl.load(
        open(r'model\bike_share_rf_model.P', 'rb'))
    # Returning model file
    return bike_model


# Predict from the model build
@app.route('/predict', methods=['POST', 'GET'])
@cross_origin()
def predict():
    print('Some one called me')
    try:
        if request.form is not None:
            print('From if')
            input_values = request.form
            print('User Form Input Values are as follows: ',input_values)
            # inputX = pd.DataFrame(json_normalize(input_values))
            # print('Data Type of user input is : ', type(inputX))

            # Object Initialization
            user_ip = user_input(input_values)

            if user_ip.df.empty:
                return render_template('home.html')
            else:

                print(80 * '*')
                print('Post user_ip is created', user_ip.df)
                print(80 * '*')

                # print(user_input)
                print('Values from user are as below')
                # print(inputX)
                # input = inputX[
                #     ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'windspeed',
                #     'qtrs']]
                inpv = user_ip.get_user_input(user_ip.df)
                print('Printing received values')
                print(inpv)

                bike_model = loadModel()

                # predval = bike_model.predict(input)
                print('Bike Model Instantiated', bike_model)

                predval = bike_model.predictionFromModel(inpv)

                print('Pred val is ', predval)

                inpv['predval'] = int(predval)
                print('Int pred value is ',inpv["predval"])

                inpv.columns = ['Season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp',
                             'windspeed', 'qtrs', 'Predcited Result']
                return render_template('predict.html', tables=[inpv.to_html()], titles=inpv.columns.values)
        else:
            return render_template('home.html')
    except ValueError:
        return Response("Error Occurred! %s" %ValueError)
    except KeyError:
        return Response("Error Occurred! %s" %KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" %e)



# Home page that renders for every web call
@app.route("/")
@cross_origin()
def home():
    print('Starting from here')
    # Highlight default landing page
    return render_template("home.html")

# About page that renders for every web call
@app.route("/About")
@cross_origin()
def about():
    print('Going to About Page')
    # Highlight default landing page
    return render_template("About.html")

# EDA Page renders detailed analysis about BikeShare Project
@app.route("/EDA")
@cross_origin()
def eda():
    print('Going to EDA Page')
    return render_template("eda.html")


@app.route('/bike_share_eda.html')
def show_map():
    return send_file('templates/bike_share_eda.html')

@app.route("/contact")
@cross_origin()
def contact():
    return render_template('Contact.html')

if __name__ == "__main__":
    print('From main')
    # port = int(os.environ.get('PORT', 8080))
    global bike_model
    app.run(host='localhost', port=config.PORT, debug=config.DEBUG_MODE)
    # app.run(debug=True)
    # app.run(host='0.0.0.0',port=port)
