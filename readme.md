This api is a wrapper for a external api, to grasp concepts needed to work with external apis
also, it will use caching to improve server resource usade, using rudis as a local memory cache.

Basically, the user send the city code though our api, we first check is its a valid citycode, and
if we have cached information acout the weather of that area, if we have, we will send the cached data
otherwise we send a request to a external weather api, cache the result, and send it to the user.

We will use openweathermap.org to do our queries, the api key should be stored in a .env
file on the project root with one line:
API_KEY=YOUR_API_KEY

Its a learning project, so i welcome any critic and insight.