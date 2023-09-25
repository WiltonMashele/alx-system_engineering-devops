# changes to our configuration file.

class ssh_client_config {

  file_line { 'ssh_identity_file':
    path => '/etc/ssh/ssh_config',
    line => '    IdentityFile ~/.ssh/school',
  }

  file_line { 'ssh_password_auth':
    path => '/etc/ssh/ssh_config',
    line => '    PasswordAuthentication no',
  }

}
