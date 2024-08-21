# Puppet manifest to configure SSH client

# Ensure that the SSH configuration file exists
file { '/root/.ssh/config':
  ensure => file,
  owner  => 'root',
  group  => 'root',
  mode   => '0600',
}

# Set up the private key for authentication
file_line { 'Declare identity file':
  path  => '/root/.ssh/config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^.*IdentityFile.*$',
}

# Disable password authentication
file_line { 'Turn off passwd auth':
  path  => '/root/.ssh/config',
  line  => '    PasswordAuthentication no',
  match => '^.*PasswordAuthentication.*$',
}
