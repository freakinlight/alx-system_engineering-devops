# This Puppet manifest fixes an issue causing a 500 Internal Server Error on Apache.

file { '/var/www/html':
  ensure => 'directory',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

service { 'apache2':
  ensure  => 'running',
  enable  => true,
  require => File['/var/www/html'],
}
