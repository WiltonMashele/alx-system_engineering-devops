# This Puppet manifest installs a specific version of the Flask package.

exec { 'install_pip3':
  command => 'apt-get install -y python3-pip',
  path    => ['/usr/bin', '/usr/sbin'],
  unless  => 'which pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['install_pip3'],
}
