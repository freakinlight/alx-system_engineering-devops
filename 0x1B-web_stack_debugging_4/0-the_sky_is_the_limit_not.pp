# 0-the_sky_is_the_limit_not.pp
# This Puppet manifest optimizes Nginx configuration to handle a high number of concurrent requests.

exec { 'tune-nginx':
  command => '/usr/sbin/nginx -s reload',
  refreshonly => true,
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Exec['tune-nginx'],
}

# Example template (nginx.conf.erb)
#
# worker_processes  auto;
# events {
#     worker_connections  1024;  # increase this value to handle more concurrent connections
# }
# http {
#     sendfile        on;
#     tcp_nopush      on;
#     tcp_nodelay     on;
#     keepalive_timeout  65;
#     types_hash_max_size 2048;
#     include         /etc/nginx/mime.types;
#     default_type    application/octet-stream;
#
#     # Gzip compression
#     gzip on;
#     gzip_disable "msie6";
#
#     include /etc/nginx/conf.d/*.conf;
#     include /etc/nginx/sites-enabled/*;
# }

