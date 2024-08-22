# This manifest configures the Apache web server.

# Increase Nginx file descriptor limit
exec { 'adjust-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx service
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
