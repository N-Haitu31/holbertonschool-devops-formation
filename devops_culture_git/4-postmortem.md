# Postmortem for PixelCart

## 1 - Factual timeline
- occurred : Friday - 17H52 - a config change (database URL) is edited by hand directly on the production server, with a typo.
- detected : Saturday - 09H15 - Inès, unofficially on call, finds the complaints.
- resolved :  Saturday - 11H40 - after reaching Karim and identifying the typo, the config file is fixed by hand and service is restored.

## 2 - Systemic Causes
- No deployment pipeline. Manual SSH access, hand-edited files on prod, no automated validation.
- No environment parity / no review. No staging environment, no second pair of eyes before shipping.
- No monitoring or alerting. Checkout is core revenue but nothing detects failures automatically — a social media post did.
- No on-call or rollback plan. No real ownership, no changelog, no way to roll back quickly.

## 3 - Three priority actions
- Monitoring and alerting on checkout. Closes the ~15h detection gap, by far the biggest chunk of the outage.
- Version-controlled, reviewed deploy pipeline. Removes the root failure mode (unreviewed manual edit on prod) and makes rollback instant.
- Real on-call rotation + rollback runbook. Turns the 2h25 diagnosis into a fast, defined response.

## 4 - Link each problem to a DORA metric
| Problem | DORA metric degraded |
|---|---|
| No deployment pipeline | **Deployment Frequency** |
| No environment parity / review | **Change Failure Rate** |
| No monitoring/alerting | **Time to Restore Service (MTTR)** |
| No on-call / rollback plan | **Time to Restore Service (MTTR)** |
| Manual, slow deploy process | **Lead Time for Changes** |