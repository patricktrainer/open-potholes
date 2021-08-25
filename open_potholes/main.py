from http import NolaData

if __name__ == "__main__":
    service_calls = "2jgv-pqrq"
    where = {"request_reason": "Pothole"}

    data = NolaData(service_calls)
    data.doFilter(where)
    response = data.doGet()
    