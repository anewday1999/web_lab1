### ab -c 10 -n 1000 http://127.0.0.1/api/v1/marketPost  
## With balance  
    This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking 127.0.0.1 (be patient)
    Completed 100 requests
    Completed 200 requests
    Completed 300 requests
    Completed 400 requests
    Completed 500 requests
    Completed 600 requests
    Completed 700 requests
    Completed 800 requests
    Completed 900 requests
    Completed 1000 requests
    Finished 1000 requests


    Server Software:        nginx/1.21.5
    Server Hostname:        127.0.0.1
    Server Port:            80

    Document Path:          /api/v1/marketPost
    Document Length:        0 bytes

    Concurrency Level:      10
    Time taken for tests:   0.662 seconds
    Complete requests:      1000
    Failed requests:        0
    Non-2xx responses:      1000
    Total transferred:      279000 bytes
    HTML transferred:       0 bytes
    Requests per second:    1510.49 [#/sec] (mean)
    Time per request:       6.620 [ms] (mean)
    Time per request:       0.662 [ms] (mean, across all concurrent requests)
    Transfer rate:          411.55 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.0      0       1
    Processing:     1    6   5.8      7      53
    Waiting:        1    6   5.8      6      53
    Total:          1    7   5.8      7      53

    Percentage of the requests served within a certain time (ms)
      50%      7
      66%     10
      75%     10
      80%     11
      90%     12
      95%     14
      98%     16
      99%     29
     100%     53 (longest request)
