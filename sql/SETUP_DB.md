# Creating the PostgreSQL User and Database for Assignment3

This document outlines the steps to create the PostgreSQL user and database specifically for Assignment3.

## Creating the 'postgres' User

The database configuration for Assignment3 specifies a user named 'postgres'.

To create this user, use the `createuser` command in a terminal session:

```
sudo -u postgres createuser --interactive --pwprompt
```

When prompted, enter `postgres` for both the username and password. When asked if the new role should be a superuser, enter `y`. This will give the `postgres` user all the necessary permissions for managing databases.

## Creating the 'Assignment3' Database

The database for Assignment3 is named `Assignment3`. To create this database, use the `createdb` command in a terminal session:

```
createdb -O postgres Assignment3
```

This command creates a new database named `Assignment3` and sets the `postgres` user as the owner.
