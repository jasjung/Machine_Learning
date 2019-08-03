# postgres

- [https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/](https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/)


## Migrate from SQLITE to POSTGRES 

- https://stackoverflow.com/questions/50322966/changing-django-development-database-from-the-default-sqlite-to-postgresql
- https://gist.github.com/sirodoht/f598d14e9644e2d3909629a41e3522ad
- https://medium.com/agatha-codes/painless-postgresql-django-d4f03364989



## Download and set up postgres

- [path variable](https://postgresapp.com/documentation/cli-tools.html)

Set up postgres account (not in venv)

```
sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp
```

```
psql
```

