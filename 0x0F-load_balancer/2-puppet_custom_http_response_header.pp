# automating the task of creating a custom HTTP header response
include 'apt'
package { 'nginx': ensure => installed, require => Class['apt'], }
file_line { 'nginx_custom_header':
  path   => '/etc/nginx/sites-available/default',
  line   => '    add_header X-Served-By $hostname;',
  after  => '    listen 80 default_server;',
  notify => Service['nginx'],
}
service { 'nginx': ensure => running, enable => true, require => Package['nginx'], }
