This api is a wrapper for a external api, to grasp concepts needed to work with external apis
also, it will use caching to improve server resource usade, using rudis as a local memory cache.

Basically, the user send the city code though our api, we first check is its a valid citycode, and
if we have cached information acout the weather of that area, if we have, we will send the cached data
otherwise we send a request to a external weather api, cache the result, and send it to the user. It's
cache function uses redis as a in memory cache, and it worked pretty well, the average query time was
0,5 seconds depending on the period, and went to 0,02 for cached results.

We will use visual crossing api, the api key should be put in a .env file on projects root as follow:
API_KEY=YOUR_API_KEY

The user can specify wich time period he wants from the query param 'period'. Available options are: 'week', 'month' and 'today'

Its a learning project, so i welcome any critic and insight.