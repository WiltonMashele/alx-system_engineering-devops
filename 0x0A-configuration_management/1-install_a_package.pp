#!/usr/bin/pup

# This Puppet manifest installs a specific version of the Flask package.
package { 'Flask Package Installation':
  name     => 'flask',
  ensure   => '2.1.0',
  provider => 'pip3',
}
