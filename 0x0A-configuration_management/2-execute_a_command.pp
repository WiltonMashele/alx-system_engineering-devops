# manifest that kills a process named killmenow

exec { 'kill_killmenow_process':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}
