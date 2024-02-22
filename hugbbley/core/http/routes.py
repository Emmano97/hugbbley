from fastapi import FastAPI
class Route:
    def __init__(self, app: FastAPI):
        self.app = app

    def get_routes(self):
        routes = self.app.routes

