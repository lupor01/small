## Real-time sentiment analysis of user feedback

Live demo: <https://small-bzsn.onrender.com><br>
<sub>
⚠️ The app backend uses Render's free tier, running on 512MB of RAM. It takes a minute to wake up from inactivity, and initial requests may be slow.
</sub>

This project demonstrates the end-to-end deployment of a transformer model as a web application.

Focus:

- End-to-end deployment
- API design and model serving
- Containerisation

Core tech:

- FastAPI (backend)
- Hugging Face Transformers (sentiment analysis)
- Docker (containerisation)
- HTML, CSS, JavaScript (frontend)

Users answer a simple question about their experience with the page, and the model performs real-time sentiment analysis on the submitted feedback. The resulting sentiment score provides a lightweight proxy for user experience. Both the feedback and sentiment score are then stored in a database.

Although survey-based methods have well-known limitations, they remain a simple and cost-effective way to collect user data. This project simulates a plausible behavioural analysis workflow using NLP to generate quantitative insight.

![screenshot](/static/screenshot.png)

## How to run

Containerisation ensures consistent execution across environments. I recommend running the app using Docker.

```bash
# make sure Docker Desktop is installed and running (refer to https://www.docker.com/products/docker-desktop/)

docker build -t webapp .
docker run -p 8000:8000 webapp
```
