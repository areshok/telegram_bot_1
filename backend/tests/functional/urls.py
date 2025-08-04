BASE_URL = "http://127.0.0.1:8000"

URLS = {
    "api": {
        "product": {
            "create": f"{BASE_URL}/api/v1/product/",
            "update": f"{BASE_URL}/api/v1/product",
            "list": f"{BASE_URL}/api/v1/product",
            "delete": f"{BASE_URL}/api/v1/product",
        }
    },

    #"web": {
    #    "product": {
    #        "list": f"{BASE_URL}/product/",
    #        "create": f"{BASE_URL}/product/create",
    #        "detail": f"{BASE_URL}/product/{}/detail/",
    #    },
    #},

}
