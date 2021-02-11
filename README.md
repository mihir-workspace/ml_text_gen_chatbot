# ML Chatbot
Text_genration bot using GTP-2 model (microsoft/DialoGPT-medium)
You can deplot the bot using Fastapi by running command :
```bash
pip install requirements.txt
cd src/
uvicorn chatbot:app --reload
````

Also you can check the output in termial using Curl command line utitlity
```bash
curl -X GET "http://127.0.0.1:8000/chat?text=Hello%2C%20how%20are%20you%3F" \
 -H "accept: application/json"
 
 >>> { "Answer":"I'm good, how are you?"}
```

Example :
![Terminal/output](https://github.com/mihir-workspace/ml_text_gen_chatbot/blob/main/images/Screenshot%20from%202021-02-11%2013-48-46.png)


Alternative way is you Fastapi GUI service which can be access by: 
```
http://127.0.0.1:8000/docs
```
![](https://github.com/mihir-workspace/ml_text_gen_chatbot/blob/main/images/Screenshot%20from%202021-02-11%2013-32-21.png)

* For more example to see : [Example_images](https://github.com/mihir-workspace/ml_text_gen_chatbot/tree/main/images)
