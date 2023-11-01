# Design doc to facilitate feature specification

## Etelemetry service objectives:
- Track software usage. Annotations:
  - Process starts
  - Process ends + exit status
  - Heartbeats for long runtime tasks
  - Software version
  - Platform (bare-metal, container, etc.)
  - Relevant options
  - "Session" information
  - "User" information
  - (possibly) Elapsed time
  - (possibly) Memory utilization
  - (possibly) CPU utilization
- Feedback to users:
  - Notice of new versions available
  - "Retired" versions (i.e., bad versions with disqualifying bugs)
  - ETA (progress bar or such, using previously acquired stats from other users)

## Wishlist
- use a more generic logging tool as the backend (like prometheus)
- discard IP addresses after geo conversion
- define the message packet, the transformed message packet
- thus far we have been able to do things without caring who used the service 
  (even though not advertised). if messages become arbitrary, we may need 
  registration/auth tokens. brings up a whole different level of complexity that 
  i would like to avoid.
- make querying, accessing, and doing analytic plots
- spin up your own backend on heroku/some such


## Message packets

### Receive

### Transformed

### Send
