#!/usr/bin/pup

# This Puppet manifest installs a specific version of the Flask package.
package { 'flask':
  name     => 'flask',
  ensure   => '2.1.0',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
  provider => 'pip3',
}
