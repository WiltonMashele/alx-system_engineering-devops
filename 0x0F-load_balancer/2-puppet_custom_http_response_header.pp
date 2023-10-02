# automating the task of creating a custom HTTP header response.
class nginx_custom_header {

  exec { 'update_apt':
    command => 'apt-get update',
    path    => ['/usr/bin', '/usr/sbin'],
  }

  package { 'nginx':
    ensure  => installed,
    require => Exec['update_apt'],
  }

  file_line { 'add_custom_header':
    ensure  => present,
    path    => '/etc/nginx/nginx.conf',
    line    => '    add_header X-Served-By ${hostname};',
    match   => '^    add_header X-Served-By',
    after   => 'http {',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => Package['nginx'],
  }
}

include nginx_custom_header
