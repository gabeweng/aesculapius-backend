![Aesculapius](https://lh5.googleusercontent.com/K2mAY5eFKC345MMLaTJ0DuyiiiWFy1aSqnIME3OTH8Cw3w2hq0zS8PJl7awjYNJTE83XmsXLqbaT9lfEjusYndyqVBEiT1BVJRAVbiLLXgP3qDRveVOcYwlvuAfQrx1kNyoEIcgVnMUP-715sKT0f3llPSpdZGQ08wHPuulLYQta0WqbI6Eser16zYbhTQ)
## Inspiration
We were inspired by the multiple health care websites across the internet, which are filled with crucial healthcare information, but we wanted to make this information more accessible, especially to people who do not understand technology but could greatly benefit from the information contained in the Internet. To help people like this, we created a chatbot, as human interaction is something almost everyone can understand, which makes the chatbot more accessible than self research. This goal of helping people access the healthcare information they need led to us naming the project Asclepius, the Roman hero of medicine whose snake entwined staff still represents medicine today. 

## What it does
The chatbot uses Cohere Intent Recognition to intelligently interpret the inputs of the user. We then use multiple external APIs to retrieve the healthcare information as requested by the user. This information is then displayed to the user in multiple ways. From a simple response from the chat bot to the information being mapped or graphed depending on the needs of the user. The chat bot is meant to be general and all encompassing, serving as a medium to get the user important healthcare information and direct them to professional help or emergency services if required. 

## How we built it
We split up this project into a front end (made with svelte and tailwind) and a backend (made with Python). The frontend contains the website and the chatbot. Based on the inputs of the user, the chatbot requests information from the Python web service API in the backend, which gets its information from external APIs such as Twillio and Cohere. We used both for sending out emergency messages, as well as using text messages to talk to a chatbot

## Challenges we ran into
- Making the svelte frontend
- Setting up the routing in the svelte frontend
- Using Vercel to host the backend
- Using Twilio to SMS message phones

## Accomplishments that we're proud of
- Making a web service Python API and hosting it on Vercel
- Using prompt engineering and Cohere’s text generation to make a chatbot
- Using cohere to recognize user’s intent
- Adapting and integrating a chatbot widget originally made for RASA
- Using Twilio to send and receive text messages in the backend
- Connecting our web application to a Domain.com domain

## What we learned
- How to recognize intent using Cohere
- How to use Twilio
- Splitting up the frontend and backend

## What's next for Aesculapius 
- Interactive map with hospital locations from backend
- Higher quantity of medical information


This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `pages/index.js`. The page auto-updates as you edit the file.

[API routes](https://nextjs.org/docs/api-routes/introduction) can be accessed on [http://localhost:3000/api/hello](http://localhost:3000/api/hello). This endpoint can be edited in `pages/api/hello.js`.

The `pages/api` directory is mapped to `/api/*`. Files in this directory are treated as [API routes](https://nextjs.org/docs/api-routes/introduction) instead of React pages.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.
