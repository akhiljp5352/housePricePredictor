import joblib
import pandas as pd




def encodeLandContour(value):
    dict={
        "Level":0,
        "Bank":1,
        "Low":2,
        "Hill":3
    }
    return dict[value]

def encodeSaleCondition(value):
    dict={
        "Normal":0,
        "Anormal":1,
        "Partial":2,
        "Adjastable":3,
        "Family":4
    }
    return dict[value]

def encodeLotShape(value):
    dict={
        "Regular":0,
        "Irregular1":1,
        "Irregular2":2,
        "Irregular3":3
    }
    return dict[value]

def make_prediction(LotFrontage,LotArea,LotShape,LandContour,PoolArea,SaleCondition):

    X=pd.DataFrame({
        "LotFrontage":[0],
        "LotArea":[0],
        'LotShape':[0],
        'LandContour':[0],
        'PoolArea':[0],
        'SaleCondition':[0]
    })

    X["LotFrontage"]=LotFrontage
    X["LotArea"]=LotArea
    X["LotShape"]=int(LotShape)
    X["LandContour"]=int(LandContour)
    X["PoolArea"]=PoolArea
    X["SaleCondition"]=int(SaleCondition)


    model = joblib.load('model.pkl')

    y=model.predict(X)

    return y[0]
    
