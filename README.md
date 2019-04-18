# Microservice
Example of microservice using Falcon, Token Authentication and generating an own token to access the content.

## To execute we use
- gunicorn microservice_falcon:api
![Screenshot](img/img1.png)

We will be able to observe in our terminal, the new generated token that we will use.

## We will use HTTPie, let's see
- http http://localhost:8000/api
![Screenshot](img/img2.png)

We need an authentication token as we can see.

## Let's put one and let's see what happens
- http http://localhost:8000/api Authorization:1234
![Screenshot](img/img3.png)

As expected, the placed token is not valid

## Finally let's test with the generated token that we have
- http http://localhost:8000/api Authorization:70b9db95-d606-42d2-ac8e-60a3d5dae8f3
![Screenshot](img/img4.png)

## Cool!!!

## Credits
This project would not be possible without:
- https://falconframework.org/
- https://httpie.org/
