## Real-time sentiment analysis of user feedback

Live demo: <URL>

This project demonstrates end-to-end deployment of a transformer model in a web application.

Users answer a simple question about what they think of the page, and the model performs real-time sentiment analysis on user feedback, providing a lightweight proxy for user experience.

Survey-based methods have well-known limitations, but they provide a simple and cost-effective way to collect user data. This work is intended to simulate a plausible scenario for behaviour analysis, using NLP for quantitative insight.

![screenshot](/static/screenshot.png)

Focus:

- End-to-end production
- API design and model serving
- Containerised deployment

Core tech:

- FastAPI (backend)
- Hugging Face Transformers (sentiment analysis)
- Docker (containerisation)
- HTML, CSS, JavaScript (frontend)

## How to run it

Conatainerisation ensures consistent execution across environments. I recommend running the app using Docker.

```bash
#make sure Docker Desktop is installed and running (refer to https://www.docker.com/products/docker-desktop/)

docker build -t webapp .
docker run -p 8000:8000 webapp
```
