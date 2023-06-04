# PROJET TODOs

1. Blind friendly -> show description
2. up to date venues / items content
3. bot logo / description
4. Gifs & descriptions
5. Technical docs / flos

# All Square

This is a project for Square Hackathon.

Square is more than a payment provider, they're positioning themself as businesses' operating system. Square provides online sales channels, in-app payment solutions, staff management and more.

Square generally develops B2B solutions. With this project we wished to touch with a B2C solution to Square's direct and indirect customers. Business powered by Square, can create an online presence. So businesses can join to a chatbot (the 5Quare) developed and managed by Square.

![](assets/Diagrams-Business-Flow.png)

Square can offer a centralized chatbot to end-users, who can interact with the official Square channel, which lists all nearby Square-powered venues.

Businesses can get some benefits through this chatbot as below;


> 1 | **Better discoverability** by being listed in chatbot

> 2 | Providing **menu from a centralized place.** (Instead of maintaining another app for QR-menus.)

> 3 | Offering a **new and accessible way** of placing orders through chatbot interface

> 4 | Reach to a **bigger customer base,** by removing the need of installing an app for the user.

> 5 | Reaching to **customer data,** which makes easy to contact them and offer discounts, loyalty program, in summary reasons to revisit the venue




## How to Run?

This bot is running on Telegram with [TheSquareBot](https://t.me/TheSquareBot) bot name.

You can interact with it. It uses Sandbox data.

Or you can deploy your own by following the title below, with a different Telegram Bot name.


## How to Deploy?

First create a virtual environment.

```Shell
python3 -m venv env
```

Create an environment file and insert credentials;
```Shell
touch .env
nano .env
```

Place these keys into the file;

```Dotenv
TOKEN=<Telegram Bot Token From @BotFather>
APPNAME=<Define Bot Name>
SQUARE_APP_ID_SANDBOX=<App Id>
SQUARE_TOKEN_SANDBOX=<Square Token>
PAYMENT_PROVIDER_TOKEN=<Token from Telegram Payment Module>
```

Telegram wraps Payment Provicer's token and provide another `PAYMENT_PROVIDER_TOKEN`. This token can be generated from Telegram's [BotFather](https://t.me/BotFather) bot. Telegram currently do not support Square's Payment System.

After creating the environment variables, activate the environment, install the requirement, and run the application.

```Shell
source env/bin/activate
pip3 install -r requirements.txt
python3 app.py
```


## Suggestions to Square

1. Providing **services to Telegram** as a payment provider, to streamline chatbot developments.
1. **Displaying unpaid/unfulfilled orders** in Seller Dashboard, to abolish 3rd party order follow interfaces.  [Reference](https://developer.squareup.com/forums/t/order-not-showing-in-sandbox-dashboard-for-v2-orders/2407/2)
1. ...