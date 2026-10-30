Caching Expensive Calculations

You are optimizing performance for a system that frequently repeats the same 
heavy calculations (e.g., a backend system or a financial calculator).


Tasks:

Create a decorator called cache_results:

Use a dictionary to store past results based on arguments.

If the same arguments are passed again, return the cached result.

Otherwise, compute the result, cache it, and return the new value.

Apply it to a function multiply(a, b):

It simply returns the product of two integers.

The decorated function should:

Return "Computed: result" for new computations.

Return "From Cache: result" for repeated calls with the same arguments.

