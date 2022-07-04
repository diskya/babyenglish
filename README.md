# babyenglish
#### My very first web app made by Django & Bootstrap!
#### Deployed to Azure App Service, with Whitenose lib to serve Django static files.

# Notes for Deployment:
1. Create an Azure App Service and connect to Github Actions.  

2. Before pushing to github, run `python manage.py collectstatic` for Whitenose to serve static files.   
    a small trick might be useful : configure media url with a /static prefix to get treated as static files.  
    `image = models.ImageField(upload_to='static/words_learn/media/', blank=True)`  

3. Pay attention to the following parameters in settings.py:   
    `DEBUG = False`   
    `ALLOWED_HOSTS = ['*']`  
    `CSRF_TRUSTED_ORIGINS = ['https://*.azurewebsites.net',]`  
    Also, add Whitenose as MIDDLEWARE `'whitenoise.middleware.WhiteNoiseMiddleware'`  


![alt tag](cover.png)
