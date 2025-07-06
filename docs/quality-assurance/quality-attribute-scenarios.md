# Quality Attribute Scenarios

## Performance Efficiency

### Importance
The support bot must quickly answer user questions, even during peak load hours. 

#1) Concurrent Users Load

| Attribute           | Performance Efficiency                  |
|                     |                                         |
|   Source            | Multiple simultaneous users             |
|  Stimulus           | 200 concurrent users ask questions at one time |
|  Artifact           | MARS Bot handling requests              |
|   Environment     | Production environment during peak usage period |
|   Response        | The system processes all questions without significant delay and maintains responsiveness |
|   Response Measure| Average response time for bot's answer is under 10 seconds, with no timeouts or failures |

Test: 
Perform load testing — simulate 200 simultaneous requests to the bot and measure the average response time and error rate.

---

# 2) Performance Efficiency: Time-behavior

#### Importance
The user should receive a response almost instantly.

| Attribute           | Performance Efficiency: Time-behavior    |
|                                                                |
|     Source          | User                                     |
|     Stimulus        | User sends a question to the bot         |
|   Artifact          | MARS Bot                                 |
|   Environment       | Production                               |
|   Response          | Bot provides an answer to the user       |
|   Response Measure  | 95% of responses are delivered within 5 seconds |

 Test:  
 Use logging to measure latency for each request, build a graph, and make sure that 95% fit within 5 seconds.

---

#3) Functional Suitability: Functional Correctness

#### Importance
The user should receive relevant and correct answers. Any incorrect or "broken" answer reduces the credibility of the system.

| Attribute           | Functional Suitability: Functional Correctness |
|---------------------|----------------------------------------------|
|     Source         | User                                         |
|    Stimulus        | User asks a supported question to the bot    |
|    Artifact      | MARS Bot                                     |
|   Environment     | Production                                   |
|    Response        | Bot provides the correct and expected answer |
|  Response Measure| At least 98% of test questions (from the reference set) are answered correctly |

Test:  
Create a test set of question-answers and run these questions through the bot, calculate the percentage of correct answers.
