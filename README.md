Techincal sample for Lyft Software Engineering Apprenticeship

- Objective:
If you don’t have a current code sample you can share, please write a small web application in one of the above languages (Python/Ruby/Node). It only needs to accept a POST request to the route “/test” which accepts one argument “string_to_cut” returns a JSON object with the key “return_string” and a string containing every third letter from the original string. E.g. if you POST {"string_to_cut": "iamyourlyftdriver"}, it will return: {"return_string": "muydv"}.] 

- Testing:
To see expected behavior you can test against a current working example with the command: curl -X POST https://lyft-interview-test.herokuapp.com/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'