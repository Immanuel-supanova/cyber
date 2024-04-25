# Cyber

Cyber is a django application that handles cryptography for API, it uses rsa and aes encryption standards

```
pip install git+https://github.com/Immanuel-supanova/Cyber.git
```

## settings.py

```
INSTALLED_APPS = [

    'rest_framework',
    'corsheaders',
    'cyber',
]
```

```
MIDDLEWARE = [
    
    "corsheaders.middleware.CorsMiddleware",
   
]
```
```
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
```
```
# Set the JWT cookie name and secure flag
SESSION_COOKIE_SAMESITE = 'Strict'
CSRF_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
JWT_AUTH_COOKIE = 'access_token'
JWT_AUTH_REFRESH_COOKIE = 'refresh_token'
```
```
CORS_ORIGIN_ALLOW_ALL = True
```
```
PRIVATE_KEY_FILE = f"{BASE_DIR}/private_key.pem"
PUBLIC_KEY_FILE = f"{BASE_DIR}/public_key.pem"
```
## urls.py

```
from cyber.views import AplicationTokenRefreshView, ApplicationTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/app/token/', ApplicationTokenObtainPairView.as_view()),
    path('api/app/token/refresh/', AplicationTokenRefreshView.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view()), 
]
```
## gitignore

```
private_key.pem
public_key.pem
```

## cmd

```
python manage.py generate_keys
python manage.py makemigrations
python manage.py migrate
```