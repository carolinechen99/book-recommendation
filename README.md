# Book Recommendation Microservice

A web microservice that recommends books based on a user-provided book title, using the Google Books API. The application is built using Flask and can be deployed to AWS Elastic Beanstalk.

## Getting Started

These instructions will guide you through setting up the project and running it on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package manager)
- virtualenv (optional, for managing virtual environments)

### Installation

1. Clone the repository or download the source code:

````bash
git clone https://github.com/yourusername/book_recommendation_microservice.git

2. Navigate to the project directory:

```bash
    cd book_recommendation_microservice
````

3. Create a virtual environment (optional):

```bash
    python -m venv venv
    source venv/bin/activate
```

4. Install the required packages:

```bash
    pip install -r requirements.txt
```

## Run the application

To run the application on your local machine, execute the following command in the terminal:

```bash
    python app.py
```

The Flask application will start running on http://127.0.0.1:5000/. Open this URL in your browser to use the book recommendation microservice.

## Deployment

The application can be deployed to AWS Elastic Beanstalk or any other platform that supports Python and Flask applications.

### References

- [Google Books API](https://developers.google.com/books/docs/v1/using)
