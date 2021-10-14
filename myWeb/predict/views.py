from django.shortcuts import render
from . import predict as pred


def home(request):
    return render(request,'home.html')


def predict(request):
    LotArea=request.POST.get("LotArea", False)
    FrontageArea=request.POST.get("FrontageArea", False)
    PoolArea=request.POST.get("PoolArea", False)
    LandContour=pred.encodeLandContour(request.POST.get("LandContour",False))
    SaleCondition=pred.encodeSaleCondition(request.POST.get("SaleCondition",False))
    LotShape=pred.encodeLotShape(request.POST.get("LotShape",False))

    cost=pred.make_prediction(FrontageArea,LotArea,LotShape,LandContour,PoolArea,SaleCondition)


    return render(request,'prediction.html',{
        "Cost": cost
    })
