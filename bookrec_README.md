[![Commit rate](https://img.shields.io/github/commit-activity/m/byukan/bookrec?label=Commits)](https://github.com/byukan/bookrec/commits/master)
[![License](https://warehouse-camo.ingress.cmh1.psfhosted.org/110fcca60a43a8ea37b1a5bda616e639325f2f30/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d425344253230332d2d436c617573652d626c75652e737667)](https://github.com/byukan/bookrec/blob/master/LICENSE.txt)


*** 

<h1 align="center">
<sub>
<img  src="https://3.bp.blogspot.com/_RzmIlSwLsTQ/TKK8MUJ1QgI/AAAAAAAAAYg/Xp7GM8hspiw/s1600/BBWrobot.png" height="70" width="40">
</sub>
 BookRec 
<sub>
<img  src="https://3.bp.blogspot.com/_RzmIlSwLsTQ/TKK8MUJ1QgI/AAAAAAAAAYg/Xp7GM8hspiw/s1600/BBWrobot.png" height="70" width="40">
</sub>

</h1>
<p align="center">
<sup> <!-- Pronounciation -->
      BookRec is a chatbot that recommends books based on the conversation you're having with it.
</sup>
<br>
</p>

***

* [Purpose](#purpose)
* [Motivation](#motivation)
* [Functional Specification](#functional-specification)
  * [Dataset](#dataset)
  * [Models](#models)
  * [Cloud Compute](#cloud-compute)
  - [Deployment](#deployment)
* [Brant Yukan](https://brantyukan.com)

## **Purpose**

From a product perspective, this chatbot is conversational and is trained on book summaries and reviews.  It's designed to capture the human voice used when describing literature -- emotions and subjective thought, which we don't typically expect when talking to a computer.  It should feel like an entertaining, conversational concierge, not customer support/service.  It'll recognize named entities and also words you use to describe the "mood" of a novel.  A feature could be to show snippets from the book summary or reviews, and perhaps even the content.

## **Motivation**

I want to build a chatbot that uses advanced NLP and deep learning techniques.  It should be intelligent, not feel like a phone tree or canned responses.  I'd like to go beyond uninteresting techniques like cosine similarity on tfidf vectors.  A modern dialog system uses pattern matching, grounding, search, and text generation.



## Functional Specification

_The vision for this project is a messaging interface that can be open on a browser.  The user can start typing free-form, send texts to the chatbot, which replies with conversationl responses which could be follow up questions, related statements about books, or excerpts._	

#### Dataset
- The data used will be a corpus of product info and reviews pages scraped from *Amazon*.
- The _html_ pages will need to be parsed using BeautifulSoup.
- I'll load all the data into a MongoDB database.  We'll have book metadata, product summary, reviews, and the content itself.
#### Models
- Try to spend the bulk of the time here on model building and learning about advanced techniques.
- Learn about and apply various advanced NLP and deep learning techniques that would be useful for a conversational chatbot.
- Modern approaches combine:
    - pattern matching
    - grounding (logical knowledge graphs and inference)
    - search
    - generative
- Read _NLPIA_ and apply those examples.
#### Cloud Compute
- I'll likely need to rent a compute instance for a GPU to train deep learning models.  Possible options are to see if I can find a good source of AWS free credits.  GCP gives $300 to any new account.  There might be other providers that are free or really cheap, I can look at the guides on fast.ai.
- I expect the data to be comfortably under 50GB.  Either way, if we're eventually going to train on cloud, the data will also have to be there, too.
- Get a barbones model working on a minimal dataset first before spending credits on training and accuracy.
#### Deployment
- If convenient, use a messenger api, like Slack or Facebook Messenger.
- Ideally, host a simple webpage that has a chatbox where you can type.


## Milestones
1. Consolidate all data in a chosen database.
1. Run prototypes of a few chatbot frameworks in jupyter notebooks.  (favor using aichat from nlpia)
- part 2 in NLPIA for deep learnign concepts
- part 3 in NLPIA for actually building a chatbot and advanced NLP
1. Set up a GPU to use.  Perhaps going to be GCP credits unless I find something better.
1. Either set up a simple web interface, pull an example template with flask perhaps.  Or integrate with a messaging api.

## License

[BSD 3-Clause License](https://github.com/byukan/bookrec/blob/main/LICENSE.txt).