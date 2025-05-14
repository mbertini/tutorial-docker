# Testing Heroku

1. Create a Heroku account
2. Install Heroku CLI
3. Build the Docker: docker build .
4. Login into Heroku: heroku login
5. Authenticate Docker with Heroku's container registry: heroku container:login
6. Create Heroku app: heroku create heroku-flask-demo  
7. Set app as container app: heroku stack:set container -a heroku-flask-demo
8. Push docker to Heroku registry:  heroku container:push web -a heroku-flask-demo
9. Release the app: heroku container:release web -a heroku-flask-demo
10. Open the app: heroku open -a heroku-flask-demo (or use the browser directly)