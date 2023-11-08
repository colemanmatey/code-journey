
http_statuses = [400, 404, 402, 403, 401, 600]

for status in http_statuses:
    match status:
        case 400:
            print(status, "Bad request") 
        case 401:
            print(status, "Unauthorized")
        case 402:
            print(status, "Payment required")
        case 403:
            print(status, "Forbidden")
        case 404:
            print(status, "Not found")
        case _:
            print("Something is terribly wrong!")
