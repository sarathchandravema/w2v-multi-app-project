Saving the work details in this page.

Working first draft of multiple apps.
* one app to find the similar words and it routes to specific models. This app contains the basic html page.
    
    `flask --app app-similar_words\app.py run --port=5002` => `http://localhost:5002/similar?word=book&topn=4&model=custom`

* two apps under model category for routing to specific model's app.
    
    via local: `flask --app app-model1\model1.py run --port=5000` => `http://127.0.0.1:5000/model?word=<word>&topn=<topn>`

    via docker: 
        `docker build --tag app-m1 app-model1`
        `docker run -p 5000:5000 app-m1`
    
    `flask --app app-model2\model2.py run --port=5001` => `http://127.0.0.1:5001/model?word=<_word>&topn=<_topn>`