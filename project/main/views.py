from django.shortcuts import render

# Create your views here.

def mainpage(request):
    context={
        'generation':12,
        'template':{'lan':'파이썬의 변수, 문법을 HTML에서 사용할 수 있도록 제공하는 직관적인 언어이며 크게 4가지의 기능을 지원한다.',
                    'rep':'HTML에서 반복적으로 사용되는 코드를 따로 분리하여, 다른 페이지에서도 사용 가능하도록 상속한다.'},
        'MTV':['Model/Template/View','Model: 데이터 / Template: 보여지는 부분, 인터페이스 / View: 요청에 따른 적절한 로직 수행','Request -> URL Conf -> View -> Model -> Template -> Response']
}
    return render(request, 'main/mainpage.html',context)
def secondpage(request):
    return render(request, 'main/secondpage.html')