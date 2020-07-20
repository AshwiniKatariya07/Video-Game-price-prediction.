from flask import Flask, render_template, request, jsonify
from sklearn.externals import joblib
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = joblib.load('random_forest_model2.pkl')

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        ID = int(request.form['ID'])
        CONSOLE = int(request.form['CONSOLE'])
        CRITICS_POINTS = int(request.form['CRITICS_POINTS'])
        USER_POINTS = int(request.form['USER_POINTS'])
        Electronic_Arts= request.form['Electronic_Arts']
        if (Electronic_Arts == 'Electronic_Arts'):
            Electronic_Arts = 1
            Activision = 0
            Ubisoft = 0
            Nintendo = 0
            Thq = 0
            Sony_Computer_Entertainment = 0
            Take_Two_Interactive = 0
            Sega = 0
            Konami_Digital_Entertainment = 0
            Namco_Bandai_Games = 0
            #Other = 0
        elif (Electronic_Arts == 'Activision'):
            Electronic_Arts = 0
            Activision = 1
            Ubisoft = 0
            Nintendo = 0
            Thq = 0
            Sony_Computer_Entertainment = 0
            Take_Two_Interactive = 0
            Sega = 0
            Konami_Digital_Entertainment = 0
            Namco_Bandai_Games = 0
            #Other = 0
        elif (Electronic_Arts == 'Ubisoft'):
            Electronic_Arts = 0
            Activision = 0
            Ubisoft = 1
            Nintendo = 0
            Thq = 0
            Sony_Computer_Entertainment = 0
            Take_Two_Interactive = 0
            Sega = 0
            Konami_Digital_Entertainment = 0
            Namco_Bandai_Games = 0
            #Other = 0
        elif (Electronic_Arts == 'Nintendo'):
            Electronic_Arts = 0
            Activision = 0
            Ubisoft = 0
            Nintendo = 1
            Thq = 0
            Sony_Computer_Entertainment = 0
            Take_Two_Interactive = 0
            Sega = 0
            Konami_Digital_Entertainment = 0
            Namco_Bandai_Games = 0
            #Other = 0
        elif (Electronic_Arts == 'Thq'):
            Electronic_Arts = 0
            Activision = 0
            Ubisoft = 0
            Nintendo = 0
            Thq = 1
            Sony_Computer_Entertainment = 0
            Take_Two_Interactive = 0
            Sega = 0
            Konami_Digital_Entertainment = 0
            Namco_Bandai_Games = 0
            #Other = 0
        elif (Electronic_Arts == 'Sony_Computer_Entertainment'):
            Electronic_Arts = 0
            Activision = 0
            Ubisoft = 0
            Nintendo = 0
            Thq = 0
            Sony_Computer_Entertainment = 1
            Take_Two_Interactive = 0
            Sega = 0
            Konami_Digital_Entertainment = 0
            Namco_Bandai_Games = 0
            #Other = 0
        elif (Electronic_Arts == 'Take-Two-Interactive'):
            Electronic_Arts = 0
            Activision = 0
            Ubisoft = 0
            Nintendo = 0
            Thq = 0
            Sony_Computer_Entertainment = 0
            Take_Two_Interactive = 1
            Sega = 0
            Konami_Digital_Entertainment = 0
            Namco_Bandai_Games = 0
            #Other = 0
        elif (Electronic_Arts == 'Sega'):
            Electronic_Arts = 0
            Activision = 0
            Ubisoft = 0
            Nintendo = 0
            Thq = 0
            Sony_Computer_Entertainment = 0
            Take_Two_Interactive = 0
            Sega = 1
            Konami_Digital_Entertainment = 0
            Namco_Bandai_Games = 0
            #Other = 0

        elif (Electronic_Arts == 'Konami_Digital_Entertainment'):
            Electronic_Arts = 0
            Activision = 0
            Ubisoft = 0
            Nintendo = 0
            Thq = 0
            Sony_Computer_Entertainment = 0
            Take_Two_Interactive = 0
            Sega = 0
            Konami_Digital_Entertainment = 1
            Namco_Bandai_Games = 0
            #Other = 0

        elif(Electronic_Arts == 'Namco_Bandai_Games'):
            Electronic_Arts = 0
            Activision = 0
            Ubisoft = 0
            Nintendo = 0
            Thq = 0
            Sony_Computer_Entertainment = 0
            Take_Two_Interactive = 0
            Sega = 0
            Konami_Digital_Entertainment = 0
            Namco_Bandai_Games = 1
            #other = 0

        else:
            Electronic_Arts = 0
            Activision = 0
            Ubisoft = 0
            Nintendo = 0
            Thq = 0
            Sony_Computer_Entertainment = 0
            Take_Two_Interactive = 0
            Sega = 0
            Konami_Digital_Entertainment = 0
            Namco_Bandai_Games = 0
            #Other = 0


        #Year = Year-2020
        RATING_E10 = request.form['Rating']
        if RATING_E10 == 'RATING_E10':
            RATING_E10 = 1
            RATING_M = 0
            RATING_T = 0
        elif(RATING_E10 == 'RATING_M'):
            RATING_E10 = 0
            RATING_M = 1
            RATING_T = 0
        elif (RATING_E10 == 'RATING_T'):
            RATING_E10 = 0
            RATING_M = 0
            RATING_T = 1
        else:
            RATING_E10 = 0
            RATING_M = 0
            RATING_T = 0


        CATEGORY_adventure = request.form['Category']
        if CATEGORY_adventure == 'CATEGORY_adventure':
            CATEGORY_adventure = 1
            CATEGORY_fighting = 0
            CATEGORY_misc = 0
            CATEGORY_platform =0
            CATEGORY_puzzle = 0
            CATEGORY_racing = 0
            CATEGORY_role_playing = 0
            CATEGORY_shooter = 0
            CATEGORY_simulation = 0
            CATEGORY_sports = 0
            CATEGORY_strategy = 0
        elif (CATEGORY_adventure == 'CATEGORY_fighting'):
            CATEGORY_adventure = 0
            CATEGORY_fighting = 1
            CATEGORY_misc = 0
            CATEGORY_platform =0
            CATEGORY_puzzle = 0
            CATEGORY_racing = 0
            CATEGORY_role_playing = 0
            CATEGORY_shooter = 0
            CATEGORY_simulation = 0
            CATEGORY_sports = 0
            CATEGORY_strategy = 0

        elif (CATEGORY_adventure == 'CATEGORY_misc'):
            CATEGORY_adventure = 0
            CATEGORY_fighting = 0
            CATEGORY_misc = 1
            CATEGORY_platform = 0
            CATEGORY_puzzle = 0
            CATEGORY_racing = 0
            CATEGORY_role_playing = 0
            CATEGORY_shooter = 0
            CATEGORY_simulation = 0
            CATEGORY_sports = 0
            CATEGORY_strategy = 0

        elif (CATEGORY_adventure == 'CATEGORY_platform'):
            CATEGORY_adventure = 0
            CATEGORY_fighting = 0
            CATEGORY_misc = 0
            CATEGORY_platform = 1
            CATEGORY_puzzle = 0
            CATEGORY_racing = 0
            CATEGORY_role_playing = 0
            CATEGORY_shooter = 0
            CATEGORY_simulation = 0
            CATEGORY_sports = 0
            CATEGORY_strategy = 0

        elif (CATEGORY_adventure == 'CATEGORY_puzzle'):
            CATEGORY_adventure = 0
            CATEGORY_fighting = 0
            CATEGORY_misc = 0
            CATEGORY_platform = 0
            CATEGORY_puzzle = 1
            CATEGORY_racing = 0
            CATEGORY_role_playing = 0
            CATEGORY_shooter = 0
            CATEGORY_simulation = 0
            CATEGORY_sports = 0
            CATEGORY_strategy = 0

        elif (CATEGORY_adventure == 'CATEGORY_racing'):
            CATEGORY_adventure = 0
            CATEGORY_fighting = 0
            CATEGORY_misc = 0
            CATEGORY_platform = 0
            CATEGORY_puzzle = 0
            CATEGORY_racing = 1
            CATEGORY_role_playing = 0
            CATEGORY_shooter = 0
            CATEGORY_simulation = 0
            CATEGORY_sports = 0
            CATEGORY_strategy = 0

        elif (CATEGORY_adventure == 'CATEGORY_role-playing'):
            CATEGORY_adventure = 0
            CATEGORY_fighting = 0
            CATEGORY_misc = 0
            CATEGORY_platform = 0
            CATEGORY_puzzle = 0
            CATEGORY_racing = 0
            CATEGORY_role_playing = 1
            CATEGORY_shooter = 0
            CATEGORY_simulation = 0
            CATEGORY_sports = 0
            CATEGORY_strategy = 0

        elif (CATEGORY_adventure == 'CATEGORY_shooter'):
            CATEGORY_adventure = 0
            CATEGORY_fighting = 0
            CATEGORY_misc = 0
            CATEGORY_platform = 0
            CATEGORY_puzzle = 0
            CATEGORY_racing = 0
            CATEGORY_role_playing = 0
            CATEGORY_shooter = 1
            CATEGORY_simulation = 0
            CATEGORY_sports = 0
            CATEGORY_strategy = 0

        elif (CATEGORY_adventure == 'CATEGORY_simulation'):
            CATEGORY_adventure = 0
            CATEGORY_fighting = 0
            CATEGORY_misc = 0
            CATEGORY_platform = 0
            CATEGORY_puzzle = 0
            CATEGORY_racing = 0
            CATEGORY_role_playing = 0
            CATEGORY_shooter = 0
            CATEGORY_simulation = 1
            CATEGORY_sports = 0
            CATEGORY_strategy = 0

        elif (CATEGORY_adventure == 'CATEGORY_sports'):
            CATEGORY_adventure = 0
            CATEGORY_fighting = 0
            CATEGORY_misc = 0
            CATEGORY_platform = 0
            CATEGORY_puzzle = 0
            CATEGORY_racing = 0
            CATEGORY_role_playing = 0
            CATEGORY_shooter = 0
            CATEGORY_simulation = 0
            CATEGORY_sports = 1
            CATEGORY_strategy = 0
        else:
            CATEGORY_adventure = 0
            CATEGORY_fighting = 0
            CATEGORY_misc = 0
            CATEGORY_platform = 0
            CATEGORY_puzzle = 0
            CATEGORY_racing = 0
            CATEGORY_role_playing = 0
            CATEGORY_shooter = 0
            CATEGORY_simulation = 0
            CATEGORY_sports = 0
            CATEGORY_strategy = 0

        no_year= int(request.form['Year'])
        no_year = 2020-no_year
        total_points = CRITICS_POINTS * USER_POINTS

        prediction = model.predict([[ID, CONSOLE, CRITICS_POINTS, USER_POINTS, Electronic_Arts, Activision , Ubisoft , Nintendo ,Thq , Sony_Computer_Entertainment ,
            Take_Two_Interactive ,Sega ,Konami_Digital_Entertainment ,Namco_Bandai_Games,RATING_E10 ,RATING_M ,RATING_T, CATEGORY_adventure, CATEGORY_fighting,
            CATEGORY_misc, CATEGORY_platform, CATEGORY_puzzle,CATEGORY_racing, CATEGORY_role_playing,CATEGORY_shooter,CATEGORY_simulation, CATEGORY_sports,
            CATEGORY_strategy, no_year , total_points
                                     ]])
        output= round(prediction[0],3)
        if output <0:
            return render_template('index.html', prediction_text = "Sorry you cannot sell this car")
        else:
            return render_template('index.html', prediction_text="Your Video-Game price is Rs. {}".format(output))
if __name__=="__main__":
    app.run(debug=True)