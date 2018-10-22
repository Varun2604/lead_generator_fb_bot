#### Lead Generator Facebook BOT

- A facebook chatbot built over flask(http://flask.pocoo.org/), that can generate leads for your business.
- Just plug the AI engine with the project.

(prerequsites - create a database, and update config.py accordingly)
Steps for Database migrations: (all commands to be executed from the root)
- flask db init (will create a migrations directory)
- flask db migrate (will create the necessary migrations)
- flask db upgrade (will conduct the necessary migrations)

Steps for client building:
- install handlebars(https://handlebarsjs.com)
- execute build_client.sh or the corresponding bat file.

Starting the flask server (run the below commands from the root)
- export FLASK_APP=index.py     (export app root)
- flask run

To run api.ai, remember to export GOOGLE_APPLICATION_CREDENTIALS (download from https://cloud.google.com/docs/authentication/getting-started)

TODO : 
1. verify the facebook event response with reciepient id (check if it the id will come in while getting subscription)
2. streamline error handling
3. use nginx to serve static files
