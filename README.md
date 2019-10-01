epc-data-import
===


Design
---
This program is broken into three steps:

1. Logs into the [EPC feed website](https://epc.opendatacommunities.org/) with a pre-registered email/token combination.
The token is obtained from the email link provided when registering.

2. Downloads feed into local scratch space.

3. Scans through the feed zip for each CSV regarding each local authority. Each CSV is loaded into a pandas dataframe
and filtered on the required columns. Once a dataframe is loaded, it's then upserted into a target table in a local
postgres instance.


Running
---
Project is unfinished. It can be run by adding a valid `LOGIN_TOKEN` and `LOGIN_EMAIL` to the docker-compose.yml and executing
`docker-compose up --build`


TODOs
---
1. Tests:
    - HEAD request to check if login worked before downloading.
    - Check data structure with dummy CSV
    - Check upsert successful with dummy CSV
2. Use ORM for creating table
3. Fix errors around upserts
4. Error handling and monitoring
5. Linting



Design improvements
---
1. Scaling imports
    - Currently needs scratchspace as large as the feed zip
    - Could either use API for updates or use cloud storage (S3) to sink data out without touching local disk
