# Design doc to facilitate feature specification

## Etelemetry service objectives:
- Return useful information to the user about the state of the software (bugs, new versions, etc.,.)
- Track software usage

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
