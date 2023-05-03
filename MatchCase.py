def http(status):
    match(status):
        case 100 | 101 :
            print("Info about request")
        case 200 | 204 :
            print("Request processed successfully")
        case 302 | 303 :
            print("Resource moved")
        case 400 | 403 | 404 :
            print("Forbidden request ")
        case _ :
            print("Server error")

http('')


