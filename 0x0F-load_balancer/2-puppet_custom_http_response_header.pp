# automating the task of creating a custom HTTP header response
class nginx_setup {

  package { 'nginx':
    ensure => installed,
    before => File_line['add_header'],
  }

  file_line { 'add_header':
    path => '/etc/nginx/nginx.conf',
    line => '    add_header X-Served-By "${hostname}";',
    match => '^    include /etc/nginx/sites-enabled/\*;$',
    after => Service['nginx'],
  }

  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }
}

include nginx_setup
