# DORA metrics quiz

## Q1
- Deployment Frequency: how often you deploy to production — it measures throughput and speed.
- Lead Time for Changes: time from commit to running in production — it measures how much friction sits in your pipeline.
- Change Failure Rate: % of deploys causing a production failure — it measures the quality of your release process.
- MTTR: time to restore service after an incident — it measures your ability to detect and recover.

## Q2
Deployment Frequency is poor. Four deploys a year means large, infrequent, riskier batches — the classic "low performer" pattern, whereas elite teams deploy on demand, multiple times a day.

## Q3
Lead Time for Changes improves. Justification: that's literally the interval this metric measures — merge-to-production time, nothing else.

## Q4
Change Failure Rate (25%). High = bad. Justification: you want failures rare; a high CFR means your tests/review process isn't catching problems before they hit prod.

## Q5
Culture, Automation, Lean, Measurement, Sharing. Culture and Sharing build trust and collaboration, Automation and Lean cut waste and manual risk, and Measurement (the DORA metrics) makes progress objective rather than a matter of opinion.

## Q6
False. Elite teams actually deploy more often and in smaller batches. Small batches carry less risk each, are easier to test and roll back, and give faster feedback — the opposite of the statement, which describes what really pushes Change Failure Rate and Lead Time in the wrong direction.

## Q7
(b) monitoring/alerting plus automated rollback, since MTTR is the sum of detection time and recovery time. Option (a) adds friction upstream but doesn't speed up recovery, and (c) has nothing to do with incident response and only makes batches bigger.

## Q8
Throughput is Deployment Frequency and Lead Time; stability is Change Failure Rate and MTTR. DORA's key finding is that these two pairs aren't a trade-off — elite teams score well on both at once, showing that speed and stability reinforce each other rather than compete.

## Q9
Blameless post-mortems exist to find systemic root causes instead of blaming people, because blame makes people hide mistakes or downplay near-misses, starving the team of the information it needs to fix the system. Psychological safety keeps the feedback loop honest and fast, which over time also improves Change Failure Rate and MTTR.