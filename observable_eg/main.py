# here is our publisher (also known as the Observable)
from news_pub import NewsPublisher
# here are the subscribers (also known as listeners or observers)
from email_sub import EmailSubscriber

# careful - a one-member tuple MUST have a trailing comma
subs_t = (EmailSubscriber, )

def main():
    '''iterate over all subscribers, notifying of fresh news'''
    news_publisher = NewsPublisher()
    for subscriber in subs_t:
        subscriber(news_publisher)
        news_publisher.add_news('News flash: we are nearly there!')
    # notify all teh subscribers
    news_publisher.notify_subscribers() # they all get notified

if __name__ == '__main__':
    main()