Smart Token Dispenser

You are developing a Smart Token Dispenser system, like those found in banks or clinics. 
This system reset counters based on user activity and needs to run until manually stopped.


Tasks:

Create an infinite generator function called token_dispenser(start=1).

On each call to next(), it should yield the current token number and increment it.

If a value is passed to the generator using send(), the generator should reset the token number to that new value.

The generator should handle the .close() method gracefully and print "Dispenser closed." when it is closed.