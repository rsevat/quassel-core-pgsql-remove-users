# quassel-core-pgsql-remove-users
Quick and dirty script to remove users from a quassel-core pgsql backend. Removing users is not possible with quassel-core. Quassel-core feature request to add a --remove-user option: http://bugs.quassel-irc.org/issues/1071

Credits to Lazza, I've used the same SQL commands as in his script for SQLite3:
https://github.com/Lazza/quassel-manage-users/blob/patch-1/manageusers.py

Usage:
python remove-users.py --user-to-delete=testuser
python remove-users.py --list-users

Todo:
Add more error handling. For now this works.

I also recommend doing the PostgreSQL performance and maintenance tips:
http://bugs.quassel-irc.org/projects/1/wiki/PostgreSQL
