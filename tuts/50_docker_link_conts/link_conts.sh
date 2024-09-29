# Docker In Practice 2nd ed.
# Technique 8 - Linking Containers For Port Isolation

:'
In the previous technique you saw how to get containers to communicate with user-
defined networks. But there’s an older method of declaring container communication—
Docker’s link flag. This isn’t the recommended way of working anymore, but it has been
part of Docker for a long time, and it’s worth being aware of in case you encounter it in
the wild.

Taking up the torch of the WordPress example, we’re going to separate the MySQL
database tier from the WordPress container, and link these to each other without port
configuration or creating a network.

Why bother with linking if you can already expose ports to the host
and use that? Linking allows you to encapsulate and define the relationships
between containers without exposing services to the host’s network (and
potentially, to the outside world). You might want to do this for security rea-
sons, for example.
'
docker run --name wp-mysql \
  -e MYSQL_ROOT_PASSWORD=yoursecretpassword -d mysql

docker run --name wordpress \
  --link wp-mysql:mysql -p 10003:80 -d wordpress

  
