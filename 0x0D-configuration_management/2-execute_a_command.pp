# Uses Puppet to create a manifest that kills a specific process

exec { 'process kill':
  command  => 'pkill killmenow',
  provider => shell,
}
