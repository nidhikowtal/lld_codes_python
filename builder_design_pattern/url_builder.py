class URLBuilder:
    def __init__(self):
        self.scheme = "http"
        self.host = None
        self.params = {}

    def set_scheme(self, scheme):
        self.scheme = scheme
        return self

    def set_host(self, host):
        self.host = host
        return self

    def add_param(self, key, value):
        self.params[key] = value
        return self

    def build(self):
        url = f"{self.scheme}://{self.host}"
        if self.params:
            query = "&".join([f"{k}={v}" for k, v in self.params.items()])
            url += f"?{query}"
        return url


if __name__ == "__main__":
    url = (URLBuilder()
           .set_scheme("https")
           .set_host("example.com")
           .add_param("q", "python")
           .add_param("page", 1)
           .build())

    print("URL: ", url)
