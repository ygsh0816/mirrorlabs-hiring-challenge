# mirrorlabs-hiring-challenge
I have created 2 APIs actually one will serve as a 
producer to produce to the topic and the other will 
return the weather information using the consumer. 
I did this on purpose to learn kafka along with the 
task completion, I had setup kafka local cluster 
to learn and complete this task.

## Assumptions
 * Kafka is already set up and running. Although I created a producer.
 * The Kafka topic and servers are provided via config variables.

## Getting Started
* Clone the repository.
* Create a virtual environment and activate it.
* Install dependencies using `pip install -r requirements.txt`.
* Set Kafka variables in `app/config.py` file.
* Run the service using python `uvicorn app.main:app --reload`.
* produce the user data to the producer using the following post endpoint
`/produce/`.
* The request data for the above post request would be `{"user_id": "yogesh", "lat": "52.523430", "long": "13.411440", "timestamp": "123456789"}`
* Get the information of the weather using the following endpoint `user/weather?user_id=yogesh`
* The swagger documentation can be found here `/docs`

## Next Steps
* Add authentication and authorization to the REST API.
* Implement error handling and logging.
* Create Dockerfile and Docker Compose for containerization.
* Write unit tests and integration tests.
* Set up CI/CD pipeline.
* Customize the documentation of APIs
## Resources
* Kafka Python Documentation
`https://kafka-python.readthedocs.io/en/master/install.html`
* Open-Meteo API Documentation
`https://open-meteo.com/en/docs`
* FastAPI Documentation
`https://fastapi.tiangolo.com/tutorial/`
* https://lemoncode21.medium.com/simple-kafka-consumer-and-producer-using-fastapi-be1b55deea2
* https://medium.com/big-data-engineering/hello-kafka-world-the-complete-guide-to-kafka-with-docker-and-python-f788e2588cfc
* https://medium.com/@arturocuicas/fastapi-and-apache-kafka-4c9e90aab27f



