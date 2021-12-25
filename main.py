import requests as requestses
import ConfigX as Conf

def Url_Shortner(Full_Link,Link_Name):
    
    Subadra = {"key": Conf.API_KEY, "short": Full_Link, "name": Link_Name}
    Req = requestses.get(Conf.BASE_URL, params=Subadra)
    Data = Req.json()
    
    try:
        title = Data['url']['title']
        fullLink = Data['url']['fullLink']
        date = Data['url']['date']
        shortLink = Data['url']['shortLink']
    
        print("Title: " + title);
        print("Full Link: " + fullLink);
        print("Date: " + date);
        print("Shorted Link: " + shortLink);
        
    except:
        status = Data['url']['status']
        print('Error Status: ', status);

    
Ful_Lin = input("Enter Your Link: ");
Lin_Nam = input("Enter Link Name: ");
print();
print();
Url_Shortner(Ful_Lin,Lin_Nam);
print();