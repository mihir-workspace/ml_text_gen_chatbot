uvicorn chatbot:app --reload

curl -X GET "http://127.0.0.1:8000/chat?text=Hello%2C%20how%20are%20you%3F" \
 -H "accept: application/json"
