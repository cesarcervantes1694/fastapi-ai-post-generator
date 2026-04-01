from fastapi import FastAPI
from routes import post_routes, auth_routes
from middlewares.jwt_validation import AuthMiddleware

app = FastAPI()

app.add_middleware(AuthMiddleware)

# Registrar rutas
app.include_router( auth_routes.router)
app.include_router(post_routes.router)