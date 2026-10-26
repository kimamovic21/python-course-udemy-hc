ATM Withdrawal Simulator

Imagine you’re building a backend feature for an ATM. 
Customers can request multiple withdrawals during one session. 
Your task is to simulate how the system should handle each request based on the account balance.

Tasks:

Use a while loop to iterate through the list named withdrawals.

For every withdrawal:

✅ If the current balance is enough:

Subtract the amount.

Append a success message: "Withdrawn: {amount}"

❌ If not enough:

Append a message: "Insufficient funds for requested amount: {amount}"

After all withdrawals:

Append the final balance as: "Remaining Balance: balance"

Return a list containing all the messages.