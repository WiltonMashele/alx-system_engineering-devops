# changes to our configuration file.

class ssh_config {

  file_line { 'Set Identity File':
    path => '/etc/ssh/ssh_config',
    line => '    IdentityFile ~/.ssh/school',
  }

  file_line { 'Disable Password Authentication':
    path => '/etc/ssh/ssh_config',
    line => '    PasswordAuthentication no',
  }

}
