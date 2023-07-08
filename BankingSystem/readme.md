## API Endpoint Table
| Endpoint                            | HTTP Method | Description                                       |
|-------------------------------------|-------------|---------------------------------------------------|
| /users                              | GET         | Retrieve all registered users.                    |
| /users/{username}                   | GET         | Retrieve a registered user by username.           |
| /users                              | POST        | Register a new user.                              |
| /users                              | DELETE      | Delete all users.                                 |
| /users/{username}                   | DELETE      | Delete a user by username.                        |
| /users/{username}                   | PUT         | Update user details for a given user.             |
| /transactions                       | GET         | Retrieve all transactions.                        |
| /transactions/{transaction_id}      | GET         | Retrieve a transaction by transaction ID.          |
| /transactions                       | POST        | Create a new transaction.                          |
